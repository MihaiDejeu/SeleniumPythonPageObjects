from Utilities import configReader


class CarBase:

    def __init__(self, driver):
        self.driver = driver

    def getCartTitle(self):
        return self.driver.find_element_by_xpath(configReader.readConfig("locators", "carTitle_XPATH")).text

    def getCarNamesAndPrices(self):
        carNames = self.driver.find_elements_by_xpath(configReader.readConfig("locators", "carName_XPATH"))
        carPrices = self.driver.find_elements_by_xpath(configReader.readConfig("locators", "carPrice_XPATH"))

        print("Number of cars found is:", len(carPrices))
        for i in range(1, len(carPrices)):
            print(carNames[i].text + "----Prices are----" + carPrices[i].text)

