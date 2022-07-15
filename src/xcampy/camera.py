#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 17:31:29 2021

@author: pi
"""
import os
import time
import datetime
from picamera import PiCamera

def camera_setup(rotation=180, resolution=(2592, 1944), frame_rate=15):
    #max video resolution: (1920, 1080)
    camera = PiCamera()
    camera.rotation = rotation
    camera.resolution = resolution
    camera.framerate = frame_rate
    
    return camera

def take_a_picture(camera, output_path, file_name):
    output = output_path + os.sep + file_name
    camera.start_preview(alpha=100)
    time.sleep(3)
    camera.capture(output)
    camera.stop_preview()

def take_a_video(camera, recording_time, output_path, file_name):
    output = output_path + os.sep + file_name
    camera.resolution = (1920, 1080)
    camera.start_preview(alpha=255)
    time.sleep(3)
    camera.start_recording(output)
    time.sleep(recording_time)
    camera.stop_recording()
    camera.stop_preview()
    
def take_n_pictures(camera, num_pics, output_path):
    for t in range(0, num_pics):
        d = datetime.datetime.now()
        d_str = time.strftime("%Y%m%d%H%M%S", d.timetuple())
        file_name = "image-" + d_str + ".jpg"
        take_a_picture(camera, output_path, file_name)

#img_num = 0
#now = datetime.datetime.now()    
#begin_time = datetime.datetime(year=2021, month=10, day=5, hour=20, minute=5, second=0)
#end_time = datetime.datetime(year=2021, month=10, day=5, hour=20, minute=7, second=0)    
#take_picture = 1
#
#cam = camera_setup()
#
#while take_picture == 1:
#    now = datetime.datetime.now()
#    if now >= begin_time and now < end_time: 
#        take_a_picture(cam, f'/home/pi/code/camera/image/time/time_{img_num}.jpg')
#        img_num += 1
#    elif now >= end_time:
#        take_picture = 0
#    time.sleep(0.25)