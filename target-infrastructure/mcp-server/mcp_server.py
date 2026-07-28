## This component handles backend system tools. It contains a severe argument injection vulnerability because it ##
## uses raw string concatentation instead of parameterized inputs when executing database queries. ##

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Mock database initialized locally inside the container to simulate the Pi 3B database node
def init_local_records():
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    cursor = conn.cursor()
    # Public Table
    cursor.execute("CREATE TABLE products (name TEXT, price REAL)")
    cursor.execute("INSERT INTO products VALUES ('Secure Firewall', 499.99), ('AI Guardrail Proxy', 250.00)")
    # Restrained Sensitive Table
    cursor.execute("CREATE TABLE enterprise_users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO enterprise_users VALUES ('sysadmin', 'SuperSecurePass2026!'), ('ceo_bob', 'Hunter2IsALie')")
    conn.commit()
    return conn

db_conn = init_local_records()

@app.route("/tools/query_product", methods=["POST"])
def tool_query_product():
    """MCP Tool Endpoint: Exposes product inventory to the LLM layer."""
    data = request.json or {}
    product_name = data.get("product_name", "")
    
    cursor = db_conn.cursor()
    # ❌ VULNERABILITY: Raw string formatting allows raw SQL command injection if arguments are untrusted
    unsafe_query = f"SELECT name, price FROM products WHERE name = '{product_name}'"
    
    print(f"[MCP LOG] Executing Downstream Tool Query: {unsafe_query}")
    
    try:
        cursor.execute(unsafe_query)
        records = cursor.fetchall()
        return jsonify({"status": "success", "result": str(records) if records else "Product not found."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    print("Starting Target MCP Protocol Server Tiers...")
    app.run(host="0.0.0.0", port=5000)
