import pandas as pd
import os

dir_current = os.getcwd()
file_name = 'data.xlsx'
exit()


expenses = {
    'name',
    'desc',
    'value'
}
profits = {
    'name',
    'desc',
    'value'
}

expenses_df = pd.DataFrame(expenses)
profits_df = pd.DataFrame(profits)

with pd.ExcelWriter(file_name) as writer:
    expenses_df.to_excel(writer, sheet_name='expenses', index=False)
    expenses_df.to_excel(writer, sheet_name='expenses', index=False)