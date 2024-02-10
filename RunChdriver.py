from selenium import webdriver

# Setting Parameters for chromedriver
chrome_options = webdriver.ChromeOptions()

binary_destination = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
chrome_options.binary_location = binary_destination

chrome_options.add_experimental_option("detach", True)


# Run Webdriver
driver = webdriver.Chrome(options=chrome_options)

# Connect to Desired Webpage on Webdriver           # the table of websites will be added soon.
driver.get('https://news.naver.com/')