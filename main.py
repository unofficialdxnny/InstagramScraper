from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options  # Import Options
from time import sleep
import os
import openpyxl


workbook = openpyxl.Workbook()
sheet = workbook.active


os.system('cls')
banner = '''

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡶⠦⢤⠴⠒⠒⠚⠛⠒⢶⠤⠤⠤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡦⠴⣒⠉⠁⠀⠀⠀⠀⠑⠀⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠹⡝⠒⠤⣄⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠊⠁⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⡤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠓⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡾⠛⠓⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⣶⡾⢿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠉⠁⢒⣒⣒⡒⠒⠒⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢹⠃⢠⡄⠙⢿⣿⣷⣤⡀⠀⠀⠀⠀⡴⠊⠁⠀⠀⠈⠑⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠤⠤⣀⣀⠀⠀⠀⠀⠀⠀⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠣⣈⣀⠀⠀⠙⠻⣿⣿⣶⣄⠀⡞⠀⠀⢰⣶⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠤⠤⠤⢍⠉⠒⠀⠀⠀⠀⠈⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠹⡄⠀⠀⠀⠈⠻⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠁⢀⣄⠀⠀⠀⠙⢄⠀⠀⠀⠀⠀⢸⣆⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠹⡄⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⢻⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣯⣶⣶⣾⣷⣶⣤⣤⣤⣈⣆⠀⠀⠀⠀⣼⣟⣤⢳⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⢸⣿⣿⠿⠛⠛⢿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣼⣿⣋⣀⡜⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠳⡄⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣥⣤⣤⣶⣾⣿⣿⠃⠀⠀⠤⠊⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠉⢹⣿⣿⡿⠉⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⣀⣠⢋⠟⠉⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠢⢄⣀⣀⢆⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⣀⣠⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠁⠀⠼⢿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠐⠋⠉⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⣀⣀⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠉⢳⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⣯⣴⣶⣶⣮⠕⠢⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡷⡀⠀⠀⢀⣏⠙⢒⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣙⠿⠿⠿⠿⠟⠛⠁⣰⣿⣿⣿⣿⠿⣟⣧⣤⣶⣾
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⣮⣽⣾⣿⣿⣾⣿⣿⣿⣿⣿⣿⣶⣶⡦⠤⠤⢤⣤⣤⣤⡤⠤⣤⣶⣶⣾⣏⠁⠀⠀⠀⠀⠀⢀⠤⣴⣿⣿⣿⣻⣷⣿⣿⣿⣟⣁⣹
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⡼⠁⠑⢤⠊⠈⢦⣿⣿⣿⣿⣿⣿⣦⣠⣤⣶⢶⠁⢀⠀⡟⠛⢻⠉⠉⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⠃⠀⠀⣤⢣⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡸⡀⣸⣏⠑⡲⠊⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠉⢸⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣷⣤⣭⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⢸⠀⠀⣿⣿⣿⣿⣿⠿⠿⠿⠿⢻⠿⢿⣿⣿⠟⢟⢦⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠿⢸⠀⠀⣿⣿⣿⣿⣿⠀⠀⠀⠀⢺⢤⡼⠿⠿⠦⠬⠆⢣⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⢸⠀⠀⣿⣿⣿⣿⣿⠀⠀⠀⠀⢸⡀⠙⠶⠿⠿⠉⢻⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠛⠉⢹⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀

'''

print(banner)
username = input('username> ')
os.mkdir(username)
# Configure Chrome to run headless
options = Options()
options.headless = True   # Key setting for headless mode

# Create the driver with the headless option
driver = webdriver.Chrome(options=options)  
driver.get(f"https://www.instagram.com/{username}")

sleep(5)
accept_cookies = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
accept_cookies.click()
sleep(2)
posts = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[1]/button').text
followers = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button').text
following = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button').text
print(posts, followers, following)


sheet["A1"] = "username"
sheet["B1"] = username
sheet["A2"] = "Posts"
sheet["B2"] = posts
sheet["A3"] = "Followers"
sheet["B3"] = followers
sheet["A4"] = "Following"
sheet["B4"] = following

workbook.save(f"./{username}/{username}_data.xlsx")



//*[@id="mount_0_0_S1"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/div/div