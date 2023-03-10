import configparser


class ConfigHandler:
    def __init__(self, config_path):
        self.config_path = config_path

        with open(self.config_path) as f:
            self.config = configparser.ConfigParser()
            self.config.read_file(f)

    def save_config(self, fields):
        for section in fields:
            for option in fields[section]:
                if (value := fields[section][option].get()) is not None:
                    self.config.set(section, option, str(value))

        with open(self.config_path, "w") as configfile:
            self.config.write(configfile)

    def get_section(self, section):
        return self.config[section] if section in self.config else None

    def get_option(self, section, option, default_value, type=str):
        if self.config.has_option(section, option):
            if type is str:
                return self.config[section][option]
            if type is bool:
                return self.config[section].getboolean(option)
            if type is int:
                return self.config[section].getint(option)
            if type is float:
                return self.config[section].getfloat(option)
        return default_value
