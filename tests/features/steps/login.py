from behave import step

from environment import get_from_config
from pages import LoginPage


@step('User enters credentials')
def step_impl(context):
    page = LoginPage(context)
    page.enter_username(get_from_config('username'))
    page.enter_password(get_from_config('password'))


@step('User clicks Login button')
def step_impl(context):
    page = LoginPage(context)
    page.click_login_button()


@step(u'User lands on Account Home Page')
def step_impl(context):
    assert "inventory" in context.browser.current_url


@step(u'User lands on Account Home Page incorrect validation')
def step_impl(context):
    assert "nothing" in context.browser.current_url


@step('Login page is opened')
def step_impl(context):
    assert 'logowanie' in context.browser.current_url





