from flask import Flask, request, jsonify
from pymilvus import connections

 
app = Flask(__name__)

def connect_to_milvus():
    connections.connect(
    alias="default",
    host="milvus-app", #milvus-app-milvus
    port="19530"
    )

@app.route("/")
def home():
    return"Home"


@app.route("/api")
def api():
    return"you are hitting the api-endpoint"



@app.route('/test_milvus_connection')
def test_milvus_connection():
    try:
        connect_to_milvus()
        # Perform a simple operation to check the connection
        stats = connections.get_connection_addr("default")
        return f"Connected to Milvus successfully! Connection details: {stats}"
    except Exception as e:
        return f"Failed to connect to Milvus: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
