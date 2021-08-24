# JetRacer_Pro - Line following by deep learning
![image](https://github.com/laitathei/JetRacer_Pro/blob/main/Image/view.jpeg)

## A. Flash JetRacer Pro AI Kit Image
1) Please download the JetRacer image through this link:https://drive.google.com/file/d/1bgCAUJ9m16g5FGuYgKy3WmGI-pGjPXN0/view
2) Prepare a SD card (min 32GB) and flash the image to the SD card by Etcher

![image](https://github.com/laitathei/JetRacer_Pro/blob/main/Image/balenaEtcher.png)

3) Insert to Jetson Nano and power it up.

## B. Environmnet installation and setup
*Please connect to a display and connect jetson nano to a network. Afterward, the OLED on JetRacer should be able to display the ip address of itself. If yes, you can contine the following step.*

![image](https://github.com/laitathei/JetRacer_Pro/blob/main/Image/pin.jpeg)

1) Open Jupyter notebook with your ip address through browser (e.g. 192.168.0.134:8888)
![image](https://github.com/laitathei/JetRacer_Pro/blob/main/Image/notebook.png)

2) Configure power mode of Jetson Nano
```
$ sudo nvpmodel -m1
$ sudo nvpmodel -q
```
The response of nano should be MODE : 5W
