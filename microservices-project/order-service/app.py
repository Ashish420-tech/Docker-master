from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify({
        "orders": [
            {"id": 101, "product": "Laptop"},
            {"id": 102, "product": "Phone"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
