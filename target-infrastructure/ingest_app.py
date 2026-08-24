from fastapi import FastAPI, Request  
import json  
import datetime  
app = FastAPI(title="Enterprise Ingestion Pipe")  
@app.post("/submit-feedback")  
async def ingest_log(request: Request):  
    try:  
        payload = await request.json()  
        payload["ingest_timestamp"] = str(datetime.datetime.now())  
        with open("/var/log/enterprise_ingest.log", "a") as f:  
            f.write(json.dumps(payload) + "\n")  
        return {"status": "ingested", "code": 202}  
    except Exception as e:  
        return {"status": "error", "message": str(e)}, 400 
