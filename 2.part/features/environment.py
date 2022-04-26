#!/usr/bin/env python3

from configparser import RawConfigParser
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

PAGE = "http://localhost:8080/VALU3S"

def get_webdriver():
    # Get Chrome/Firefox driver from Selenium Hub
    try:
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                      desired_capabilities=DesiredCapabilities.CHROME)
    except WebDriverException:
        print("Cannot connect to chrome")
        exit()
    driver.implicitly_wait(2)
    return driver 


def before_all(context):
    context.driver = get_webdriver()
    context.base_url = PAGE

def after_all(context):
    context.driver.quit()


def after_scenario(context, scenario):
    # teardown 
    ## if there was something created clear it 
    for i in range(1):
        try:
            teardown(context)
        except:
            pass
 
    try:
        pass
        #context.driver.get("http://localhost:8080/repo")
        #context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
        #context.driver.find_element(By.ID, "personaltools-logout").click()
    except:
        pass
    context.driver.get("http://localhost:8080/repo")


## remove created elements
def teardown(context):
    for i in range(1):
        try:
            context.driver.get("http://localhost:8080/repo")
            context.driver.find_element(By.CSS_SELECTOR, "#contentview-folderContents span:nth-child(2)").click()
            context.driver.find_element(By.ID, "select8InputCheckbox").click()
            context.driver.find_element(By.CSS_SELECTOR, ".glyphicon-trash").click()
            context.driver.find_element(By.CSS_SELECTOR, ".glyphicon-trash").click()
            time.sleep(0.5)
            context.driver.find_element(By.CSS_SELECTOR, ".applyBtn").click()
        except:
            pass
    #for i in range(50):
        #try:
            #context.driver.get("http://localhost:8080/repo/tools/folder_contents")
            #context.driver.find_element(By.CSS_SELECTOR, "#contentview-folderContents span:nth-child(2)").click()
            #context.driver.find_element(By.ID, "select0InputCheckbox").click()
            #context.driver.find_element(By.CSS_SELECTOR, ".glyphicon-trash").click()
            #context.driver.find_element(By.CSS_SELECTOR, ".glyphicon-trash").click()
            #time.sleep(0.5)
            #context.driver.find_element(By.CSS_SELECTOR, ".applyBtn").click()
        #except:
            #pass


