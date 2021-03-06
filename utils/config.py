import configparser
from utils.logger import Logger


class Config:
    """Class which reads the config.ini file and passes values on to the script"""

    def __init__(self, config_file):
        """
        Initialises the config file
        :param config_file: The config.ini file in the root project directory
        """
        Logger.log_message("message", "Initialising config file")
        self.config_file = config_file
        self.barbarians = {'Barbarians': 'disabled'}
        self.barbarian_level = {'BarbarianLevel': 10}
        self.refill_action_points = {'RefillActionPoints': 'disabled'}
        self.xp_mod = {'XPMod': 1.0}

    def read_config_file(self):
        """Reads the config file to set class variables"""
        config = configparser.ConfigParser()
        config.read(self.config_file)

        self.barbarian_level['BarbarianLevel'] = config.getint('BarbarianFarmer', 'BarbarianLevel')
        self.barbarians['Barbarians'] = config.get('BarbarianFarmer', 'Barbarians')
        self.refill_action_points['RefillActionPoints'] = config.get('BarbarianFarmer', 'RefillActionPoints')
        self.xp_mod['XPMod'] = config.getfloat('BarbarianFarmer', 'XPMod')
