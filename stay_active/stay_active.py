import pyautogui, time, random

first = True
while True:
    if first:
        time.sleep(10)
        first = False
    else:
        time.sleep(random.randint(3, 15))
    pyautogui.press("f13")
