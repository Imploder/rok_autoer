from utils.config import Config
from utils.stats import Stats
from utils.screen import sleep
from utils.logger import Logger
from modules.barbarians import BarbarianCombat


class RokAuto:
    """The almighty script"""

    def __init__(self, config):
        self.config = config
        self.stats = Stats(self.config)

    def attack_barbarians(self):
        """Runs the barbarian module"""

        combat_module = BarbarianCombat(self.config, self.stats)
        combat_module.navigate_to_map()
        combat_module.set_search_level()

        while True:
            try:
                combat_module.search_for_barbarian()
                combat_module.attack_barbarian()
                action_point_empty = combat_module.detect_action_points_empty()
                if action_point_empty is not None:
                    Logger.log_message('warning', "You have run out of action points")
                    if 'enabled' in self.config.refill_action_points['RefillActionPoints']:
                        combat_module.refill_action_points()
                        Logger.log_message("success", "Action points refilled")
                    else:
                        Logger.log_message("warning", "Action point refill set to disabled")
                        break
                combat_module.confirm_victory()
            except KeyboardInterrupt:
                Logger.log_message("error", "Script cancelled by user")
                break

        self.stats.print_stats()


configfile = Config('config.ini')
configfile.read_config_file()
script = RokAuto(configfile)
script.attack_barbarians()
