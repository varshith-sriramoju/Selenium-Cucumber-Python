from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given("opening browser")
def open_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://smartinventoryreact.netlify.app/")


@when('provide valid "{username}" and "{password}"')
def validUserPass(context, username, password):
    context.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/form/button').click()

@then("verify titlle of the page")
def verifyHome(context):
    assert "SmartInventory - Frontend Only" == context.driver.title

@then("verify success message")
def verifySuccess(context):
    try:
        text=context.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div[1]/h2').text
    except:
        context.driver.close()
        assert False, "Test Case failed"
    if text == "SmartInventory - Frontend Only":
        context.driver.close()
        assert True, "Test Case Passed"

@when("verify login using below")
def step_def(context):
    for r in context.table:
        context.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(r["username"])
        context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(r["password"])
        context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/form/button').click()
