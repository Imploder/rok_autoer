import numpy
import pyautogui
import cv2
from datetime import datetime, timedelta
from time import sleep
from random import uniform
from utils.adb import Adb


class Region:
    """A section of the screen"""
    x, y, w, h = 0, 0, 0, 0

    def __init__(self, x, y, w, h):
        """
        Initialises the region
        :param x: Initial x coordinate of the region (top-left).
        :param y: Initial y coordinate of the region (top-left).
        :param w: Width of the region
        :param h: Height of the region
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h


class Utils:
    """Tools to interact with and check the screen"""

    DEFAULT_SIMILARITY = 0.90
    DEFAULT_WAIT = 5

    @staticmethod
    def sleep(min_sleep=None, max_sleep=None):
        """
        Causes the script to wait for a set amount of time, useful for when wait methods fail
        :param min_sleep: the minimum amount of time to wait
        :param max_sleep: the maximum amount of time to wait
        """
        if min_sleep is None:
            sleep(uniform(0.3, 0.5))
        else:
            max_sleep = min_sleep if max_sleep is None else max_sleep
            sleep(uniform(min_sleep, max_sleep))

    @classmethod
    def update_screen(cls):
        """Takes a screen shot of the screen, converts it to be OpenCV readable and returns it"""
        # image = pyautogui.screenshot(region=(0, 0, 1280, 720))
        # return cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2GRAY)
        decoded = None
        while decoded is None:
            decoded = cv2.imdecode(
                numpy.fromstring(
                    Adb.run_command_exec('screencap -p'), dtype=numpy.uint8), 0)
        return decoded

    @staticmethod
    def output_screen(name):
        """Takes a screenshot of the screen and saves it to a file"""
        Adb.run_command_exec(f'screencap /sdcard/{name}.png')
        print("Screenshot taken")

    @classmethod
    def click(cls, coordinates):
        """
        Clicks at the given coordinates
        :param coordinates: List of the x and y coordinate to click
        """
        # pyautogui.click(coordinates[0] + 1, coordinates[1] + 1)
        Adb.run_command_shell(f"input tap {coordinates[0]} {coordinates[1]}")

    @classmethod
    def find(cls, image: str, similarity=DEFAULT_SIMILARITY):
        """
        Finds the specified image on the screen
        :param image: The image to be found as a file name string
        :param similarity: How much in percent the image should match
        :return: A region class with coordinate variables, or None if image not found
        """
        screen = cls.update_screen()
        image_to_find = cv2.imread(f"assets/{image}.png", 0)
        width, height, = image_to_find.shape[::-1]

        result = cv2.matchTemplate(screen, image_to_find, cv2.TM_CCOEFF_NORMED)
        value, location = cv2.minMaxLoc(result)[1], cv2.minMaxLoc(result)[3]
        if value >= similarity:
            return Region(location[0], location[1], width, height)
        return None

    @classmethod
    def find_and_click(cls, image, similarity=DEFAULT_SIMILARITY):
        """
        Finds an image on the screen and clicks it
        :param image: The image to find
        :param similarity: How much in percent the image should match
        :return: True if image was found, false if not
        """
        region = cls.find(image, similarity)
        if region is not None:
            coordinates = (region.x, region.y)
            cls.click(coordinates)
            return True
        return False

    @classmethod
    def wait_and_find(cls, image, wait=DEFAULT_WAIT, similarity=DEFAULT_SIMILARITY):
        """
        Continue to try to find the image for a set amount of time
        :param image: The image to find
        :param wait: The time in seconds to try to find the image
        :param similarity: How much in percent the image should match
        :return: A region class with coordinate variables or None if image not found
        """
        wait_time = datetime.now() + timedelta(seconds=wait)
        while datetime.now() < wait_time:
            region = cls.find(image, similarity)
            if region is not None:
                return region
        return None

    @classmethod
    def wait_and_click(cls, image, wait=DEFAULT_WAIT, similarity=DEFAULT_SIMILARITY):
        """
        Continue to try to find the image for a set amount of time and then click it
        :param image: The image to find
        :param wait: The time in seconds to try to find the image
        :param similarity: How much in percent the image should match
        :return: True if image was found, false if not
        """
        wait_time = datetime.now() + timedelta(seconds=wait)
        while datetime.now() < wait_time:
            if cls.find_and_click(image, similarity):
                return True
        return False

