## Using Automation Driver Install
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options
driver= webdriver.Chrome()
## Getting the Webpage URL
driver.get("https://jqueryui.com/droppable/")
time.sleep(3)

## Switching to the iframe that contains the draggable and droppable elements
iframe= driver.find_element(By.CSS_SELECTOR,".demo-frame")
driver.switch_to.frame(iframe)

## Locating the draggable and droppable elements
draggable=driver.find_element(By.ID,"draggable")
droppable = driver.find_element(By.ID,"droppable")

## Performing drag and drop to the rectangular Box
actions=ActionChains(driver)
actions.drag_and_drop(draggable,droppable).perform()
time.sleep(2)
driver.quit()