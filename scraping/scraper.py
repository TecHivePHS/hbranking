import pandas as pd
import openpyxl as op
import re
wb = op.load_workbook(filename = 'History Bowl 21-22 Scores & Rankings.xlsx', data_only = True)
ws = wb[wb.sheetnames[0]]
df = pd.DataFrame(ws.values)
scores_df = df.iloc[:67]
print(scores_df.to_string())