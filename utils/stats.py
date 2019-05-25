from utils.logger import Logger
from datetime import datetime


class Stats(object):
    """Tracks stats"""
    def __init__(self):
        """Initialises the Stats class"""
        self.start_time = datetime.now()
        self.barbarians_killed = 0
        self.commander_xp_obtained = 0
        self.xp_books_obtained = 0

    def print_stats(self):
        """Prints all stats to the console"""
        time_elapsed = datetime.now() - self.start_time

        Logger.log_message("success", f"Script has been running for: {time_elapsed}")
        Logger.log_message("success", f"You have killed {self.barbarians_killed} barbarians.")
        Logger.log_message("success", f"Your commanders have gained {self.commander_xp_obtained} xp.")
        Logger.log_message("success", f"You have gained {self.xp_books_obtained} xp books.")
