#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from xcampy.camera import XCam

class Image(XCam):
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

    def take_an_image(self, output_path, file_name):
        output = output_path + os.sep + file_name
        #self.camera.camera.start_preview(alpha=50)
        #time.sleep(3)
        self.camera.camera.capture(output)
        #self.camera.camera.stop_preview()