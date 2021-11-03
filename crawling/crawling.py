from selenium import webdriver
import time
import os 
from urllib.request import urlretrieve

    
driver = webdriver.Chrome(r'C:\Users\shiminsu\Desktop\실습\likelion\tuguru\crawling\chromedriver.exe')

img_folder = './img'
if not os.path.isdir(img_folder): # 폴더 없으면 새로 생성하는 조건문 
    os.mkdir(img_folder)

page = list(range(1,5))

for page_num in page:
    url = f'https://companiesmarketcap.com/page/{page_num}'
    driver.get(url)
    time.sleep(5)
    brand_image = driver.find_elements_by_css_selector('img.company-logo')
    img_url = []
    for image in brand_image :
        url = image.get_attribute('src')
        img_url.append(url)

print(img_url)


    
# for index, link in enumerate(img_url) :
#     start = link.rfind('64/')
#     end = link.rfind('.')
# # #     filetype = link[start:end]
# #     urlretrieve(link, f'./img/{index}.jpg')

# https://companiesmarketcap.com/img/company-logos/64/AAPL.png

driver.quit()
