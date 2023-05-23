import pyautogui
from time import sleep


pyautogui.hotkey('alt', 'tab')
sleep(2)
for click in range (0, 100):
    pyautogui.click(x=564, y=749) #Personagem
    pyautogui.click(x=626, y=594) #Confirmar 
    sleep(0.25)    
    pyautogui.click(x=564, y=749) #Personagem
    pyautogui.click(x=626, y=594) #Confirmar 
    sleep(0.25)    
    pyautogui.click(x=564, y=749) #Personagem
    pyautogui.click(x=626, y=594) #Confirmar
    sleep(0.25)
print('Terminei...') 
# sleep(3)
# print(pyautogui.position())

