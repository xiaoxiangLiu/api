# coding=utf-8
from selenium.webdriver.common.by import By
from base import Base


class HomePage(Base):

    url = "https://www.baidu.com"
    search_loc = (By.ID, "kw")
    button_loc = (By.ID, "su")

    def search_selenium(self):
        self.find_element(*self.search_loc).send_keys("selenium")
        self.find_element(*self.button_loc).click()
        return self

