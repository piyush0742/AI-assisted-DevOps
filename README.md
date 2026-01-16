# Cloud Observability & FinOps on AWS EKS

📌 Project Overview

This project demonstrates a production-grade Cloud Observability & FinOps setup built on AWS EKS, following real-world DevOps/SRE best practices.
We designed, deployed, and debugged a microservices-based architecture with end-to-end observability, cost awareness**, and secure ingress routing.

The project covers:

* Microservices deployment on EKS
* AWS ALB Ingress Controller
* OpenTelemetry-based tracing
* Prometheus metrics scraping
* Grafana dashboards
* Terraform-based infrastructure provisioning
* Cost & governance-ready structure

---

🏗️ Architecture Summary

Services:

* `auth-service`
* `order-service`
* `payment-service`

Traffic Flow:

```
User → ALB (Ingress) → Kubernetes Service → Pod (FastAPI)
```

Observability Flow:

```
FastAPI → OpenTelemetry → Metrics & Traces → Prometheus → Grafana
```

---

📂 Repository Structure

```
cloud-observability-finops/
│
├── services/                  # Application source code
│   ├── auth-service/
│   ├── order-service/
│   └── payment-service/
│
├── Kubernetes-files/          # K8s manifests
│   ├── auth-service/
│   ├── order-service/
│   └── payment-service/
│
├── terraform/                 # EKS infrastructure
│   └── eks/
│
├── observability/             # Dashboards & configs
├── docs/                      # Architecture & design docs
├── governance/                # Governance placeholders
├── finops/                    # FinOps placeholders
└── README.md
```

---

🚀 Application Stack

Backend

* FastAPI (Python)
* Dockerized services
* Health, metrics & business APIs

Kubernetes

* Namespaces per service
* Deployments & Services
* ALB Ingress Controller

AWS

* EKS Cluster (Terraform)
* ALB (Application Load Balancer)
* IAM Roles & Policies

---

🔍 Observability

1️⃣ Metrics (Prometheus)

Each service exposes:

* `/metrics` endpoint
* Request count
* Latency
* Error rates

Prometheus scrapes metrics using:

* `ServiceMonitor` per service

---

2️⃣ Distributed Tracing (OpenTelemetry)

Implemented using:

* OpenTelemetry SDK
* Auto-instrumented FastAPI spans

Tracked:

* API latency
* Error spans
* Service-level traces

---

3️⃣ Grafana Dashboards

Grafana dashboards include:

📊 Service Overview Dashboard**

* Requests per second (RPS)
* P95 / P99 latency
* Error rate (%)

📊 Pod & Namespace Metrics**

* CPU usage
* Memory usage
* Pod restarts

📊 Ingress Metrics**

* ALB request count
* HTTP status codes
* Target health

Dashboards are:

* Namespace-aware
* Service-specific
* Production-ready

---

🌐 Ingress & Routing

Implemented using **AWS ALB Ingress Controller**.

Path-based routing:

| Path         | Service         |
| ------------ | --------------- |
| `/login`     | auth-service    |
| `/order/*`   | order-service   |
| `/payment/*` | payment-service |

---


💰 FinOps Readiness

* Cost tags defined in Terraform
* Namespace-level cost attribution possible
* Ready for Kubecost / CUR integration

---

🔐 Governance & Security

* IAM least privilege policies
* Namespace isolation
* Ingress controlled exposure

---

🎯 Key Learnings

* Ingress routing ≠ NGINX rewrite
* Health checks are CRITICAL
* Observability must be built-in, not added later
* Logs + Metrics + Traces = Faster debugging
* Infra & App teams must align

---

🧠 Next Enhancements

* Alerting (Alertmanager)
* SLO-based dashboards
* Cost dashboards (Kubecost)
* Canary deployments
* CI/CD pipelines

---
