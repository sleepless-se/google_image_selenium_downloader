
# coding: utf-8

# In[1]:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests


# In[2]:

def read_img_page_url():
    elems = driver.find_elements_by_class_name("rg_l")
    img_page_urls =[]
    for i in range(len(elems)):
        elm = elems[i]
        item_page_url = elm.get_attribute("href")
#         print(item_page_url)
        img_page_urls.append(item_page_url)
    return img_page_urls



# In[3]:

def show_all_img():
    import time
    for i in range(5):
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
    driver.find_element_by_id("smb").click()
    for i in range(5):
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)


# In[18]:

# image xpaths
list =["//img[@class='irc_mi']","//*[@id='irc_cc']/div[2]/div[1]/div[2]/div[3]/a/img"]

def read(list):
    for i in range(len(list)):
        elms = driver.find_elements_by_xpath(list[i])
        if len(elms) > 0:
            return elms[0]


# In[13]:




# In[4]:


def download(url):
    file_name = url.split("/")[-1]
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        with open(file_name, 'wb') as file:
            for chunk in res.iter_content(chunk_size=1024):
                file.write(chunk)
                


# In[5]:

if __name__ == '__main__':
    driver = webdriver.Firefox()
    keyword = "猫"
    driver.get("https://www.google.co.jp/search?q="+keyword+"&source=lnms&tbm=isch")
#     show_all_img()
    urls = read_img_page_url()
    

    


# In[19]:

for i in range(len(urls)):
    print (urls[i])
    driver.get(urls[i])
    try:
        elm = read(list)
        img_url = elm.get_attribute("src")
        download(img_url)
        time.sleep(3)
    except ValueError:
        print("//img[@class='irc_mi'] didn't find.")


# In[ ]:


driver.close()


# In[ ]:



