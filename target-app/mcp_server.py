from fastapi import FastAPI  
app = FastAPI(title="Enterprise MCP Core")  
@app.get("/tools")  
def list_mcp_tools():  
    return {"tools": [{"name": "query_vector_db", "description": "Fetches semantic knowledge from Pi 3B Node 1"}]} 
