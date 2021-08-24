#!/usr/bin/env python3
import time
import math
import sys

import torch
import torchvision
import traitlets
import numpy as np
import ipywidgets.widgets as widgets
from jetracer.nvidia_racecar import NvidiaRacecar
from torch2trt import TRTModule
from torch2trt import torch2trt
from jetcam.csi_camera import CSICamera
from utils import preprocess

car = NvidiaRacecar()

print("[SYSTEM] System starts up .... Please wait")

# use the TensorRT to faster inference
CATEGORIES = ['apex']

### use the following code when you are the first time to use
### we need the following code to get the TensorRT version weight

###device = torch.device('cuda')
###model = torchvision.models.resnet18(pretrained=False)
###model.fc = torch.nn.Linear(512, 2 * len(CATEGORIES))
###model = model.cuda().eval().half()
###model.load_state_dict(torch.load('road_following_model.pth'))
###data = torch.zeros((1, 3, 224, 224)).cuda().half()
###model_trt = torch2trt(model, [data], fp16_mode=True)
###torch.save(model_trt.state_dict(), 'road_following_model_trt.pth')
###model_trt = TRTModule()
###model_trt.load_state_dict(torch.load('road_following_model_trt.pth'))

### When you got the TensorRT version weight, change to following code
model_trt = TRTModule()
model_trt.load_state_dict(torch.load('road_following_model_trt.pth'))

print("[OK] Finish to faster inference with TensorRT")

camera = CSICamera(width=224, height=224, capture_fps=65)

# front wheel setting
# car.steering_gain means the maximum rotation of front wheel
# car.steering_offset means the init shifting of front wheel

# back wheel setting
# car.throttle means the maximum speed of back wheel
# car.throttle_gain means the maximum limitation speed of back wheel

# Car parameter
car.throttle = 0.18
car.steering = 0
car.steering_offset = 0

# PID parameter
STEERING_GAIN = 1
STEERING_BIAS = 0.1225

print ("Successful to load parameter")

#If the car wobbles left and right, lower the steering gain
#If the car misses turns, raise the steering gain
#If the car tends right, make the steering bias more negative (in small increments like -0.05)
#If the car tends left, make the steering bias more postive (in small increments +0.05)

while True:
        image = camera.read()
        image = preprocess(image).half()
        output = model_trt(image).detach().cpu().numpy().flatten()
        x = float(output[0])
        pid_steering = x * STEERING_GAIN + STEERING_BIAS 
        print("[OUTPUT] AI-Output:{} PID-Steering:{}".format(x,pid_steering))
        car.steering = pid_steering
