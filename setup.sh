#!/bin/bash

echo "*******************************"
echo "*  Kamera wird eingeschaltet  *"
echo "*******************************"
# 0=on, 1=off
sudo raspi-config nonint do_camera 0

echo "***************************"
echo "*  System wird upgedatet  *"
echo "***************************"
sudo apt update
yes | sudo apt dist-upgrade

echo "***************************************"
echo "*  Abhängigkeiten werden installiert  *"
echo "***************************************"
yes | sudo apt install apache2 php7.1 ffmpeg git xorg python3 python3-picamera python3-pyqt5 python3-pyqt5.qtwebkit lightdm python3-rpi.gpio

echo "********************************"
echo "*  Installation der FotoKiste  *"
echo "********************************"
git clone https://github.com/MichaelGier/FotoKiste.git /home/pi/fotobox

echo "*****************************"
echo "*  Konfiguration AutoStart  *"
echo "*****************************"
mkdir -p ~/.config/openbox
echo "xset s noblank" >> ~/.config/openbox/autostart
echo "xset s off" >> ~/.config/openbox/autostart
echo "xset -dpms" >> ~/.config/openbox/autostart
echo "cd ~/fotobox/ ; python3 fotobox.py | tee fotobox.log" >> ~/.config/openbox/autostart

# GUI-Boot with autologin
sudo raspi-config nonint do_boot_behaviour B4

echo "****************"
echo "*  Syncing...  *"
echo "****************"
sudo sync
