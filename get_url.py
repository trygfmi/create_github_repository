# python $(find . -type f -maxdepth 1 -name "get_url.py") "hello world"


import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
sys.path.append(os.path.expanduser("~")+'/Desktop/programming/own_command_list/running-terminal-commands/share/python')
from dotenv import load_dotenv
load_dotenv()
from feature.use_selenium_feature import *
from feature.read_env import *
import pyperclip


set_sleep_time = 3
set_send_keys_sleep_time = 1
repository_name = sys.argv[1]
driver = getDriver()
repository_url="https://github.com/trygfmi/"+repository_name
driver.get(repository_url)
title = driver.title


# urlをクリップボードにコピー
search_input_url_string = '//input[@id="empty-setup-clone-url"]'
element_number = 1
git_url_element = get_element(driver, search_input_url_string)
git_url = git_url_element.get_attribute('value')
print("git remote add origin "+git_url)
pyperclip.copy("git remote add origin "+git_url)
time.sleep(set_send_keys_sleep_time)


driver.quit()


