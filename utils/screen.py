import numpy
import pyautogui
import cv2
from utils.logger import Logger


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

    DEFAULT_SIMILARITY = 0.95
    DEFAULT_WAIT = 2

    @classmethod
    def update_screen(cls):
        """Takes a screen shot of the screen, converts it to be OpenCV readable and returns it"""
        image = pyautogui.screenshot(region=(0, 0, 1280, 720))
        return cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2GRAY)

    @classmethod
    def find(cls, image: str, similarity=DEFAULT_SIMILARITY):
        """
        Finds the specified image on the screen
        :param image: The image to be found as a file name string
        :param similarity: How much in percent the image should match
        :return: A region class with coordinate variables, or None if image not found
        """
        screen = cls.update_screen()
        image_to_find = cv2.imread(f"../assets/{image}.png", 0)
        width, height, = image_to_find.shape[::-1]

        result = cv2.matchTemplate(screen, image_to_find, cv2.TM_CCOEFF_NORMED)
        value, location = cv2.minMaxLoc(result)[1], cv2.minMaxLoc(result)[3]
        if value >= similarity:
            return Region(location[0], location[1], width, height)
        Logger.log_message("error", f"Could not find {image}.png in screen shot")
        return None

    @classmethod
    def click(cls, coordinates):
        """
        Clicks at the given coordinates
        :param coordinates: List of the x and y coordinate to click
        """
        pyautogui.click(coordinates[0], coordinates[1])
