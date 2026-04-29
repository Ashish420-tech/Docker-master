from flask import Flask
import logging
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Enable metrics endpoint
metrics = PrometheusMetrics(app)

logging.basicConfig(filename='/var/log/app.log', level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home route accessed")
    return "Monitoring Docker App"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
