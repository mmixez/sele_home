from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://google.com")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)


input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.clear()
input_element.send_keys("Brew Cool youtube" + Keys.ENTER)



WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Brew Cool"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Brew Cool")
link.click()


  #  driver.quit()
time.sleep(60)
driver.quit()
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#
#

