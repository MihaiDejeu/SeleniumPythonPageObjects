import time

import pytest

from Pages.CarBase import CarBase
from Pages.HomePage import HomePage
from Pages.NewCarsPage import NewCarsPage
from Pages.RegistrationPage import RegistrationPage
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
import logging
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_CarWale(BaseTest):

    @pytest.mark.skip
    def test_goToNewCar(self):
        log.logger.info("*****Inside New Car Test*****")
        home = HomePage(self.driver)
        home.goToNewCars()
        time.sleep(3)

    @pytest.mark.skip
    @pytest.mark.parametrize("carBrand, carTitle", dataProvider.get_data("NewCarsTest"))
    def test_selectCars(self, carBrand, carTitle):
        log.logger.info("******Inside Select Cars Test******")
        home = HomePage(self.driver)
        car = CarBase(self.driver)

        print("Car brand is ", carBrand)
        if carBrand == "BMW":
            home.goToNewCars().selectBMW()
            title = car.getCartTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Honda":
            home.goToNewCars().selectHonda()
            title = car.getCartTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Toyota":
            home.goToNewCars().selectToyota()
            title = car.getCartTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Hyundai":
            home.goToNewCars().selectHyundai()
            title = car.getCartTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"

    @pytest.mark.parametrize("carBrand, carTitle", dataProvider.get_data("NewCarsTest"))
    def test_printCarNamesAndPrices(self, carBrand, carTitle):
        log.logger.info("******Inside Select Cars Test******")
        home = HomePage(self.driver)
        car = CarBase(self.driver)

        print("Car brand is ", carBrand)
        if carBrand == "BMW":
            home.goToNewCars().selectBMW()
            title = car.getCartTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNamesAndPrices()
        # elif carBrand == "Honda":
        #     home.goToNewCars().selectHonda()
        #     title = car.getCartTitle()
        #     print("Car title is: " + title)
        #     assert title == carTitle, "Not on the correct page as title is not matching"
        #     car.getCarNamesAndPrices()
        # elif carBrand == "Toyota":
        #     home.goToNewCars().selectToyota()
        #     title = car.getCartTitle()
        #     print("Car title is: " + title)
        #     assert title == carTitle, "Not on the correct page as title is not matching"
        #     car.getCarNamesAndPrices()
        elif carBrand == "Hyundai":
            home.goToNewCars().selectHyundai()
            title = car.getCartTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNamesAndPrices()

        time.sleep(3)
