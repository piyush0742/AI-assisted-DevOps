import subprocess
import requests
import sys

# ========================
# CONFIG (EDIT THIS)
# ========================

NAMESPACE = "auth-ns"          # change if needed
POD_NAME = "order-service"     # partial name is OK
CONTAINER_NAME = None          # set to "order-service" if multi-container pod
AI_API_URL = "http://127.0.0.1:8000/summarize"

TAIL_LINES = "50"
SINCE_TIME = "05m"

# ========================
# HELPERS
# ========================

def get_pod_name():
    """
    Finds the full pod name using partial match
    """
    cmd = [
        "kubectl", "get", "pods",
        "-n", NAMESPACE,
        "--no-headers"
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print("❌ Failed to get pods")
        print(result.stderr)
        sys.exit(1)

    for line in result.stdout.splitlines():
        if POD_NAME in line:
            return line.split()[0]

    print(f"❌ Pod containing '{POD_NAME}' not found")
    sys.exit(1)


def get_logs(pod):
    """
    Fetch logs from Kubernetes
    """
    cmd = [
        "kubectl", "logs", pod,
        "-n", NAMESPACE,
        "--tail", TAIL_LINES,
        "--since", SINCE_TIME
    ]

    if CONTAINER_NAME:
        cmd.extend(["-c", CONTAINER_NAME])

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print("❌ Failed to fetch logs")
        print(result.stderr)
        sys.exit(1)

    if not result.stdout.strip():
        print("⚠️ No logs found")
        sys.exit(0)

    return result.stdout


def send_to_ai(logs):
    """
    Send logs to local AI (FastAPI + LLaMA)
    """
    response = requests.post(
        AI_API_URL,
        json={"logs": logs},
        timeout=30
    )

    if response.status_code != 200:
        print("❌ AI service error")
        print(response.text)
        sys.exit(1)

    return response.json()


# ========================
# MAIN
# ========================

def main():
    print("🔍 Finding pod...")
    pod = get_pod_name()
    print(f"✅ Pod found: {pod}")

    print("📥 Fetching logs...")
    logs = get_logs(pod)
    print("✅ Logs fetched")

    print("🧠 Sending logs to AI...")
    result = send_to_ai(logs)

    print("\n================ AI SUMMARY ================\n")
    print(result.get("summary", "No summary returned"))
    print("\n===========================================\n")


if __name__ == "__main__":
    main()
