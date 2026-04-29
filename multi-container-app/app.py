from flask import Flask
import psycopg2
import time
import os

app = Flask(__name__)

def connect_db():
    for i in range(5):
        try:
            conn = psycopg2.connect(
                dbname=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                host="db"
            )
            return conn
        except Exception as e:
            print("DB not ready, retrying...")
            time.sleep(2)
    return None


@app.route("/")
def home():
    conn = connect_db()
    if conn:
        conn.close()   # ✅ important (close connection)
        return "✅ Connected to PostgreSQL!"
    else:
        return "❌ DB connection failed"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
