## This script handles the user interface. It simulates a native LLM chat gateway that accepts user text, processes it, ##
## and blindly passes the extracted parameters down to the backend MCP server without validation. ##

from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

MCP_SERVER_URL = os.getenv("MCP_SERVER_URL", "http://localhost:5000")

@app.route("/api/chat", methods=["POST"])
def handle_chat_gateway():
    user_prompt = request.json.get("message", "")
    print(f"[FRONTEND LOG] Incoming user interaction received: {user_prompt}")
    
    # Simulating a naive LLM parsing layer: 
    # The application extracts arguments directly from user strings without data-cleansing routines
    extracted_argument = user_prompt.replace("Check price for ", "").strip()
    
    # Forward the parameter to the isolated backend MCP Server Tool via internal container routing
    try:
        mcp_response = requests.post(
            f"{MCP_SERVER_URL}/tools/query_product",
            json={"product_name": extracted_argument},
            timeout=5
        )
        
        if mcp_response.status_code == 200:
            tool_data = mcp_response.json().get("result", "")
            return jsonify({
                "status": "success",
                "llm_response": f"According to the backend MCP enterprise tool, here is the data: {tool_data}"
            })
        else:
            return jsonify({"status": "error", "llm_response": "The downstream MCP tool failed to execute properly."}), 500
            
    except requests.exceptions.RequestException as e:
        return jsonify({"status": "error", "llm_response": f"Failed to connect to backend infrastructure: {e}"}), 500

if __name__ == "__main__":
    print("Starting Front-facing Vulnerable AI Application Gateway...")
    app.run(host="0.0.0.0", port=8000)
