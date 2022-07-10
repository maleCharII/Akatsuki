import win32com.client as win32
import os
import time
from win32gui import SetForegroundWindow

print("="*75)


print(">> Open an excel interface")
xl = win32.Dispatch('Excel.Application')
xl.Visible = True
SetForegroundWindow(xl.hwnd)

try:
    print(">> Add an Excel workbook")
    wb = xl.Workbooks.Add()
except Exception as e:
    print(e.args)    
finally:
    print(">> waiting and quit")
    time.sleep(5)
    xl.Quit()


print("="*75)
