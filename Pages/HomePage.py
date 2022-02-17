from Pages.BasePage import BasePage
from Pages.NewCarsPage import NewCarsPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def goToNewCars(self):
        self.moveTo("newCar_XPATH")
        self.click("findNewCar_XPATH")

        return NewCarsPage(self.driver)

    def goToCompareCars(self):
        pass

    def goToUsedCars(self):
        pass