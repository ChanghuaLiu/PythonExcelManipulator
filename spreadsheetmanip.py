import pandas as pd

# parse the Excel file from hardcoded path
df = pd.read_excel(r'C:\Users\GIRU\Desktop\Book2.xlsx', index_col=0)

# the index column gets parsed as a date time, so convert it to datetime and extract the date
# that way we don't end up with an arbitrary 00:00:00 after each date on the index col
df.index = pd.to_datetime(df.index).date

new_excel_data = []

# iterating through each date
for date, row in df.iterrows():
    # now iterate through each time slot in the row
    for time, value in row.items():
        # now create the new data in our new spreadsheet, repeat the date column and append time and value
        new_excel_data.append([date, time, value])

# output the result to a new dataframe
result = pd.DataFrame(new_excel_data, columns=['Date', 'Time', 'Value'])

# dump new file
result.to_excel(r'C:\Users\GIRU\Desktop\Book3.xlsx', index=False)
