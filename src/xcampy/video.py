#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
from xcampy.camera import XCam

class Video(XCam):
    """
    Class for...
    """

    def __init__(self):
        """
        The constructor for XCam class.
        Arguments:
            None.
        Returns:
            None.
        Tips:
        None.
        """
        self.camera = XCam()

    def take_a_video(self, recording_time, output_path, file_name):
        output = output_path + os.sep + file_name
        self.camera.camera.resolution = (1920, 1080)
        self.camera.camera.start_recording(output)
        time.sleep(recording_time)
        self.camera.camera.stop_recording()
