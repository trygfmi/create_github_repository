# python $(find . -type f -maxdepth 1 -name "main.py") "hello world"


import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
sys.path.append(os.path.expanduser("~")+'/Desktop/programming/own_command_list/running-terminal-commands/share/python')
from dotenv import load_dotenv
load_dotenv()
from feature.use_selenium_feature import *
from feature.read_env import *


start_time=time.time()

set_sleep_time = 3
set_send_keys_sleep_time = 2
repository_name = sys.argv[1]
driver = getDriver()
driver.get(access_url)
title = driver.title
print(title)

for_login(driver)

search_new_button_string = '//a[@class="text-center btn btn-primary ml-2"]'
element_number = 1
press_something_block_xpath(driver, search_new_button_string, element_number)

time.sleep(set_sleep_time)
search_input_repository_name_string = '//input[@id="repository-name-input"]'
repository_name_element = get_element(driver, search_input_repository_name_string)
repository_name_element.send_keys(repository_name)
time.sleep(set_send_keys_sleep_time)

search_create_button_string = '//button[@class="prc-Button-ButtonBase-c50BI mt-4"]'
element_number = 1
press_something_block_xpath(driver, search_create_button_string, element_number)
time.sleep(set_sleep_time)

# リポジトリのトップページでメニューボタンを押す
search_menu_button_string = '//button[@class="Button Button--iconOnly Button--secondary Button--medium UnderlineNav-item"]'
menu_button_element = get_element(driver, search_menu_button_string)
menu_button_element.click()
time.sleep(set_send_keys_sleep_time)

# ボタンを押した後に開くドロップダウンからSettingsをクリック
search_settings_string = '//a[@class="ActionListContent ActionListContent--visual16"]'
element_number = 1
press_something_block_xpath(driver, search_settings_string, element_number)
time.sleep(set_sleep_time)

# 画面左の項目からRulesetsをクリック
search_rulesets_section_string = '//a[@class="ActionListContent"]'
element_number = 8
press_something_block_xpath(driver, search_rulesets_section_string, element_number)
time.sleep(set_sleep_time)

# New rulesetsボタンをクリック
search_new_ruleset_button_string = '//button[@class="prc-Button-ButtonBase-c50BI"]'
new_rule_sets_button_element = get_element(driver, search_new_ruleset_button_string)
new_rule_sets_button_element.click()
time.sleep(set_send_keys_sleep_time)

# New branch rulesetsセクションをクリック
search_new_branch_ruleset_string = '//a[@class="prc-ActionList-ActionListContent-sg9-x prc-Link-Link-85e08"]'
element_number = 5
press_something_block_xpath(driver, search_new_branch_ruleset_string, element_number)
time.sleep(set_sleep_time)

# Rulesetsの名前を入力
rule_sets_name = "block force pushes"
search_rule_sets_name_string = '//input[@data-component="input"]'
element_number = 1
rule_sets_name_element = get_element(driver, search_rule_sets_name_string)
rule_sets_name_element.send_keys(rule_sets_name)
time.sleep(set_send_keys_sleep_time)

# Enforcement statusボタンをクリック
search_enforcement_status_string = '//button[@aria-label="Disabled, Enforcement status"]'
element_number = 1
press_something_block_xpath(driver, search_enforcement_status_string, element_number)

# Enforcement statusのactiveをクリック
search_enforcement_active_string = '//div[@class="prc-ActionList-ActionListContent-sg9-x"]'
element_number = 2
press_something_block_xpath(driver, search_enforcement_active_string, element_number)

# Add targetボタンをクリック
search_add_target_string = '//button[@class="prc-Button-ButtonBase-c50BI"]'
element_number = 2
press_something_block_xpath(driver, search_add_target_string, element_number)

# Include all branchesセクションをクリック
search_include_all_branches_string = '//div[@class="prc-ActionList-ActionListContent-sg9-x"]'
element_number = 3
press_something_block_xpath(driver, search_include_all_branches_string, element_number)

# Createボタンをクリック
search_create_button_string = '//button[@class="prc-Button-ButtonBase-c50BI"]'
element_number = 1
press_something_block_xpath(driver, search_create_button_string, element_number)
input("認証する必要があれば認証してください")


end_time=time.time()
print("かかった時間:"+str(end_time-start_time))


driver.quit()


