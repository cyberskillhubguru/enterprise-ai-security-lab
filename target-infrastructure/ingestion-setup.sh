#!/bin/bash  
echo "[*] Updating package index..."  
sudo apt update  
echo "[*] Installing Fluent Bit and Python dependencies..."  
sudo apt install -y td-agent-bit python3-pip python3-venv python3-dev  
echo "[*] Provisioning log workspace and setting permissions..."  
sudo touch /var/log/enterprise_ingest.log  
sudo chmod 666 /var/log/enterprise_ingest.log  
echo "[*] Configuring Fluent Bit collection rules..."  
sudo tee /etc/td-agent-bit/td-agent-bit.conf << 'EOF'  
[SERVICE]  
    Flush        5  
    Log_Level    info  
[INPUT]  
    Name         tail  
    Path         /var/log/enterprise_ingest.log  
    Tag          enterprise.ingest  
[OUTPUT]  
    Name         stdout  
    Match        *  
EOF  
echo "[*] Building isolated Python ingestion execution space..."  
python3 -m venv ingest_env  
./ingest_env/bin/pip3 install fastapi uvicorn  
echo "[*] Launching Ingestion Engine Pipeline over network..."  
sudo systemctl restart td-agent-bit  
sudo systemctl enable td-agent-bit  
echo "[+] Node 4 Ingestion service ready. Starting API server..." 
