import time
import logging
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

class WebscrapOnlineResearch():
    def __init__(self):
        """
        Initialize the WebscrapOnlineResearch class.
        :param url: the URL of the online research paper
        """
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)

    def get_page_source_as_string(self, url):
        """
        Get the page source of the online research paper.
        :param url: the URL of the online research paper
        :return: the page source as a string
        """
        try:
            self.driver.get(url)
            time.sleep(3)
            html = self.driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            formatted_html = soup.prettify()
            online_data_pool = ""
            for string in soup.stripped_strings:
                online_data_pool = online_data_pool + ' ' + string
                
            logging.info(online_data_pool)
            return online_data_pool

        except Exception as e:
            logging.error(f"Error: {e}")
        finally:
            self.driver.quit()
