import time
import logging
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

class WebscrapOnlineResearch():
    def __init__(self):
        """
        Initialize the WebscrapOnlineResearch class.
        :param url: the URL of the online research paper
        """
        # self.url = url
        # # self.driver = None
        # self.html = None
        # self.soup = None
        # self.online_data_pool = None
        options = Options()
        # options.add_argument("--headless")  # Run in headless mode
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
                # logging.info(repr(string))
                # import pdb;pdb.set_trace()
                online_data_pool = online_data_pool + ' ' + string
                
            logging.info(online_data_pool)
            return online_data_pool

        except Exception as e:
            logging.error(f"Error: {e}")
        finally:
            self.driver.quit()

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)

# url = "https://conbio.onlinelibrary.wiley.com/doi/10.1111/csp2.13096"
# driver.get(url)

# Wait and get the page source
# import time
# time.sleep(10)  # Adjust as needed
# try:
#     html = driver.page_source
#     soup = BeautifulSoup(html, "html.parser")
#     formatted_html = soup.prettify()
#     # logging.info(formatted_html.stripped_strings)  # Check if content is returned
#     online_data_pool = ""
#     for string in soup.stripped_strings:
#         # logging.info(repr(string))
#         online_data_pool = online_data_pool + string
        
#     logging.info(online_data_pool)
# finally:
#     driver.quit()

# # Save to a text file
# with open("dump.txt", "w", encoding="utf-8") as file:
#     file.write(online_data_pool)

# # Extracting all H1 and H2 tags
# h1_tags = [h1.get_text(strip=True) for h1 in soup.find_all("h1")]
# h2_tags = [h2.get_text(strip=True) for h2 in soup.find_all("h2")]

# # Extracting all paragraphs
# paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]

# # Extracting all links (anchor tags with href)
# links = [a['href'] for a in soup.find_all("a", href=True)]

# # Extracting button text (ignoring disabled buttons)
# buttons = [btn.get_text(strip=True) for btn in soup.find_all("button") if "disabled" not in btn.attrs]

# # Extracting all other visible text (excluding scripts, styles, etc.)
# all_text = soup.get_text(separator="\n", strip=True)

# # # Storing extracted data
# # extracted_data = f"""
# # H1 Tags:\n{'\n'.join(h1_tags)}

# # H2 Tags:\n{'\n'.join(h2_tags)}

# # Paragraphs:\n{'\n'.join(paragraphs)}

# # Links:\n{'\n'.join(links)}

# # Buttons:\n{'\n'.join(buttons)}

# # All Other Visible Text:\n{all_text}
# # """

# # logging.info results
# logging.info(extracted_data)


# # Save to a text file
# with open("dump.txt", "w", encoding="utf-8") as file:
#     file.write(formatted_html)

# logging.info("Formatted HTML saved to output.txt")
