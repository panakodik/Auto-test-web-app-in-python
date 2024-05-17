import pytest
from module import Site, test_data
import yaml

@pytest.fixture()
def selector_1():
    return """//*[@id="login"]/div[1]/label/input"""

@pytest.fixture()
def button_1():
    return '//*[@id="login"]/div[3]/button'

@pytest.fixture()
def button_create_1():
    return '//*[@id="app"]/main/div/div[2]/div[1]/button'

@pytest.fixture()
def button_post():
    return '//*[@id="create-item"]/div/div/div[7]/div/button'

@pytest.fixture()
def selector_2():
    return '''//*[@id="login"]/div[2]/label/input'''

@pytest.fixture()
def selector_3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""
@pytest.fixture()
def title_selector():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""
@pytest.fixture()
def description_selector():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""
@pytest.fixture()
def content_selector():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture()
def title_name():
    return 'Black'
@pytest.fixture()
def description_name():
    return 'dog'
@pytest.fixture()
def content_name():
    return 'Bubble!'
@pytest.fixture()
def res_log():
    return """//*[@id="app"]/main/div/div[1]/h1"""

@pytest.fixture()
def res_post():
    return """//*[@id="app"]/main/div/div[1]/h1"""

@pytest.fixture()
def site_1():
    my_site = Site(test_data['address'])
    yield my_site
    my_site.close()
