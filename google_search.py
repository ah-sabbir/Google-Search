from selenium import webdriver
from itertools import cycle
from time import sleep
from bs4 import BeautifulSoup as bs
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as action
import pandas as pd
import time
import random
from requests import get



path=r'chromedriver\chromedriver.exe'


options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
driver = webdriver.Chrome(executable_path = path,options=options)

company_name = []
website = []
address = []
phone = []
catagory = []

def get_phone(driver):
    for a in driver.find_elements_by_tag_name("a"):
        if "phone" in a or "Phone" in a:
            break
        #todo something here


def get_google_data():
    while True:
        sleep(4)
        companies = driver.find_elements_by_css_selector("div.cXedhc.uQ4NLd")
        if len(companies)<1:
            companies = driver.find_elements_by_css_selector("div.cXedhc")
        for com in companies:
            com.click()
            sleep(3)
            try:
                company_name.append(driver.find_element_by_css_selector("h2.qrShPb.kno-ecr-pt.PZPZlf.mfMhoc.PPT5v").text)
            except:
                company_name.append("N/A")
            try:
                website.append(driver.find_element_by_css_selector("a.CL9Uqc.ab_button").get_attribute("href"))
            except:
                website.append("N/A")
            try:
                address.append(driver.find_element_by_css_selector("span.LrzXr").text)
            except:
                address.append("N/A")
            try:
                catagory.append(driver.find_element_by_css_selector("span.YhemCb").text)
            except:
                catagory.append("N/A")
            try:
                phone.append(driver.find_element_by_css_selector("span.LrzXr.zdqRlf.kno-fv").text)
            except:
                phone.append("N/A")

        d_list={"company_name":company_name,"website":website,"address":address,"catagory":catagory,"phone":phone}
        writer = pd.ExcelWriter('google search result.xlsx', engine='xlsxwriter')
        dataframe= pd.DataFrame(d_list)
        ##    print(dataframe)
        dataframe.to_excel(writer)
        writer.save()
        try:
            driver.find_element_by_css_selector("a#pnnext").click()
        except Exception as e:
            print(e)
            break



