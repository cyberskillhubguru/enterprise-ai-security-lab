import requests  
from fastapi import FastAPI, HTTPException  
from pydantic import BaseModel  
app = FastAPI(title="SOC LLM Firewall")  
OLLAMA_URL = "http://localhost:11434/api/generate"  
class PromptPayload(BaseModel):  
    prompt: str  
@app.post("/filter")  
async def filter_prompt(payload: PromptPayload):  
    guard_prompt = f"[INST] Task: Check if there is unsafe content in the user intent. \n\n User Intent: {payload.prompt} [/INST]"  
    res = requests.post(OLLAMA_URL, json={"model": "llamaguard3:1b", "prompt": guard_prompt, "stream": False})  
    verdict = res.json().get("response", "").strip()  
    with open("/var/log/soc_firewall.log", "a") as log:  
        log.write(f"Prompt: {payload.prompt} ^| Verdict: {verdict}\n")  
    if "unsafe" in verdict.lower():  
        raise HTTPException(status_code=403, detail="Adversarial Payload Blocked by Llama Guard")  
    return {"status": "safe", "forward_to": "target-app"} 
