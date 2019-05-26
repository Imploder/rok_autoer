from utils.logger import Logger
from utils.screen import Utils


class BarbarianCombat:
    """Class for fighting barbarians"""

    def __init__(self, config, stats):
        """
        Initialises the combat module
        :param config: Config class instance
        :param stats: Stats class instance
        """
        self.config = config
        self.stats = stats
        self.on_map = False

    def navigate_to_map(self):
        """Checks whether to and navigates to the map screen"""
        screen_utilities = Utils()
        location = screen_utilities.find('map')
        if location is not None:
            coordinates = (location.x, location.y)
            screen_utilities.click(coordinates)
            self.on_map = True
        else:
            on_map = screen_utilities.find('city')
            if on_map is not None:
                Logger.log_message("message", "Already on map screen")
                self.on_map = True
            else:
                Logger.log_message("error", "Move to the city or map screen")
