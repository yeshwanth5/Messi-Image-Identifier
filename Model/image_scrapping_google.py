from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64
import requests

folder = "Images/0_Others"
player = "JohnCena"
driver = webdriver.Chrome()
driver.get('https://www.google.com/imghp')
search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys(f'{player} face' + Keys.RETURN)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'title')))
for i in range(1,15):
    image_url = ""
    try:
        image_url = driver.find_element(By.XPATH,f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div/img').get_attribute('src')
        image = base64.b64decode(image_url.split(',')[1])
        with open(f'{folder}/{player}{i}.jpg', 'wb') as file:
            file.write(image)
            file.close()
        print(f'{i} saved.')
    except Exception:
        if image_url is not None and 'http' in image_url:
            response =  requests.get(image_url)
            with open(f'{folder}/{player}{i}.jpg', 'wb') as file:
                file.write(response.content)
                file.close()
            print(f'{i} saved.')
        pass
driver.quit()
