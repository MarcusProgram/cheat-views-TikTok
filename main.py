from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
from colorama import Fore, init
import sys
import random
import ctypes
from selenium.common.exceptions import NoSuchElementException
from fake_useragent import UserAgent
from PIL import Image


print(f"{Fore.RED} Данная программа была написанна программистом MARCUS {Fore.RESET}{'\n'*10}")
sleep(2)



#███╗░░░███╗░█████╗░██████╗░░█████╗░██╗░░░██╗░██████╗
#████╗░████║██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔════╝
#██╔████╔██║███████║██████╔╝██║░░╚═╝██║░░░██║╚█████╗░
#██║╚██╔╝██║██╔══██║██╔══██╗██║░░██╗██║░░░██║░╚═══██╗
#██║░╚═╝░██║██║░░██║██║░░██║╚█████╔╝╚██████╔╝██████╔╝
#╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═════╝░











sys.setrecursionlimit(2147483647)
init()

ua = UserAgent()
user_agent = ua.random

options = webdriver.ChromeOptions()

for messages_eror in [0,1,2,3,4]:
    options.add_argument(f"log-level={messages_eror}")
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)


elements = ['', '', 'Followers', 'Hearts', 'Comments Hearts', 'Views', 'Shares', 'Favorites']
buttons = {
    1: '/html/body/div[6]/div/div[2]/div/div/div[2]/div/button',
    2: '/html/body/div[6]/div/div[2]/div/div/div[3]/div/button',
    3: '/html/body/div[6]/div/div[2]/div/div/div[4]/div/button',
    4: '/html/body/div[6]/div/div[2]/div/div/div[5]/div/button',
    5: '/html/body/div[6]/div/div[2]/div/div/div[6]/div/button',
    6: '/html/body/div[6]/div/div[2]/div/div/div[7]/div/button'
}
buttons2 = {
    2:8,
    4:10,
    5:11,
    6:12
}
buttons3 = {
    1: 'followers-countdown',
    2: 'hearts-countdown',
    3: 'c-hearts-countdown',
    4: 'views-countdown',
    5: 'shares-countdown',
    6: 'favorites-countdown'
}
buttons4 = {
    2:"Hearts",
    4:"Views",
    5:'Shares',
    6:'Favorites'
}
buttons5 = {
    2:"лайков",
    4:"просмотров",
    5:'пересылов',
    6:'избранных'
}
views = shares = favorites = hearts = 0
disButton = []





clear = lambda: os.system('cls')


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def connectCaptcha(captcha):
    xpath_input = '/html/body/div[5]/div[2]/form/div/div/div/input'
    xpath_button = '/html/body/div[5]/div[2]/form/div/div/div/div/button'
    input_element = driver.find_element(By.XPATH, xpath_input)
    input_element.clear()
    input_element.send_keys(captcha)
    driver.find_element(By.XPATH, xpath_button).click()

def printElement():
    print('\n\n')
    for i in range(2, 8):
        button = driver.find_element(By.XPATH, f'/html/body/div[6]/div/div[2]/div/div/div[{i}]/div/button')
        if button.get_attribute('disabled'):
            disButton.append(i-1)
        else:
            print(f'{Fore.GREEN}[{i-1}]{Fore.RESET} {Fore.RED + elements[i] + Fore.RESET}')
    print('\n')

def Favorites(nameAccount):
    print("!Автор ниразу туда не заходил, так что не знает как работает!")
def commentHearsAll(urlVideo,nameAccount):
    print("Автор скоро это сделает")
    #urlVideo = checkLink(urlVideo, 'https://')
    #nameAccount = checkLink(nameAccount,'@')
    #if len(urlVideo) != 0:
    #    driver.find_element(By.XPATH, f'/html/body/div[9]/div/form/div/input').clear()
    #    driver.find_element(By.XPATH, f'/html/body/div[9]/div/form/div/input').send_keys(urlVideo)
    #    driver.find_element(By.XPATH, f'/html/body/div[9]/div/form/div/div/button').click()
    #    sleep(10)
    #    driver.find_element(By.XPATH, f'/html/body/div[9]/div/div/div[1]/div/form/button').click()
    #    #/html/body/div[9]/div/div/form/ul/li/div/button
    #    sleep(3)
    #else:
    #    print("Вы ввели пустую строку:(")
    #    exit()

