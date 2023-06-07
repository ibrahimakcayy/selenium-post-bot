#import all libraries
from selenium.webdriver import ActionChains
from selenium import webdriver as web
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


#useless
def cont():
    
    return "ibrahim-facebook.py"


#get driver from main page
def drivers(driv):
    
    global driver
    driver=driv


#open url and max window
def openurl(url):
    
    driver.get(url)
    driver.maximize_window()
    time.sleep(1.5)

    print("Webpage opened")


#login webpage
def login(usrn,passw):
    
    #write username
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input').send_keys(usrn)
    time.sleep(0.3)
    
    #write password 
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input').send_keys(passw)
    time.sleep(0.3)
    
    #click login button
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
    time.sleep(1)

    print("Logged in")


#share post (with pic or without)
def share_post(text,photo_url="None"):

    print("Start Sharing")
    
    #share post button click
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]').click()
    time.sleep(20)

    #if you choose photo+text mode active this section
    if photo_url!="None":

        #open drop img section
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div[1]/div').click()
        time.sleep(1)

        #upload img
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/input').send_keys(photo_url)
        time.sleep(2)

    #write text
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]').send_keys(text)
    time.sleep(1)
    
    #click share button
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div').click()
    
    print("Post Shared")
