from utils.config import Config
from utils.stats import Stats
from utils.screen import sleep
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
            combat_module.search_for_barbarian()
            combat_module.attack_barbarian()
            combat_module.confirm_death()
            sleep(25)


configfile = Config('config.ini')
script = RokAuto(configfile)
script.attack_barbarians()
