import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

def main():
    times = ["0830", "1200", "1300", "1630"]
    driver = webdriver.Chrome("chromedriver.exe")
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver.get("http://mysu.susqu.edu")
    keep_looking = True
    while keep_looking == True:
        if driver.find_element_by_xpath('//*[@id="ctl00_SPWebPartManager1_g_c6aa6a6e_e9b7_4df5_8834_1d0343b80f1f"]/div/div[4]/div[1]/ul/li[2]/div/a/h5'):
            employee = driver.find_element_by_xpath('//*[@id="ctl00_SPWebPartManager1_g_c6aa6a6e_e9b7_4df5_8834_1d0343b80f1f"]/div/div[4]/div[1]/ul/li[2]/div/a/h5')
            keep_looking = False
    employee.click()
    sleep(0.75)
    time_entry_history = driver.find_element_by_xpath('//*[@id="ctl00_SPWebPartManager1_g_c6aa6a6e_e9b7_4df5_8834_1d0343b80f1f"]/div/div[4]/div[1]/ul/li[2]/ul/li[3]/a/span')
    time_entry_history.click()
    sleep(0.3)
    time_entry = driver.find_element_by_xpath('//*[@id="ctl00_SPWebPartManager1_g_c6aa6a6e_e9b7_4df5_8834_1d0343b80f1f"]/div/div[4]/div[2]/ul/li[1]/a/span')
    time_entry.click()
    sleep(1.2)
    pay_period = driver.find_element_by_xpath('//*[@id="LIST_VAR1_1"]')
    pay_period.click()
    submit = driver.find_element_by_xpath('//*[@id="WASubmit"]')
    submit.click()
    sleep(1)
    for i in range(1, 28, 2):
        if i != 11 and i != 13 and i != 25 and i != 27:
            xpath0 = '//*[@id="LIST_VAR4_' + str(i) + '"]'
            driver.find_element_by_xpath(xpath0).send_keys(times[0])
            xpath1 = '//*[@id="LIST_VAR5_' + str(i) + '"]'
            driver.find_element_by_xpath(xpath1).send_keys(times[1])
            xpath2 = '//*[@id="LIST_VAR4_' + str(i+1) + '"]'
            driver.find_element_by_xpath(xpath2).send_keys(times[2])
            xpath3 = '//*[@id="LIST_VAR5_' + str(i+1) + '"]'
            driver.find_element_by_xpath(xpath3).send_keys(times[3])
        else:
            continue

    quit()
main()
