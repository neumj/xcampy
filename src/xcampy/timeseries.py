#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import datetime
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


    def take_n_images(self, n, period, output_path):
        imager = Image()
        for i in range(0, n):
            d = datetime.datetime.now()
            d_str = time.strftime("%Y%m%d%H%M%S", d.timetuple())
            file_name = "image-" + d_str + ".jpg"
            imager.take_an_image(output_path, file_name)
            time.sleep(period)
        
    def take_n_videos(self, n, duration, period, output_path):
        vid = Video()
        for i in range(0, n):
            d = datetime.datetime.now()
            d_str = time.strftime("%Y%m%d%H%M%S", d.timetuple())
            file_name = "video-" + d_str + ".h264"
            vid.take_a_video(duration, output_path, file_name)
            time.sleep(period)

    def image_in_window(self, begin_time_tuple, end_time_tuple, period, output_path):
        imager = Image()    
        begin_time = datetime.datetime(year=begin_time_tuple[0], month=begin_time_tuple[1],
            day=begin_time_tuple[2], hour=begin_time_tuple[3], minute=begin_time_tuple[4],
            second=begin_time_tuple[5])
        end_time = datetime.datetime(year=end_time_tuple[0], month=end_time_tuple[1],
            day=end_time_tuple[2], hour=end_time_tuple[3], minute=end_time_tuple[4],
            second=end_time_tuple[5])
        take = 1
        while take == 1:
            now = datetime.datetime.now()
            if now >= begin_time and now < end_time:
                d = datetime.datetime.now()
                d_str = time.strftime("%Y%m%d%H%M%S", d.timetuple()) 
                imager.take_an_image(output_path, f'image-{d_str}.jpg')
            elif now >= end_time:
                take = 0
            time.sleep(period)

    def video_at_time(self, begin_time_tuple, duration, poll, output_path):
        vid = Video()    
        begin_time = datetime.datetime(year=begin_time_tuple[0], month=begin_time_tuple[1],
            day=begin_time_tuple[2], hour=begin_time_tuple[3], minute=begin_time_tuple[4],
            second=begin_time_tuple[5])
        take = 1
        while take == 1:
            now = datetime.datetime.now()
            if now >= begin_time:
                d = datetime.datetime.now()
                d_str = time.strftime("%Y%m%d%H%M%S", d.timetuple()) 
                vid.take_a_video(duration, output_path, f'video-{d_str}.h264')
                take = 0
            time.sleep(poll)