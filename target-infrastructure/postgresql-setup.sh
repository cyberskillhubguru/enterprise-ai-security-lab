#!/bin/bash  
sudo apt update  
sudo apt install -y postgresql postgresql-contrib  
PG_VERSION=$(psql --version | awk '{print $3}' | cut -d. -f1)  
sudo sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/g" /etc/postgresql/$PG_VERSION/main/postgresql.conf  
echo "host    all             all             192.168.1.0/24          md5" | sudo tee -a /etc/postgresql/$PG_VERSION/main/pg_hba.conf  
sudo systemctl restart postgresql  
sudo systemctl enable postgresql 
