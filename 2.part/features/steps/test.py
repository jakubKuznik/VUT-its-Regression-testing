#!/usr/bin/env python3

from ast import Pass
from cmath import exp
from multiprocessing.connection import wait
from re import I
from venv import create
from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

## sometimes there is an error that u have to login twice but it is not our test main goal 
def log_itsreviewer(context):
    for i in range(2):
        try:
            context.driver.get("http://localhost:8080/repo")
            context.driver.find_element(By.ID, "personaltools-login").click()
            context.driver.find_element(By.ID, "__ac_name").send_keys("itsreviewer")
            context.driver.find_element(By.ID, "__ac_password").send_keys("itsreviewer")
            context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()
        except:
            pass
def log_admin(context):
    for i in range(2):
        try:
            context.driver.get("http://localhost:8080/repo")
            context.driver.find_element(By.ID, "personaltools-login").click()
            context.driver.find_element(By.ID, "__ac_name").send_keys("administrator")
            context.driver.find_element(By.ID, "__ac_password").send_keys("administrator")
            context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()
        except:
            pass
def logout(context):
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
    context.driver.find_element(By.ID, "personaltools-logout").click()

def delete_tool(context):
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.XPATH, "//li[@id=\'contentview-folderContents\']/a/span[2]").click()
    context.driver.find_element(By.XPATH, "(//a[contains(text(),\'Tools\')])[2]").click()
    element = context.driver.find_element(By.XPATH, "(//a[contains(text(),\'tool 420\')])[2]")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    try:
        context.driver.find_element(By.ID, "select1InputCheckbox").click()
    except:
        return
    element = context.driver.find_element(By.ID, "select1InputCheckbox")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.ID, "btn-delete")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    context.driver.find_element(By.ID, "btn-delete").click()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    context.driver.find_element(By.XPATH, "//div[@id=\'popover-delete\']/div[3]/button").click()

def log_reg_user(context):
    for i in range(2):
        try:
            context.driver.get("http://localhost:8080/repo")
            context.driver.find_element(By.ID, "personaltools-login").click()
            context.driver.find_element(By.ID, "__ac_name").send_keys("administrator")
            context.driver.find_element(By.ID, "__ac_password").send_keys("administrator")
            context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()
        except:
            pass

def create_tool(context):
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


# 1
@given(u'a web browser is on "use case" page')
def step_impl(context):
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
    context.driver.find_element(By.ID, "use_case").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("use case 420")
    context.driver.switch_to.frame(0)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>use case des</p>'}", element)
    context.driver.switch_to.default_content()
@given(u'use case "visibility" state is "public"')
def step_impl(context):
    context.driver.find_element(By.ID, "form-buttons-save").click()
@when(u'Administrator click on "Send back" option from "State" menu')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".label-state-private > span:nth-child(2)").click()
    context.driver.find_element(By.ID, "workflow-transition-publish").click()
@then(u'"Use case" is not shown to User in "Use Cases page"')
def step_impl(context):
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
    context.driver.find_element(By.ID, "personaltools-logout").click()
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.CSS_SELECTOR, ".outer-wrapper").click()
    context.driver.find_element(By.LINK_TEXT, "Use Cases").click()
    context.driver.find_element(By.LINK_TEXT, "use case 420").click()
    # teardown 
    log_reg_user(context)
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.CSS_SELECTOR, ".outer-wrapper").click()
    context.driver.find_element(By.LINK_TEXT, "Use Cases").click()
    context.driver.find_element(By.LINK_TEXT, "use case 420").click()
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-actions .plone-toolbar-title").click()
    context.driver.find_element(By.ID, "plone-contentmenu-actions-delete").click()
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #form-buttons-Delete").click()
    logout(context)

# 3
@given(u'a Administrator is logged in')
def step_impl(context):
    log_reg_user(context)
@given(u'a requirement is created with no "sharing rights"')
def step_impl(context):
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
    context.driver.find_element(By.ID, "requirement").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys("regui 420")
@given(u'a web browser is on the requirement "sharing page"')
def step_impl(context):
    context.driver.find_element(By.ID, "form-buttons-save").click()
