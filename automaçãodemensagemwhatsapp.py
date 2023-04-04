

# In[132]:
import pyautogui as pd
import time
import pyperclip

pyautogui.PAUSE = 1.5

pyautogui.press('Win')
pyautogui.click(x=1019, y=548)
time.sleep(3)
pyautogui.hotkey('ctrl','f')
pyautogui.write('Pai')
pyautogui.click(x=275, y=252)
pyautogui.write('Bom dia Pai !')
pyautogui.click(x=597, y=976)
pyautogui.write('m')
pyautogui.click(x=575, y=548)
time.sleep(2)
pd.click(x=801, y=985)
pd.click(x=801, y=985)
pd.press('space')
pd.press('tab')
pd.press('enter')
pd.press('tab')
pd.click(x=777, y=986)
pyperclip.copy('Tudo bem ?')
pd.hotkey('ctrl','v')
pd.press('tab')
pd.press('enter')
pd.hotkey('ctrl','f')
pyperclip.copy('Mãe')
pd.hotkey('ctrl','v')
pd.click(x=388, y=238)
pyperclip.copy('Bom dia Mãe ! ')
pd.hotkey('ctrl','v')
pd.click(x=567, y=984)
pd.write('m')
pd.click(x=570, y=562)
pd.press('backspace')
pd.write('amor')
pd.click(x=324, y=562)
pd.click(x=886, y=989)
pd.press('tab')
pd.press('enter')
pd.press('tab')
pd.click(x=915, y=990)
pyperclip.copy('Tudo bem ?')
pd.hotkey('ctrl','v')
pd.press('tab')
pd.press('enter')
pd.hotkey('ctrl','f')
pyperclip.copy('Letícia')
pd.hotkey('ctrl','v')
pd.click(x=332, y=226)
pd.write('Bom dia minha princesa ! ')
pd.click(x=579, y=988)
pd.write('amor')
pd.click(x=318, y=564)
pd.click(x=1069, y=994)
pd.press('tab')
pd.press('enter')
pd.press('tab')
pd.click(x=1136, y=989)
pyperclip.copy('Que Deus te guarde ! '+'\nQue ele te proteja ! '+'\nQue você tenha um dia maravilhoso minha loira ! ')
pd.hotkey('ctrl','v')
pd.press('tab')
pd.press('enter')
pd.press('tab')
pd.click(x=1083, y=993)
pd.write('EU TE AMO MUITOOOO !')
pd.press('tab')
pd.press('enter')
pd.press('tab')
pd.click(x=581, y=995)
pd.write('amor')
pd.click(x=327, y=562)
time.sleep(2)
pd.click(x=998, y=989)
pd.click(x=998, y=989)
pd.press('tab')
pd.press('enter')
time.sleep(3)
pd.hotkey('alt','F4')


# In[127]:


import time
time.sleep(5)
print(pyautogui.position())



























