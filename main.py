from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time
import sys
import socket
import json


class Whatsapp:
	def __init__(self, website_url):
		self.whatsapp_url = website_url
		driver_path = os.getcwd() + "\\chrome_driver\\chromedriver.exe"
		print(socket.gethostname())
		if socket.gethostname() == "My-Personal-PC":
			print("Running Under My Personal PC")
			chrome_directory = r"user-data-dir=C:\Users\Admin\AppData" \
			                   r"\Local\Google\Chrome\User_Data_For_Auto_Trigger_System"
		elif socket.gethostname() == "FS-35825":
			print("Running Under Company Laptop")
			chrome_directory = r"user-data-dir=C:\Users\fs120806\AppData\Local\Google\Chrome" \
			                   r"\User_Data_For_Auto_Trigger_System"
		else:
			print("Running Under Home PC")
			chrome_directory = r"user-data-dir=C:\Users\admin\AppData\Local\Google" \
			                   r"\Chrome\User_Data_For_Auto_Trigger_System"
		# Access to whatsapp
		self.chrome_options = Options()
		self.chrome_options.add_argument(chrome_directory)
		self.chrome_options.add_experimental_option("detach", True)
		# Keep the chrome driver open after the program is finished
		self.service = Service(driver_path)
		self.chrome_driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
		self.wait = WebDriverWait(self.chrome_driver, 100)
		self.chrome_driver.get(self.whatsapp_url)


if __name__ == '__main__':
	website_url = "https://web.whatsapp.com/"
	whatsapp = Whatsapp(website_url)



