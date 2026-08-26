#!/bin/bash  
echo "[*] Installing Docker dependencies on Pi 5..."  
sudo apt update && sudo apt install -y docker.io docker-compose  
echo "[*] Launching containerized Ollama engine..."  
sudo docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama --restart unless-stopped ollama/ollama  
echo "[*] Pulling Llama Guard model weights (this takes a moment)..."  
sudo docker exec -it ollama ollama run llamaguard3:1b  
echo "[+] Defender Gateway LLM Firewall is active on Port 11434." 
