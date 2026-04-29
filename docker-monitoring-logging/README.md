# 📊 Docker Monitoring & Logging Project (Prometheus + Grafana + ELK)

## 🚀 Overview

This project demonstrates a **production-style observability stack** using:

* Prometheus (Metrics Collection)
* Grafana (Visualization)
* ELK Stack (Logging: Elasticsearch, Logstash, Kibana)
* Docker Compose (Container Orchestration)

---

## 🧱 Architecture

Client → Flask App → Logs → Logstash → Elasticsearch → Kibana
Client → Flask App → Metrics → Prometheus → Grafana

---

## ⚙️ Tech Stack

* Python (Flask)
* Docker & Docker Compose
* Prometheus
* Grafana
* Elasticsearch, Logstash, Kibana (ELK)

---

## 📁 Project Structure

docker-monitoring-logging/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── prometheus/
│   └── prometheus.yml
│
├── logstash/
│   └── logstash.conf
│
├── docker-compose.yml
└── README.md

---
                ┌──────────────┐
                │   Browser    │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │  Flask App   │
                │ (Container)  │
                └──────┬───────┘
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
┌──────────────┐              ┌──────────────┐
│ Prometheus   │              │   Logstash   │
│ (Metrics)    │              │ (Log Parser) │
└──────┬───────┘              └──────┬───────┘
       │                              │
       ▼                              ▼
┌──────────────┐              ┌──────────────┐
│   Grafana    │              │ Elasticsearch│
│ (Dashboard)  │              │ (Storage)    │
└──────────────┘              └──────┬───────┘
                                     ▼
                              ┌──────────────┐
                              │   Kibana     │
                              │ (Visualization)
                              └──────────────┘


============================================================================
## ▶️ Run the Project

```bash
docker-compose up --build
```

---

## 🌐 Access URLs

| Service    | URL                   |
| ---------- | --------------------- |
| Flask App  | http://localhost:5000 |
| Prometheus | http://localhost:9090 |
| Grafana    | http://localhost:3001 |
| Kibana     | http://localhost:5601 |

---

## 📊 Metrics Example

```text
flask_http_request_total
rate(flask_http_request_total[1m])
```

---

## 📈 Features

✅ Real-time monitoring with Prometheus
✅ Visualization with Grafana dashboards
✅ Centralized logging with ELK stack
✅ Containerized microservice architecture

---

## 🚧 Future Improvements

* Add cAdvisor (container metrics)
* Add Node Exporter (host metrics)
* Add Alertmanager (alerting)
* Replace ELK with Loki (lightweight logging)
* Kubernetes deployment (Prometheus Operator)

---

## 💡 Learning Outcome

* Observability fundamentals (metrics + logs)
* Prometheus querying (PromQL)
* Docker-based monitoring architecture
* Real-time system monitoring

---

## 🧠 Author

Ashish Mondal
DevOps | Cloud | Observability Enthusiast 🚀
