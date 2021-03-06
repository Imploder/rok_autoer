from time import strftime
import colorama


class Logger:

    colorama.init()
    LOG_MSG = '\033[94m'
    LOG_SUCCESS = '\033[92m'
    LOG_WARNING = '\033[93m'
    LOG_ERROR = '\033[91m'
    LOG_INFO = '\33[33m'
    LOG_END = '\033[0m'

    @staticmethod
    def _log_add_time(message):
        """
        Method which adds a timestamp to a log message
        :param message: message to add a time to
        :return: message with a time stamp attached
        """
        return f"{strftime('%Y-%m-%d %H:%M:%S')} {message}"

    @staticmethod
    def _assign_log_type(message_type='message'):
        """
        converts the message type into a colour to use
        :param message_type: the message type (message, success, warning, error)
        :return: the message colour
        """
        message_type = message_type.lower()
        if message_type == "message":
            message_type = Logger.LOG_MSG
        elif message_type == "success":
            message_type = Logger.LOG_SUCCESS
        elif message_type == "warning":
            message_type = Logger.LOG_WARNING
        elif message_type == "error":
            message_type = Logger.LOG_ERROR
        elif message_type == "info":
            message_type = Logger.LOG_INFO
        else:
            raise Exception(f"Invalid log message type: {message_type}")
        return message_type

    @staticmethod
    def log_message(message_type, message):
        self = Logger
        """
        Method which prints a log message to the console with colours
        :param message_type: the type of message (Message, success, failure, error)
        :param message: The message to colour and print
        """
        print(f"{self._assign_log_type(message_type)}{self._log_add_time(message)}{self.LOG_END}")
