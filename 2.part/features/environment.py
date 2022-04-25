#!/usr/bin/env python3

from configparser import RawConfigParser
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

PAGE = "http://localhost:8080/VALU3S"

def get_webdriver():
    # Get Chrome/Firefox driver from Selenium Hub
    try:
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                      desired_capabilities=DesiredCapabilities.CHROME)
    except WebDriverException:
        print("Cannot connect to chrome")
        exit()
    driver.implicitly_wait(1)
    return driver 


def before_all(context):
    context.driver = get_webdriver()
    context.base_url = PAGE

def after_all(context):
    context.driver.quit()


def after_scenario(context, scenario):
    # teardown 
    ## if there was something created clear it 
    for i in range(2):
        try:
            teardown(context)
        except:
            pass
 
    try:
        context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
        context.driver.find_element(By.ID, "personaltools-logout").click()
    except:
        pass


## remove created elements
def teardown(context):
    context.driver.get("http://localhost:8080/repo/folder_contents")
    context.driver.find_element(By.CSS_SELECTOR, "#contentview-folderContents span:nth-child(2)").click()
    context.driver.find_element(By.ID, "select8InputCheckbox").click()
    element = context.driver.find_element(By.ID, "btn-structure-rearrange")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = context.driver.find_element(By.ID, "btn-paste")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = context.driver.find_element(By.ID, "btn-delete")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element, 0, 0).perform()
    context.driver.find_element(By.CSS_SELECTOR, ".glyphicon-trash").click()
    element = context.driver.find_element(By.CSS_SELECTOR, ".glyphicon-trash")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element, 0, 0).perform()
    context.driver.find_element(By.CSS_SELECTOR, ".applyBtn").click()
    element = context.driver.find_element(By.ID, "btn-tags")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element, 0, 0).perform()