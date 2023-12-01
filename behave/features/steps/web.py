"""
This module contains step definitions for web.feature.
It uses Selenium WebDriver for browser interactions:
https://www.seleniumhq.org/projects/webdriver/
Setup and cleanup are handled in environment.py
For a real test automation project,
use Page Object Model or Screenplay Pattern to model web interactions.
"""

from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



# "Constants"

DUCKDUCKGO_HOME = 'https://duckduckgo.com/'


# Givens

@given('the DuckDuckGo home page is displayed')
def step_impl(context):
    context.browser.get(DUCKDUCKGO_HOME)


# Whens

@when('the user searches for "{phrase}"')
def step_impl(context, phrase):
    #search_input = context.browser.find_element_by_id('search_form_input_homepage')
    search_input = context.browser.find_element(By.ID, 'searchbox_input')
    search_input.send_keys(phrase + Keys.RETURN)


@when('the user searches for the phrase')
def step_impl(context):
    search_input = context.browser.find_element(By.ID, 'searchbox_input')
    search_input.send_keys(context.text + Keys.RETURN)


# Thens

@then('one of the results contains "{phrase}"')
def step_impl(context, phrase):
    xpath = "//div[@id='links']//*[contains(text(), '%s')]" % phrase
    xpath = "//*[@id='web_content_wrapper']//*[contains(text(), '%s')]" % phrase
    results = context.browser.find_elements(By.XPATH, xpath)
    assert len(results) > 0


@then('results are shown for "{phrase}"')
def step_impl(context, phrase):
    # Check search result list
    # (A more comprehensive test would check results for matching phrases)
    # (Check the list before the search phrase for correct implicit waiting)
    links_div = context.browser.find_element(By.ID, 'web_content_wrapper')
    assert len(links_div.find_elements(By.XPATH, '//li')) > 0
    # Check search phrase
    search_input = context.browser.find_element(By.ID, 'search_form_input')
    assert search_input.get_attribute('value') == phrase
