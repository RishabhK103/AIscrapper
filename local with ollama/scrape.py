import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def scrape_web(website):

    chrome_driver_path="/usr/bin/chromedriver"
    options=webdriver.ChromeOptions()
    options.add_argument("--headless") 
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver=webdriver.Chrome(service=Service(chrome_driver_path),options=options)

    try:
        driver.get(website)
        print("page loaded")
        html=driver.page_source

        return html

    finally:
        driver.quit()


def extract_body(html_content):
    soup=BeautifulSoup(html_content,"html.parser")
    body_content=soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup=BeautifulSoup(body_content,"html.parser")

    for script_or_style in soup(["script","style"]):
        script_or_style.extract()

    cleaned_content=soup.getText(separator="\n")
    cleaned_content="\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    
    return cleaned_content


def split_dom_content(dom_content,max_len=3000):
    return [dom_content[i:i + max_len] for i in range(0,len(dom_content),max_len)]

