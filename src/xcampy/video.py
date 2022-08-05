#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
from picamera import PiCamera

class Video():
    """
    Class for...
    """

    def __init__(self, rotation=180, resolution=(1920, 1080), frame_rate=15):
        """
        The constructor for XCam class.
        Arguments:
            None.
        Returns:
            None.
        Tips:
        None.
        """
        self.rotation = rotation
        self.resolution = resolution
        self.frame_rate = frame_rate

    def take_a_video(self, recording_time, output_path, file_name):
        output = output_path + os.sep + file_name
        try:
            camera = PiCamera()
            camera.rotation = self.rotation
            camera.resolution = self.resolution
            camera.framerate = self.frame_rate
            camera.start_recording(output)
            time.sleep(recording_time)
            camera.stop_recording()
            pass
        finally:
            camera.close()