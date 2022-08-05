#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from picamera import PiCamera

class Image():
    """
    Class for...
    """

    def __init__(self, rotation=180, resolution=(2592, 1944)):
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
        

    def take_an_image(self, output_path, file_name):
        output = output_path + os.sep + file_name
        try:
            camera = PiCamera()
            camera.rotation = self.rotation
            camera.resolution = self.resolution
            camera.capture(output)
            pass
        finally:
            camera.close()