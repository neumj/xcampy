#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from picamera import PiCamera

class XCam:
    """
    Base Class for Camera.
    """

    def __init__(self, rotation=180, resolution=(2592, 1944), frame_rate=15):
        """
        The constructor for XCam class.
        Arguments:
            None.
        Returns:
            None.
        Tips:
        None.
        """
        
        #max video resolution: (1920, 1080)
        self.camera = PiCamera()
        self.camera.rotation = rotation
        self.camera.resolution = resolution
        self.camera.framerate = frame_rate