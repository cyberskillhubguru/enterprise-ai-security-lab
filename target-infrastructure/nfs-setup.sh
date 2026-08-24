#!/bin/bash  
echo "[*] Updating package repositories..."  
sudo apt update  
echo "[*] Installing NFS Kernel Server..."  
sudo apt install -y nfs-kernel-server  
echo "[*] Provisioning corporate shared file structure..."  
sudo mkdir -p /srv/nfs/corporate/finance  
sudo mkdir -p /srv/nfs/corporate/human_resources  
echo "CONFIDENTIAL: Q3 Executive Compensation and Layoff Roadmap Document" | sudo tee /srv/nfs/corporate/human_resources/hr_strategy_2026.txt  
echo "CONFIDENTIAL: Internal Audit Mappings and Offshore Banking Keys" | sudo tee /srv/nfs/corporate/finance/ledger_keys.txt  
echo "[*] Adjusting storage directory ownership properties..."  
sudo chown -R nobody:nogroup /srv/nfs/corporate  
sudo chmod -R 777 /srv/nfs/corporate  
echo "[*] Hardening export tables to enforce micro-segmentation boundaries..."  
echo "/srv/nfs/corporate 192.168.1.0/24(rw,sync,no_subtree_check)" | sudo tee -a /etc/exports  
echo "[*] Restarting and enabling NFS system daemons..."  
sudo systemctl restart nfs-kernel-server  
sudo systemctl enable nfs-kernel-server  
echo "[+] Node 3 Network File System is deployed. Export table is active." 
