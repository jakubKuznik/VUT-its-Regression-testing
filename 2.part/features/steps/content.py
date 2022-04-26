#!/usr/bin/env python3

from multiprocessing.connection import wait
from re import I
from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# 9 #
@given(u'Administrator is logged in')
def step_impl(context):
    # login sometimes fail 
    for i in range(2):
        try:
            context.driver.get("http://localhost:8080/repo")
            context.driver.find_element(By.ID, "personaltools-login").click()
            context.driver.find_element(By.ID, "__ac_name").send_keys("administrator")
            context.driver.find_element(By.ID, "__ac_password").send_keys("administrator")
            context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()
        except:
            pass
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
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("evaluation scenario 420")
    context.driver.find_element(By.ID, "form-widgets-evaluation_secnario_id").click()
    context.driver.find_element(By.ID, "form-widgets-evaluation_secnario_id").send_keys("420")
    context.driver.find_element(By.ID, "form-widgets-evaluation_scenario_textual_description").click()
    context.driver.find_element(By.ID, "form-widgets-evaluation_scenario_textual_description").send_keys("420")
@when(u'Administrator click on "Save" button eval')
def step_impl(context):
    context.driver.find_element(By.ID, "form-buttons-save").click()
@then(u'Evaluation scenario is visible in "Evaluation scenario page"')
def step_impl(context):
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.CSS_SELECTOR, "div > img").click()
    context.driver.find_element(By.LINK_TEXT, "evaluation scenario 420").click()

## 11 #
@given(u'tool is created')
def step_impl(context):
    for i in range(2):
        context.driver.get("http://localhost:8080/repo/tools/++add++tool")
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys("tool 420")
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-description").send_keys("neco")
    context.driver.find_element(By.ID, "form-widgets-tool_purpose").send_keys("neco")
    context.driver.switch_to.frame(3)
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>neco</p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.switch_to.frame(2)
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>neco</p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.switch_to.frame(1)
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>neco</p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.switch_to.frame(0)
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>neco</p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.find_element(By.ID, "form-buttons-save").click()
    context.driver.find_element(By.CSS_SELECTOR, ".documentFirstHeading").click()
@given(u'a web browser is on "Tools" page')
def step_impl(context):
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.LINK_TEXT, "Tools").click()
@given(u'tool "checkbox" is selected')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "tool 420").click()
@when(u'Administrator click on "Delete" button (trash bin)')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-actions .plone-toolbar-title").click()
    context.driver.find_element(By.ID, "plone-contentmenu-actions-delete").click()
    element = context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #form-buttons-Delete")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
@then(u'Tool is not visible in "Tools page"')
def step_impl(context):
    try:
        context.driver.get('http://localhost:8080/repo/tools/tool-420')
    except:
        pass

# 12
@given(u'Method is created')
def step_impl(context):
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
    context.driver.find_element(By.ID, "method").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("metod 420")
    context.driver.find_element(By.ID, "form-widgets-method_purpose").send_keys("metod purpose")
    context.driver.switch_to.frame(2)
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>metod desc</p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.execute_script("window.scrollTo(0,1166.6666259765625)")
    context.driver.switch_to.frame(1)
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>metod stren</p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.switch_to.frame(0)
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>metod limita</p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.find_element(By.ID, "form-buttons-save").click()
    context.driver.find_element(By.CSS_SELECTOR, ".documentFirstHeading").click()
@given(u'a web browser is on "method editation" page')
def step_impl(context):
    context.driver.get("http://localhost:8080/repo/metod-420/view")
@given(u'Name textbox is changet to new one')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "fieldset-default").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("metod 4200")
    #context.driver.find_element(By.ID, "form-buttons-save").click()
@then(u'Method page with new name is presented')
def step_impl(context):
    context.driver.get("http://localhost:8080/repo/metod-4200/view")

# 13
@given(u'test is created')
def step_impl(context):
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
    context.driver.find_element(By.ID, "test_case").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("test case 420")
    context.driver.find_element(By.ID, "form-widgets-test_case_id").send_keys("420")
    context.driver.find_element(By.ID, "form-buttons-save").click()
@given(u'a web browser is on "test case editation" page')
def step_impl(context):
    pass
@given(u'"Test Case id" is changed to new one')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)").click()
    context.driver.find_element(By.CSS_SELECTOR, "#formfield-form-widgets-test_case_id > .horizontal > .required").click()
    context.driver.find_element(By.ID, "form-widgets-test_case_id").click()
    context.driver.find_element(By.ID, "form-widgets-test_case_id").send_keys("4200")
@then(u'Method page with same name and new id is created')
def step_impl(context):
    ## todo 
    pass

# 14
@given(u'use case is created')
def step_impl(context):
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
    context.driver.find_element(By.ID, "use_case").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("use case 420")
    context.driver.switch_to.frame(0)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>fdasfsad</p>'}", element)
    context.driver.switch_to.default_content()
@given(u'a web browser is on "Edit Use Case" page')
def step_impl(context):
    context.driver.find_element(By.ID, "form-buttons-save").click()
@given(u'a web browser is at section "VALU3S Framework"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)").click()
    context.driver.find_element(By.ID, "autotoc-item-autotoc-2").click()
@given(u'in "Evaluation Performance Indicator" "V&V process criteria" is chosen')
def step_impl(context):
    dropdown = context.driver.find_element(By.ID, "form-widgets-IFramework-valu3s_evaluation_performance_indicator-from")
    dropdown.find_element(By.XPATH, "//option[. = 'V&V process criteria']").click()
    context.driver.find_element(By.CSS_SELECTOR, "#form-widgets-IFramework-valu3s_evaluation_performance_indicator td:nth-child(2)").click()
    context.driver.find_element(By.CSS_SELECTOR, "#form-widgets-IFramework-valu3s_evaluation_performance_indicator td:nth-child(2) > button:nth-child(1)").click()
@then(u'use case page is presented')
def step_impl(context):
    context.driver.get("http://localhost:8080/repo/use-case-420-1")
@then(u'"V&V process criteria" is pre in "Evaluation Performance Indicator"')
def step_impl(context):
    # teardown
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.LINK_TEXT, "Use Cases").click()
    context.driver.find_element(By.LINK_TEXT, "use case 420").click()
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-actions .plone-toolbar-title").click()
    context.driver.find_element(By.ID, "plone-contentmenu-actions-delete").click()
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #form-buttons-Delete").click()

# 15
@given(u'a web browser is on "home page"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a web browser is on "home page"')
@when(u'administrator click on "Add new... Workflow"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When administrator click on "Add new... Workflow"')
@then(u'Workflow edit page is presented')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Workflow edit page is presented')

