import time

import yaml

with open('testdata.yaml') as f:
    test_data = yaml.safe_load(f)

#site = Site(test_data['address'])


def test_step_1(selector_1, selector_2, selector_3, button_1,site_1):
    input1 = site_1.find_element('xpath', selector_1)
    input1.send_keys('test')
    input2 = site_1.find_element('xpath', selector_2)
    input2.send_keys('test')
    btn = site_1.find_element('xpath', button_1)
    btn.click()
    error_label = site_1.find_element('xpath', selector_3)
    assert error_label.text == '401'


def test_step_2(selector_1, selector_2, selector_3, button_1, site_1, res_log):
    input1 = site_1.find_element('xpath', selector_1)
    input1.send_keys(test_data['login'])
    input2 = site_1.find_element('xpath', selector_2)
    input2.send_keys(test_data['password'])
    btn = site_1.find_element('xpath', button_1)
    btn.click()
    res_label = site_1.find_element('xpath', res_log)
    assert res_label.text == 'Blog'


def test_step_3(selector_1, selector_2, selector_3, button_1, site_1,
                res_log, button_create_1, description_selector,
                content_selector, button_post, title_selector, title_name, content_name, description_name):
    input1 = site_1.find_element('xpath', selector_1)
    input1.send_keys(test_data['login'])
    input2 = site_1.find_element('xpath', selector_2)
    input2.send_keys(test_data['password'])
    btn = site_1.find_element('xpath', button_1)
    btn.click()
    btn_create_post = site_1.find_element('xpath', button_create_1)
    btn_create_post.click()
    time.sleep(test_data['sleep_time'])
    input_title = site_1.find_element('xpath',title_selector)
    input_title.send_keys(title_name)
    input_description = site_1.find_element('xpath', description_selector)
    input_description.send_keys(content_name)
    input_content = site_1.find_element('xpath', content_selector)
    input_content.send_keys(description_name)
    btn_post_1 = site_1.find_element('xpath', button_post)
    time.sleep(test_data['sleep_time'])
    btn_post_1.click()
    res_label = site_1.find_element('xpath', res_log)
    assert res_label.text == 'Create Post'

# css_selector = 'span.mdc-text-field__ripple'
# print(site.get_element_property('css', css_selector, 'height'))
#
# xpath = '//*[@id="login"]/div[3]/button/div'
# print(site.get_element_property('xpath', xpath, 'color'))
