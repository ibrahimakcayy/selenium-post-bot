#import all libraries
from selenium.webdriver import ActionChains
from selenium import webdriver as web
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


#useless
def cont():
    return "ibrahim-instagram.py"


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


#login instagram
def login(usern,passw):
    time.sleep(1)
    
    #write username
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys(usern)
    
    #write password
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys(passw)
    time.sleep(1)

    #click login button
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
    time.sleep(10)

    print("Logged in")
    
    driver.get("https://www.instagram.com")
    time.sleep(8)
    
    #click notification decline
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
    time.sleep(2)


#share photo in instagram 
def share_photo(text,photo_url,usern):
    
    print("Start Sharing")

    #open share popup
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div').click()
    time.sleep(3)
    
    #upload photo
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/form/input').send_keys(photo_url)
    time.sleep(5)
    
    #share actions
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div').click()
    time.sleep(3)
    
    #write caption
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]').send_keys(text)
    time.sleep(0.5)
    
    #share photo
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div').click()
    time.sleep(15)

    print("Post Shared")

    #open profile
    driver.get(f"https://www.instagram.com/{usern}/")
