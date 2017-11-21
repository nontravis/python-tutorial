import pyautogui

#┌─────────────────────────┐
#│ NOTE: Mouse controlling │
#└─────────────────────────┘
# NOTE: move cursor to 0,0 to cancel event
# X-coordinates: right
# Y-coordinates: down
width, height = pyautogui.size()

pyautogui.position()        # current mouse position
pyautogui.moveTo(100, 100, duration=0.5)
pyautogui.moveRel(200, 0, duration=1.0)
pyautogui.moveRel(0, -100, duration=1.0)

pyautogui.click()           # click on current position
pyautogui.click(777, 388)
pyautogui.doubleClick(777, 388)
pyautogui.rightClick(777, 388)
pyautogui.middleClick(777, 388)
pyautogui.dragTo(200, 0)
pyautogui.dragRel(200, 0)

pyautogui.displayMousePosition()    # show real-time current position and RGB


#┌────────────────────────────┐
#│ NOTE: Keyboard controlling │
#└────────────────────────────┘
pyautogui.click()
pyautogui.typewrite("Hello world!")
pyautogui.typewrite("Hello world!", interval=0.2)
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=1.0)  # left: move cursor left
pyautogui.KEYBOARD_KEYS

pyautogui.press("f1")      # for one key
pyautogui.hotkey("ctrl", 'o')


#┌───────────────────┐
#│ NOTE: Screenshots │
#└───────────────────┘
pyautogui.screenshot("/Users/thekhaeng/Pictures/Screen shot/test.png")

# search by picture on screen
location = pyautogui.locateOnScreen("/Users/thekhaeng/Pictures/Screen shot/calc7key.png")
location = pyautogui.locateOnScreen("/Users/thekhaeng/Pictures/Screen shot/locateOnScreen3.png")
location = pyautogui.locateCenterOnScreen(
    "/Users/thekhaeng/Pictures/Screen shot/locateOnScreen3.png")
pyautogui.moveTo(location, duration=1)