@when(u'Administrator click "Can view checkbox"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#contentview-local_roles span:nth-child(2)").click()
    context.driver.find_element(By.CSS_SELECTOR, ".listingCheckbox:nth-child(5)").click()
    context.driver.find_element(By.NAME, "entries.role_Reader:records").click()
    context.driver.find_element(By.ID, "sharing-save-button").click()
    context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
    context.driver.find_element(By.ID, "personaltools-logout").click()
    context.driver.find_element(By.ID, "personaltools-login").click()
    context.driver.find_element(By.ID, "__ac_name").send_keys("administrator")
    context.driver.find_element(By.ID, "__ac_password").send_keys("administrator")
    context.driver.find_element(By.ID, "__ac_name").click()
    context.driver.find_element(By.ID, "__ac_name").click()
    element = context.driver.find_element(By.ID, "__ac_name")
    actions = ActionChains(context.driver)
    actions.double_click(element).perform()
@when(u'Administrator click on "Save" button specify')
def step_impl(context):
    pass
@then(u'reg_user can see this "requirement" in the "Requirements cathegory"')
def step_impl(context):
    log_itsreviewer(context)
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.CSS_SELECTOR, "div > img").click()
    context.driver.find_element(By.LINK_TEXT, "regui 420").click()

# 4
@given(u'a Tool is created with "Logged-in user can view and edit" sharing right')
def step_impl(context):
    try:
        logout(context)
    except:
        pass
    log_reg_user(context)
    create_tool(context)
    logout(context)
@given(u'User reg_user is logged in')
def step_impl(context):
    log_reg_user(context)
@given(u'a web browser is on "tool editing page"')
def step_impl(context):
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.LINK_TEXT, "Tools").click()
    context.driver.find_element(By.LINK_TEXT, "tool 420").click()
@when(u'reg_user "change name" of Tool to new one')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys("tool 4200")
@when(u'reg_user click on "save" button')
def step_impl(context):
    context.driver.find_element(By.ID, "form-buttons-save").click()
@then(u'Page with new "tool" name is presented to reg_user')
def step_impl(context):
    # teardown
    delete_tool(context)

# 6
@given(u'a test tool is create with "Logged-in user can view it" sharing right')
def step_impl(context):
    create_tool(context)
@given(u'a test method is created with "Logged-in user can view it" sharing right')
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

@given(u'a test "method" has "Tools relation" with "tool"')
def step_impl(context):
    context.driver.find_element(By.ID, "form-buttons-save").click()
    context.driver.find_element(By.CSS_SELECTOR, ".documentFirstHeading").click()
@given(u'a web browser is on the method "sharing page"')
def step_impl(context):
    context.driver.get("http://localhost:8080/repo/metod-420")
@when(u'Administrator click "Can edit" checkbox')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)").click()
@then(u'reg_user cannot edit tool name')
def step_impl(context):
    logout(context)
    log_itsreviewer(context)
    try:
        context.driver.get("http://localhost:8080/repo/metod-420")
        context.driver.get("dasfdu")
    except:
        pass
# 7
@given(u'a web browser is on the Use Cases page')
def step_impl(context):
    try:
        logout(context)
    except:
        pass
    log_admin(context)
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.XPATH, "//li[@id=\'plone-contentmenu-factories\']/a/span[4]").click()
    context.driver.find_element(By.ID, "use_case").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("use case 420")
    context.driver.switch_to.frame(0)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>use case desc&nbsp;</p>'}", element)
    context.driver.switch_to.default_content()
@given(u'a Use Cases has "Logged-in user can add" access right')
def step_impl(context):
    context.driver.find_element(By.ID, "form-buttons-save").click()
@given(u'a reg_user is logged in')
def step_impl(context):
    logout(context)
    log_reg_user(context)
@when(u'If there is "Add new.." button then clik on it')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Use Cases").click()
@then(u'to reg_user is shown')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//li[@id=\'plone-contentmenu-factories\']/a/span[2]").click()
    context.driver.find_element(By.ID, "use_case").click()

# 8 
@when(u'If there is "Add new.. Use Case" button then click on it')
def step_impl(context):
    logout(context)
    log_reg_user(context)
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.XPATH, "//li[@id=\'plone-contentmenu-factories\']/a/span[4]").click()
    context.driver.find_element(By.ID, "use_case").click()
@when(u'Fill all required fields')
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("use case 420")
    context.driver.switch_to.frame(0)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>use case desc&nbsp;</p>'}", element)
    context.driver.switch_to.default_content()
@when(u'click "save" button')
def step_impl(context):
    context.driver.find_element(By.ID, "form-buttons-save").click()
@then(u'to reg_user is shown his Use case page')
def step_impl(context):
    context.driver.get("http://localhost:8080/repo/use-case-420")

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
    create_tool(context)
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
    context.driver.get("http://localhost:8080/repo")
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
@when(u'administrator click on "Add new... Workflow"')
def step_impl(context):
    try:
        context.driver.find_element(By.ID, "workflow").click()
    except:
        raise NotImplementedError(u'workflow cannot create')
@then(u'Workflow edit page is presented')
def step_impl(context):
    pass    



