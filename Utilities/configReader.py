from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read('C:\\UdemySeleniumCourse\Advanced\PageObjectModelFramework\ConfigurationData\conf.ini')
    return config.get(section, key)
