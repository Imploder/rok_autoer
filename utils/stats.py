from utils.logger import Logger
from datetime import datetime


class Stats:
    """Tracks stats"""
    def __init__(self, config_file):
        """
        Initialises the Stats class with information from the config
        :param config_file: The config class
        """
        self.config = config_file
        self.start_time = datetime.now()
        self.barbarians_killed = 0
        self.commander_xp_obtained = 0
        self.xp_books_obtained = 0
        self.action_points_used = 0

    def print_stats(self):
        """Prints all stats to the console"""
        time_elapsed = datetime.now() - self.start_time

        Logger.log_message("message", f"Script has been running for: {str(time_elapsed)[:7]}")
        Logger.log_message("message", f"You have killed {self.barbarians_killed} barbarians.")
        Logger.log_message("message", f"Your commanders have gained {self.commander_xp_obtained} xp.")
        Logger.log_message("message", f"You have gained {str(self.xp_books_obtained)} xp books.")
        Logger.log_message("warning", f"{self.action_points_used} Action point potions have been used.")

    def increment_barbarian_stats(self):
        """Increment the amount of barbarians killed, xp gained, and xp books gained"""
        self.barbarians_killed += 1
        self.commander_xp_obtained += self.config.barbarian_level['BarbarianLevel'] * 100 * self.config.xp_mod['XPMod']
        if self.config.barbarian_level['BarbarianLevel'] % 10 is 0:
            self.xp_books_obtained += 1
        else:
            self.xp_books_obtained += self.config.barbarian_level['BarbarianLevel']

    def increment_action_point_item(self):
        """Increment the amount of action point potions used"""
        self.action_points_used += 1
