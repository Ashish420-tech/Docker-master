🔹 Basic Questions
Q1: What is Prometheus?

👉 Monitoring system that collects time-series metrics via scraping.

Q2: Why use rate()?

👉 Converts cumulative counters into real-time values (RPS).

Q3: Why was your graph flat initially?

👉 No traffic → counters didn’t increase.

Q4: Difference between logs and metrics?
Logs	Metrics
Detailed events	Numeric time-series
Debugging	Monitoring
🔹 Intermediate Questions
Q5: Why /metrics returned 404 earlier?

👉 Exporter not initialized in Flask app.

Q6: Why container rebuild didn’t work initially?

👉 Docker cache + wrong COPY path.

Q7: Why avoid container_name?

👉 Causes conflicts and breaks scaling.

🔹 Advanced Questions
Q8: How does Prometheus collect data?

👉 Pull-based model (scrapes endpoints).

Q9: What is PromQL?

👉 Query language for time-series data.

Q10: How would you scale this?
Use Kubernetes
Add Prometheus Operator
Use Helm charts
