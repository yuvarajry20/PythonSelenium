from configparser import ConfigParser
def get_config(category, key):
    config = ConfigParser()
    config.read('C:\\Users\\yuvar\\PythonSelenium\\PageObjectModel\\Utility\\config.ini')
    return config.get(category, key)