#!/bin/bash

echo "Kamera wird eingeschaltet"
# 0=on, 1=off
sudo raspi-config nonint do_camera 0

echo "System wird upgedatet"
sudo apt update
yes | sudo apt dist-upgrade

echo "Abhängigkeiten werden installiert"
yes | sudo apt install apache2 php7.0 php7.0-gd libav-tools git

echo "Installation der FotoKiste"
git clone https://github.com/ 