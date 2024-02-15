#pip3 install selenium
#pip3 install webdrivermanager or #pip3 install webdriver_manager
from selenium import webdriver
import time
timeout_seconds = 10
element_name='//*[@id="app"]/div/main/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/button[1]'
path='/home/navid/Desktop/links'
file = open(path , 'r')
links = file.readlines()
links_array=[]
for link in links:
    links_array.append(link)
number_all= len(links_array)
while len(links_array) != 0:
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(timeout_seconds)
        try:
            print(f'processing {links_array[0]}')
            driver.get(links_array[0])
    
        except:
            pass
        element=driver.find_element("xpath",element_name)
        element.click()
        time.sleep(2)
        driver.quit()
        links_array.pop(0)
        print(f'{number_all-len(links_array)} of {number_all} in done.')
    except:
        pass




