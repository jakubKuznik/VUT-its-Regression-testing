#!/usr/bin/env python3

from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# 9 #
@given(u'Administrator is logged in')
def step_impl(context):
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.ID, "personaltools-login").click()
    context.driver.find_element(By.ID, "__ac_name").send_keys("administrator")
    context.driver.find_element(By.ID, "__ac_password").send_keys("administrator")
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()
@given(u'a web browser is on "Test case creation" page')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
    context.driver.find_element(By.ID, "test_case").click()
@given(u'all required fields are filled for test case')
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("test_case test")
    context.driver.find_element(By.ID, "form-widgets-test_case_id").click()
    context.driver.find_element(By.ID, "form-widgets-test_case_id").send_keys("420")
@when(u'Administrator click on "Save" button')
def step_impl(context):
    context.driver.find_element(By.ID, "form-buttons-save").click()
@then(u'test case is visible in "Test Cases" page')
def step_impl(context):
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.LINK_TEXT, "test_case test").click()


# 10 #
@given(u'a web browser is on "Evaluation scenario creation" page')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
    context.driver.find_element(By.ID, "evaluation_scenario").click()
@given(u'all required fields are filled for evaluation scenario')
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("test eval 420")
    context.driver.find_element(By.ID, "form-widgets-evaluation_secnario_id").send_keys("420")
    context.driver.find_element(By.ID, "form-widgets-evaluation_scenario_textual_description").click()
@then(u'Evaluation scenario is visible in "Evaluation scenario page"')
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-evaluation_scenario_textual_description").send_keys("neco neco")


# 11 #
@given(u'tool is created')
def step_impl(context):
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
    context.driver.find_element(By.ID, "tool").click()
    context.driver.switch_to.frame(2)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    context.driver.switch_to.default_content()
    element = context.driver.find_element(By.CSS_SELECTOR, "#mceu_127 > .mce-open")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "#mceu_127 > .mce-open")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element, 0, 0).perform()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys("test tool 420")
    context.driver.find_element(By.ID, "form-widgets-tool_purpose").send_keys("neco neco")
    element = context.driver.find_element(By.CSS_SELECTOR, "#mceu_125-button > .mce-ico")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element, 0, 0).perform()
    context.driver.switch_to.frame(2)
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>neco&nbsp;</p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.switch_to.frame(1)
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>neco</p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.switch_to.frame(0)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>neco</p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.find_element(By.ID, "form-buttons-save").click()
    exit(0)
@given(u'a web browser is on "Tools" page')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Tools").click()
@given(u'tool "checkbox" is selected')
def step_impl(context):

    raise NotImplementedError(u'STEP: Given tool "checkbox" is selected')
@when(u'Administrator click on "Delete" button (trash bin)')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Administrator click on "Delete" button (trash bin)')
@then(u'Tool is not visible in "Tools page"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Tool is not visible in "Tools page"')
