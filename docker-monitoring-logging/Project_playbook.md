ssue 1: /metrics 404

✔ Cause: Exporter not initialized
✔ Fix:

metrics = PrometheusMetrics(app)
🔥 Issue 2: No data in Prometheus

✔ Cause: No traffic
✔ Fix:

curl http://localhost:5000
🔥 Issue 3: Port already in use

✔ Cause: Port conflict
✔ Fix:

3001:3000
🔥 Issue 4: Container name conflict

✔ Cause: Duplicate container name
✔ Fix:

docker rm -f flask-app
🔥 Issue 5: Old code running

✔ Cause: Docker cache
✔ Fix:

docker-compose build --no-cache
🔥 Issue 6: Elasticsearch crash

✔ Cause: Memory issue
✔ Fix:

ES_JAVA_OPTS=-Xms512m -Xmx512m
🔥 Issue 7: Prometheus target DOWN

✔ Cause: Wrong service name
✔ Fix:

targets: ['web:5000']
🚀 Final Result

You now have a production-grade observability project:

Monitoring (Prometheus) ✅
Visualization (Grafana) ✅
Logging (ELK) ✅
Debugging experience ✅
