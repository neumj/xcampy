#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import datetime
from xcampy.camera import XCam
from xcampy.image import Image
from xcampy.video import Video


class TimeSeries():
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
        pass


    def take_n_images(self, num_pics, period, output_path):
        imager = Image()
        for t in range(0, num_pics):
            d = datetime.datetime.now()
            d_str = time.strftime("%Y%m%d%H%M%S", d.timetuple())
            file_name = "image-" + d_str + ".jpg"
            imager.take_an_image(output_path, file_name)
            time.sleep(period)

    def image_in_window(self, begin_time_tuple, end_time_tuple, period, output_path):
        imager = Image()    
        begin_time = datetime.datetime(year=begin_time_tuple[0], month=begin_time_tuple[1],
            day=begin_time_tuple[2], hour=begin_time_tuple[3], minute=begin_time_tuple[4],
            second=begin_time_tuple[5])
        end_time = datetime.datetime(year=end_time_tuple[0], month=end_time_tuple[1],
            day=end_time_tuple[2], hour=end_time_tuple[3], minute=end_time_tuple[4],
            second=end_time_tuple[5])
        take_picture = 1
        while take_picture == 1:
            now = datetime.datetime.now()
            if now >= begin_time and now < end_time:
                d = datetime.datetime.now()
                d_str = time.strftime("%Y%m%d%H%M%S", d.timetuple()) 
                imager.take_an_image(output_path, f'image-{d_str}.jpg')
            elif now >= end_time:
                take_picture = 0
            time.sleep(period)