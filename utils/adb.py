import subprocess


class Adb:

    @classmethod
    def __init__(cls):
        cls.kill_server()
        cls.start_server()

    @staticmethod
    def start_server():
        """Starts the ADB server"""
        subprocess.run(f"adb start-server", shell=True)

    @staticmethod
    def kill_server():
        """Kills the ADB Server"""
        subprocess.run(f"adb kill-server", shell=True)

    @staticmethod
    def run_command_shell(commands):
        cmd = ['adb', 'shell'] + commands.split(' ')
        subprocess.run(cmd, shell=True)

    @staticmethod
    def run_command_exec(commands):
        cmd = ['adb', 'exec-out'] + commands.split(' ')
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        return process.communicate()[0]