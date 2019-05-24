from time import strftime

class logger():

    LOG_MSG = '\033[94m'
    LOG_SUCCESS = '\033[92m'
    LOG_WARNING = '\033[93m'
    LOG_ERROR = '\033[91m'
    LOG_END = '\033[0m'

    @staticmethod
    def log_add_time(message):
        """
        Method which adds a timestamp to a log mesage
        :param message: message to add a time to
        :return: message with a time stamp attached
        """
        return "[{}] {}".format(strftime("%Y-%m-%d %H:%M:%S"), message)

    @staticmethod
    def assign_log_type(message_type='message'):
        """"""
        message_type.lower()
        if message_type == "message":
            message_type = logger.LOG_MSG
        elif message_type == "success":
            message_type = logger.LOG_SUCCESS
        elif message_type == "warning":
            message_type = logger.LOG_WARNING
        elif message_type == "error":
            message_type = logger.LOG_ERROR
        else:
            raise Exception(f"Invalid log message type: {message_type}")
        return message_type

    @staticmethod
    def log_message(message_type, message):
        self = logger
        """
        Method which prints a log message to the console with colours
        :param type: the type of message (Message, success, failure, error)
        :param message: The message to colour and print
        """
        print(f"{self.assign_log_type(message_type)}{self.log_add_time(message)}{self.LOG_END}")