def rangeValue(urlVideo,choiseButton):
    try:
        old_text = driver.find_element(By.XPATH,f"/html/body/div[{buttons2[choiseButton]}]/div/div/div[1]/div/form/button").text
        old_text = old_text.replace(',', '')
        print(f'{Fore.GREEN}Total{Fore.RESET} {Fore.RED+old_text+Fore.RESET} {Fore.GREEN + buttons5[choiseButton] + Fore.RESET}')
        sleep(2)
        driver.find_element(By.XPATH,
                            f'/html/body/div[{buttons2[choiseButton]}]/div/div/div[1]/div/form/button').click()
        sleep(4)
    except NoSuchElementException:
        check_timer_for_hvsf(urlVideo, choiseButton)


def h_v_s_f_All(urlVideo,choiseButton):
    global views, shares, favorites
    urlVideo = checkLink(urlVideo, 'https://')
    driver.find_element(By.XPATH, f'/html/body/div[{buttons2[choiseButton]}]/div/form/div/input').clear()
    if len(urlVideo) != 0:
        driver.find_element(By.XPATH, f'/html/body/div[{buttons2[choiseButton]}]/div/form/div/input').send_keys(urlVideo)
        sleep(7)
        driver.find_element(By.XPATH, f'/html/body/div[{buttons2[choiseButton]}]/div/form/div/div/button').click()
        sleep(7)
        rangeValue(urlVideo, choiseButton)
        sleep(10)
        check_timer_for_hvsf(urlVideo,choiseButton)
    else:
        print("Вы ввели пустую строку:(")
def check_timer_for_hvsf(urlVideo, choiseButton):
    isReady = driver.find_element(By.CLASS_NAME, buttons3[choiseButton])
    if isReady.text != 'Next Submit: READY....!':
        sleep(2)
        check_timer_for_hvsf(urlVideo, choiseButton)
    else:
        h_v_s_f_All(urlVideo, choiseButton)
def checkLink(text,startwith):
    if not text.startswith(startwith):
        text = startwith + text
    return text

def ipConnect():
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return ip

def changeImage(nameImage):
    driver.save_screenshot(f"captcha/{nameImage}")
    image = Image.open(f"captcha/{nameImage}")
    screen_height = driver.execute_script("return window.innerHeight")
    cropped_image = image.crop((0, 0, image.width - 100, screen_height - 300))
    cropped_image.save(f"captcha/{nameImage}")
def main():

    print(Fore.GREEN + "Дождитесь пока откроется страница." + Fore.RESET, '\n\n')
    driver.get('https://zefoy.com/')

    print(Fore.RED + "При не правильной капче программа выведет ошибку" + Fore.RESET)
    changeImage('captcha.png')
    captcha = input(Fore.GREEN + "Введите код с капчи: " + Fore.RESET).lower()


    connectCaptcha(captcha)
    printElement()
    try:
        choiseButton = int(input("Выбери: "))
        if choiseButton in disButton:
            print("Эта кнопка отключена :(")
        else:
            driver.find_element(By.XPATH, buttons[choiseButton]).click()
            if choiseButton in [2, 4, 5, 6]:
                urlVideo = input("Введите url видео: ")
                clear()
                h_v_s_f_All(urlVideo,choiseButton)

            elif choiseButton == 3:
                urlVideo = input("Введите url видео: ")
                accountName = input("Введите account name: ")
                clear()
                commentHearsAll(urlVideo,accountName)
            else:
                print(Fore.RED + "Такой кнопки нет :(")
    except Exception as ex:
        print(ex)
        print(10*'\n')
        print("(Возможно вы не правильно ввели капчу)", 3*'\n')

if __name__ == '__main__':
    if is_admin():
        if not os.path.exists("captcha"):
            os.makedirs("captcha")
            captcha_image = Image.new('RGB', (200, 100), color='white')
            # Сохраняем изображение в файл
            captcha_file_path = os.path.join("captcha", "captcha.png")
            captcha_image.save(captcha_file_path)
        clear()
        print(f'{Fore.GREEN}User Agent: {Fore.RED + user_agent + Fore.RESET}')
        print(f'{Fore.GREEN}IP: {Fore.RED + ipConnect() + Fore.RED}\n\n')
        main()
    else:
        print(Fore.RED + "Пожалуйста откройте программу с правами администратора!")
        exit()

#@marksale18
#https://vt.tiktok.com/ZSNDKBBPa/
