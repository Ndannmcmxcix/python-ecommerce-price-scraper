thonpython
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

class SeleniumHandler:
 def __init__(self):
 self.logger = logging.getLogger("SeleniumHandler")
 options = Options()
 options.add_argument("--headless")
 self.driver = webdriver.Chrome(options=options)

 def load_page(self, url: str) -> str:
 self.logger.info(f"Rendering page via Selenium: {url}")
 self.driver.get(url)
 return self.driver.page_source

 def close(self):
 self.driver.quit()