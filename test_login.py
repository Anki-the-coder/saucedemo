import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class loginSauce:

    def login(self):
        baseURL = "https://www.saucedemo.com/"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(baseURL)
        driver.find_element_by_css_selector("#user-name").send_keys("standard_user")
        driver.find_element_by_css_selector("#password").send_keys("secret_sauce")
        driver.find_element_by_css_selector("#login-button").click()

        # Start here
        _inventoryItemPrice = driver.find_elements_by_css_selector("div.inventory_item_price")
        _withOutDollarList = []

        for _prices in _inventoryItemPrice:
            _withDollar = str(_prices.text)
            _withOutDollar = _withDollar[1:]

            if int(float(_withOutDollar)) < 20:
                driver.find_element_by_xpath(
                    f"//div[text()='{format(_withOutDollar)}']/parent::div[@class='pricebar']//button").click()
                _withOutDollarList.append(_withOutDollar)

        _samePrice = []
        count = 0

        for i in range(len(_withOutDollarList)):
            for j in range(len(_withOutDollarList)):
                if _withOutDollarList[i] == _withOutDollarList[j]:
                    count = count + 1

            if count > 1:
                if _withOutDollarList[i] not in _samePrice:
                    _samePrice.append(_withOutDollarList[i])

            count = 0

        print(_samePrice)

        for _price in _samePrice:
            print(_price)
            

        # Later
        driver.find_element_by_xpath("//span[@class='fa-layers-counter shopping_cart_badge']").click()
        time.sleep(5)
        driver.find_element_by_link_text("CHECKOUT").click()
        driver.find_element_by_css_selector("#first-name").send_keys("Shreyas")
        driver.find_element_by_css_selector("#last-name").send_keys("Iyer")
        driver.find_element_by_css_selector("#postal-code").send_keys("Trial")
        driver.find_element_by_css_selector("input.btn_primary.cart_button").click()
        driver.find_element_by_css_selector("a.btn_action.cart_button").click()
        # driver.implicitly_wait()


abc = loginSauce()
abc.login()
