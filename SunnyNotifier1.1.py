from msilib.schema import Class, tables
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tabulate import tabulate
from win10toast import ToastNotifier
import datetime

items =[]
data_table = [['LP_token_name', 'APY']]

def table(container):
    for items in container:
        name = items.find_element_by_xpath('.//*[@class="css-1bb389o e1jpzkah1"]')
        apy = items.find_element_by_xpath('.//*[@class="css-sbxpr1 e1sqznmx1"]')
        data_table.append([name.text, apy.text])
    data_table_t = tabulate(data_table, headers='firstrow', tablefmt='fancy_grid')
    return data_table_t

def write_to_file(data_table_t):
    org_stdout = sys.stdout
    with open (r"C:\temp\Sunny.txt", 'w', encoding='utf-8') as f:
        sys.stdout = f
        print("The file was generated at {}".format(datetime.datetime.now()))
        print(data_table_t)
        sys.stdout = org_stdout

def win_toast(headlines, file_path):
    toast = ToastNotifier()
    #toast.show_toast("Updated Sunny LP Token details", r"C:\temp\Sunny.txt")
    toast.show_toast(headlines, file_path)

def scrapper():  
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path= "C:\Temp\chromedriver_win32\chromedriver.exe", options= options)
    driver.get("https://app.sunny.ag/")
    container =  WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH,"//*[@class='css-11wdhah e10iyz7l0']")))
    # Create a table
    dt= table(container)
    # Write table to file
    write_to_file(dt)
    # notify windows
    win_toast("Updated Sunny LP Token details", r"C:\temp\Sunny.txt")
    driver.quit()

if __name__ == "__main__":  
    scrapper()