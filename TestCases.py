import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains
# import KEYS
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException




class SampleTeseCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        # maximize the window size
        self.driver.maximize_window()


    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.get('http://localhost:3000/')
        

    def test_alphabet(self):
        # find edit text,clear its content and enter some inputs
        self.editText = self.driver.find_element(
            By.XPATH, '/html/body/div/div/input')
        self.editText.clear()
        self.editText.send_keys('mmm')

        self.action = ActionChains(self.driver)

        self.action.key_down(Keys.ENTER).perform()

        time.sleep(3)
        try:
            self.text = self.driver.find_element(By.XPATH, '/html/body/div/div/div/h2/span').text
            self.assertTrue('Mashhad' in self.text)

        except NoSuchElementException:
            pass


    def test_alphabetCity(self):
        # find edit text,clear its content and enter some inputs
        self.editText = self.driver.find_element(
            By.XPATH, '/html/body/div/div/input')
        self.editText.clear()
        self.editText.send_keys('mashhad')

        self.action = ActionChains(self.driver)

        self.action.key_down(Keys.ENTER).perform()

        time.sleep(3)
        try:
            self.text = self.driver.find_element(By.XPATH, '/html/body/div/div/div/h2/span').text
            self.assertTrue('Mashhad' in self.text)

        except NoSuchElementException:
            pass




    def test_numbers(self):
        # find edit text,clear its content and enter some inputs
        self.editText = self.driver.find_element(By.XPATH, '/html/body/div/div/input')
        self.editText.clear()
        self.editText.send_keys('7777')

        self.action = ActionChains(self.driver)

        self.action.key_down(Keys.ENTER).perform()

        time.sleep(4)

        try:
            self.text = self.driver.find_element(By.XPATH, '/html/body/div/div/div/h2/span').text
            self.assertIsNone(self.text)
            
        except NoSuchElementException:
            pass


    def test_MerageNumberAlphabet(self):
        # find edit text,clear its content and enter some inputs

        self.editText = self.driver.find_element(
            By.XPATH, '/html/body/div/div/input')
        self.editText.clear()

        self.editText.send_keys('teh32ran')

        self.action = ActionChains(self.driver)

        self.action.key_down(Keys.ENTER).perform()

        time.sleep(2)

        try:
            self.text = self.driver.find_element(
                By.XPATH, '/html/body/div/div/div/h2/span').text
            self.assertIsNone(self.text)

        except NoSuchElementException:
            pass



    def test_mark(self):

        self.editText = self.driver.find_element(
            By.XPATH, '/html/body/div/div/input')
        self.editText.clear()

        self.editText.send_keys('#@!%$#$&*')

        self.action = ActionChains(self.driver)

        self.action.key_down(Keys.ENTER).perform()

        time.sleep(2)

        try:
            self.text = self.driver.find_element(
                By.XPATH, '/html/body/div/div/div/h2/span').text
            self.assertIsNone(self.text)

        except NoSuchElementException:
            pass


    def test_MergeMarkAlphabet(self):

        self.editText = self.driver.find_element(
            By.XPATH, '/html/body/div/div/input')
        self.editText.clear()

        self.editText.send_keys('#@teh^ran$#@')

        self.action = ActionChains(self.driver)

        self.action.key_down(Keys.ENTER).perform()

        time.sleep(2)

        try:
            self.text = self.driver.find_element(
                By.XPATH, '/html/body/div/div/div/h2/span').text
            self.assertIsNone(self.text)

        except NoSuchElementException:
            pass


    def test_MergeMarkNumber(self):

        self.editText = self.driver.find_element(
            By.XPATH, '/html/body/div/div/input')
        self.editText.clear()

        self.editText.send_keys('#@45^25$#1@')

        self.action = ActionChains(self.driver)

        self.action.key_down(Keys.ENTER).perform()

        time.sleep(2)

        try:
            self.text = self.driver.find_element(
                By.XPATH, '/html/body/div/div/div/h2/span').text
            self.assertIsNone(self.text)

        except NoSuchElementException:
            pass




    def test_MergeMarkAlphabetNumber(self):

        self.editText = self.driver.find_element(
            By.XPATH, '/html/body/div/div/input')
        self.editText.clear()

        self.editText.send_keys('#@mashhad45^25$#1@')

        self.action = ActionChains(self.driver)

        self.action.key_down(Keys.ENTER).perform()

        time.sleep(2)

        try:
            self.text = self.driver.find_element(
                By.XPATH, '/html/body/div/div/div/h2/span').text
            self.assertIsNone(self.text)

        except NoSuchElementException:
            pass


    @classmethod
    def tearDownClass(self):
        self.driver.quit()





if __name__ == "__main__":
    unittest.main()

