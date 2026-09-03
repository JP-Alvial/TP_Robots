#!/bin/bash

echo "=== Actualizando repositorios del sistema ==="
sudo apt update && sudo apt upgrade -y

echo "=== Instalando aplicaciones predeterminadas ==="

# Lista tus aplicaciones separadas por un espacio
# El parámetro '-y' acepta automáticamente la confirmación de espacio en disco

sudo apt install -y 'ros-humble-gazebo-*' \
	'ros-humble-cartographer' \
	'ros-humble-cartographer-ros' \
	'ros-humble-navigation2' \
	'ros-humble-nav2-bringup'

source /opt/ros/humble/setup.bash
mkdir -p ~/turtlebot3_ws/src
cd ~/turtlebot3_ws/src/
git clone -b humble https://github.com/ROBOTIS-GIT/DynamixelSDK.git
git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3.git
sudo apt install python3-colcon-common-extensions
cd ~/turtlebot3_ws
colcon build --symlink-install
echo 'source ~/turtlebot3_ws/install/setup.bash' >> ~/.bashrc
source ~/.bashrc


echo "=== ¡Instalación completada con éxito! ==="

$ echo 'export ROS_DOMAIN_ID=30 #TURTLEBOT3' >> ~/.bashrc
$ echo 'source /usr/share/gazebo/setup.sh' >> ~/.bashrc
$ echo 'source /opt/ros/humble/setup.bash' >> ~/.bashrc
$ source ~/.bashrc
