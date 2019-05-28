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
        in_town = Utils.find_and_click('map')
        if in_town:
            Logger.log_message("success", "Navigated to map screen")
            self.on_map = True
        else:
            on_map = Utils.find('city')
            if on_map:
                Logger.log_message("message", "Already on map")
                self.on_map = True
            else:
                Logger.log_message("error", "Move to the city or map screen")

    def set_search_level(self):
        """Resets the Barbarian Level to 1 and increments it to the desired level"""
        Utils.wait_and_click('search')
        Utils.wait_and_click('search_barbarian')

        Utils.sleep(0.5)

        minus_button = Utils.wait_and_find('search_minus')
        if minus_button is not None:
            Utils.sleep()
            reset_bar_location = (minus_button.x + 45, minus_button.y + 12)
            Utils.click(reset_bar_location)
            Logger.log_message("success", "Reset search level")
        else:
            Logger.log_message("error", "could not find minus button")

        plus_button = Utils.find('search_plus')
        plus_button_location = (plus_button.x, plus_button.y)
        for x in range(self.config.barbarian_level['BarbarianLevel'] - 1):
            Utils.click(plus_button_location)

    @staticmethod
    def search_for_barbarian():
        """Checks for/Navigates to the search button, and clicks it"""
        search_button = Utils.find('search_search')
        if search_button is not None:
            search_button_location = (search_button.x, search_button.y)
            Utils.click(search_button_location)
        else:
            Utils.wait_and_click('search')
            Utils.wait_and_click('search_barbarian')
            Utils.wait_and_click('search_search')

    def attack_barbarian(self):
        """Finds the created barbarian and attacks it with the default army"""
        Utils.sleep()
        Utils.wait_and_click(f"barbarian_{self.config.barbarian_level['BarbarianLevel']}", similarity=0.88)
        Utils.wait_and_click('barbarian_attack')
        Utils.wait_and_click('attack_new_troops', wait=30)
        Utils.sleep(0.5, 3)
        Utils.wait_and_click('attack_march')

    def confirm_victory(self):
        victory = Utils.wait_and_find('victory', wait=60)
        if victory is not None:
            self.stats.increment_barbarian_stats()
        else:
            Logger.log_message("error", "Could not find victorious battle")
            quit()

    @staticmethod
    def detect_action_points_empty():
        action_points_screen = Utils.wait_and_find('action_point_recovery', wait=1)
        if action_points_screen is not None:
            return action_points_screen
        else:
            return None

    def refill_action_points(self):
        action_point_item_100 = Utils.wait_and_find('action_point_100')
        action_point_item_100_location = (action_point_item_100.x, action_point_item_100.y)
        use_button_location = (action_point_item_100_location[0] + 700, action_point_item_100_location[1] + 40)
        for x in range(2):
            Utils.click(use_button_location)
            self.stats.increment_action_point_item()
        Utils.find_and_click('action_point_close')
        Utils.sleep(0.5, 3)
        Utils.wait_and_click('attack_march')
