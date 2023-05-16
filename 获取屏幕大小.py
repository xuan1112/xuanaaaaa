import pyautogui
#获取屏幕大小
size = pyautogui.size()
print(size)
mouse_pos = pyautogui.position()
print(mouse_pos)
print(pyautogui.onScreen(100,100))