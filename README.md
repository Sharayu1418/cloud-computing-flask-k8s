# Flask + MongoDB on Kubernetes with Monitoring and Alerting

This repository contains a complete end-to-end deployment of a Flask To-Do web application with MongoDB, containerized using Docker and deployed on Kubernetes (Minikube and AWS EKS). The application is enhanced with health monitoring, rolling updates, autoscaling, and real-time alerting using Prometheus, Alertmanager, and Slack.

This project was completed as part of a Cloud Computing assignment.

---

## Features

* Flask application with MongoDB backend
* Docker containerization and Docker Compose development environment
* Kubernetes deployment on Minikube and AWS EKS
* ReplicaSets, rolling updates, and auto-healing
* Liveness and readiness probes
* Horizontal Pod Autoscaler (HPA) with Metrics Server
* Monitoring using kube-prometheus-stack
* Alerting through Alertmanager and Slack Webhook

---

## Repository Structure

```
.
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
├── Dockerfile
├── docker-compose.yml
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── probes.yaml
│   ├── rolling-update.yaml
│   ├── hpa.yaml
│   └── mongodb-deployment.yaml
├── monitoring/
│   ├── prometheus-rule.yaml
│   ├── alertmanager-config.yaml
│   ├── alertmanager-secret.yaml
│   ├── test-alert.yaml
└── README.md
```

---

## Architecture Overview

Application stack:

* Flask web application
* MongoDB for data storage
* Docker for packaging
* Kubernetes for orchestration
* Prometheus and Alertmanager for monitoring and alerting
* Slack for notifications

Deployment flow:

Local development → Docker Compose
Minikube deployment → Kubernetes objects
AWS EKS deployment → LoadBalancer service → Internet access

---

## Local Development (Docker Compose)

Build and start containers:

```
docker compose up --build
```

Application will be available at:

```
http://localhost:5000
```

---

## Kubernetes Deployment (Minikube)

Start Minikube and configure context:

```
minikube start
kubectl config use-context minikube
```

Deploy the application:

```
kubectl apply -f k8s/
```

Access the service:

```
minikube service flask-todo-service
```

---

## AWS EKS Deployment

Create the cluster, configure kubectl, then deploy the same manifests:

```
kubectl apply -f k8s/
```

Retrieve the LoadBalancer URL:

```
kubectl get svc
```

Open the external address in a browser to verify the application is running on EKS.

---

## Autoscaling (HPA)

Apply Horizontal Pod Autoscaler:

```
kubectl apply -f k8s/hpa.yaml
kubectl top pods
kubectl get hpa
```

HPA will scale pods based on CPU load once metrics are detected.

---

## Monitoring and Alerting Setup

Install kube-prometheus-stack (via Helm).
Create the Alertmanager Secret and AlertmanagerConfig to send alerts to Slack.

Test the alert:

```
kubectl apply -f monitoring/test-alert.yaml
```

Verify alert in Alertmanager UI and Slack channel.

---
## Troubleshooting Summary

| Issue                        | Resolution                                                       |
| ---------------------------- | ---------------------------------------------------------------- |
| Prometheus rule not firing   | Corrected PrometheusRule labels and restarted Prometheus pods    |
| Slack alerts not delivered   | Configured AlertmanagerConfig CRD and valid Slack webhook secret |
| HPA showing unknown metrics  | Patched metrics server to allow insecure TLS                     |
| Pods restarting unexpectedly | Adjusted liveness and readiness probe values                     |
| Rolling update failure       | Correct image tagging and push to Docker Hub                     |

---

## Conclusion

This project demonstrates the deployment and management of a distributed web application on Kubernetes with fault tolerance, scaling, monitoring, and alerting. It validates practical understanding of containerization, orchestration, DevOps monitoring practices, and cloud deployment workflows.

---
