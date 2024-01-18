from selenium import webdriver
from selenium.webdriver.chrome.options import Options


PROXY = '84.201.186.26:80'
url = 'http://qa.test/'

options = Options()
options.add_argument(f'--proxy-server={PROXY}')

def main():
    driver = webdriver.Chrome(options=options)
    driver.get(url=url)
    driver.save_screenshot("screenshot.png")
    driver.close()

if __name__ == '__main__':
    main()