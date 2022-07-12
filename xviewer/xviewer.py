import win32com.client as win32
from win32gui import SetForegroundWindow
import pandas as pd

class XViewer():
    
    def __init__(self, df) -> None:
        self.df = df.copy(True) # deep copy so no later dependency to the df
        self.xl = win32.Dispatch('Excel.Application') # setup an excel in background

    # def __del__(self) -> None:
    #     print(">> closing dispatched Excel...")
    #     self.xl.Quit()

    def show(self) -> None:
        self.xl.Visible = True
        wb = self.xl.Workbooks.Add()
        ws = wb.Worksheets("sheet1")

        end_row, end_col = self.df.shape

        # print header
        ws.Range(ws.Cells(1, 1), ws.Cells(1, end_col)).Value = self.df.columns.values
        # print content
        ws.Range(ws.Cells(2, 1), ws.Cells(end_row + 1, end_col)).Value = self.df.values        
        



print('='*70)
print(">> In script trial...")

data = [
    ('a1', 'A', 1), 
    ('a2', 'A', 3), 
    ('b1', 'B', 3), 
]

df = pd.DataFrame(data, columns=['Key', 'Class', 'Value'])

viewer = XViewer(df)
viewer.show()
print('='*70)





