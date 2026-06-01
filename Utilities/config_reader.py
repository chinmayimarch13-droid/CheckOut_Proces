import configparser

config = configparser.ConfigParser()
config.read("config.ini")

def get_url():
    return config.get("settings", "url")
