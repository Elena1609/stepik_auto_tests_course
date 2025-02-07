import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class TestAbs(unittest.TestCase):
    
    def check(self, link):
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.first_class input.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.second_class input.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.third_class input.third")
        input3.send_keys("ivan.petrov@ttt.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(10)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")            
        welcome_text = welcome_text_elt.text
        time.sleep(10)
        browser.quit()
        return welcome_text
    
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = self.check(link)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        
    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = self.check(link)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        
            
        
if __name__ == "__main__":
    unittest.main()