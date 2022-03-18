from PIL import Image
import pytesseract
import pyautogui
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

last = 0

time.sleep(2)

while True :
    screenshot = pyautogui.screenshot().crop(( ))
    screenshot.save('screenshot.png')

    text = pytesseract.image_to_string(screenshot, lang='eng')
    print('parse : ', text)
    try:
        next = str(eval(text) + 1)
        print('valid : ', next)

        if next != last + 1 or last == 0 :

            last = next
            for i in next :
                keyboard.press(i)
                keyboard.release(i)

            time.sleep(1)

            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
    except SyntaxError:
        print('not valid')
        
    time.sleep(2)
    
