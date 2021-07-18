#!/bin/bash
sudo apt-get update
sudo apt-get install -y redis-server python3 python3-pip 
pip3 install -r requirements.txt
sudo service redis-server restart
python3 worker.py &
python3 app.py
