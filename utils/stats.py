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

    def increment_barbarian_kills(self):
        """Increment the amount of barbarians killed"""
        self.barbarians_killed += 1

    def increment_commander_xp(self, xp):
        """Increment the amount of commander xp"""
        self.barbarians_killed += xp

    def increment_xp_books(self, books):
        """Increment the amount of """
        self.barbarians_killed += books
