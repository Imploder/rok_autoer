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

    def print_stats(self):
        """Prints all stats to the console"""
        time_elapsed = datetime.now() - self.start_time

        Logger.log_message("success", f"Script has been running for: {str(time_elapsed)[:7]}")
        Logger.log_message("success", f"You have killed {self.barbarians_killed} barbarians.")
        Logger.log_message("success", f"Your commanders have gained {self.commander_xp_obtained} xp.")
        Logger.log_message("success", f"You have gained {str(self.xp_books_obtained)} xp books.")

    def increment_barbarian_stats(self):
        """Increment the amount of barbarians killed, xp gained, and xp books gained"""
        self.barbarians_killed += 1
        self.commander_xp_obtained += self.config.barbarian_level['BarbarianLevel'] * 100
        self.xp_books_obtained += self.config.barbarian_level['BarbarianLevel']
