#┌────────────────────┐
#│ NOTE: Open website │
#└────────────────────┘
import webbrowser
webbrowser.open("https://www.google.co.th/maps/")


#┌─────────────────────┐
#│ NOTE: Download file │
#└─────────────────────┘
import requests
response = requests.get("https://automatetheboringstuff.com/files/rj.txt")
response.status_code
len(response.text)
response.text[:500]
# if success not show anything
# else error example will raise HTTPError: 404 Client Error: Not Found
response.raise_for_status()

# NOTE: save file
# wb: write binary mode:
# to write binary data from website instend of text data in order to maintain Unicode encoding
play_file = open("RomeoAndJuliet.txt", "wb")
for chunk in response.iter_content(100000):  # can pass how many bytes each iterator
    play_file.write(chunk)
play_file.close()


#┌────────────────────┐
#│ NOTE: Web scraping │
#└────────────────────┘
import bs4
import requests
response = requests.get(
    "https://www.amazon.com/Automate-Boring-Stuff-Python-Programming-ebook/dp/B00WJ049VU")
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, "html.parser")
# inspect mode > copy selector
elements = soup.select(
    "#mediaNoAccordion > div.a-row > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price")
elements[0].text.strip()


#┌────────────────┐
#│ NOTE: Selenium │
#└────────────────┘
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://automatetheboringstuff.com/")
element = browser.find_element_by_css_selector(
    "body > div.main > div:nth-child(1) > ul:nth-child(18) > li:nth-child(1) > a")
element.click()
elements = browser.find_elements_by_css_selector('p')

search_element = browser.find_element_by_css_selector(".search-field")
search_element.send_keys("TheKhaeng")
search_element.submit()

text_element = browser.find_element_by_css_selector(
    "body > div.main > div:nth-child(1) > p:nth-child(6)")
text_element.text

# all entire html page
text_element = browser.find_element_by_css_selector("html")
text_element.text

browser.back()
browser.forward()
browser.refresh()
browser.quit()      # close browser
