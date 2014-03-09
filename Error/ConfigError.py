__author__ = 'Donald'


class ConfigError(Exception):

    def __init__(self, configuration, message):
        self.configuration = configuration
        self.message = message

    def __str__(self):
        return repr(str(self.configuration) + ":" + str(self.message))