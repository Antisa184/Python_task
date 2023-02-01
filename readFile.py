# Import pandas
import pandas as pd

def readFile (fileName='SpaceNK_2.0 (1).xlsx', rowsToSkip=5, sheetOrder=0):
    # Load the xlsx file
    excel_data = pd.read_excel(fileName, skiprows=rowsToSkip, sheet_name=sheetOrder)
    # Read the values of the file in the dataframe
    data = pd.DataFrame(excel_data, columns=[
                        'Store No', 'Store', 'TY Units','LY Units','TW Sales','LW Sales','LW Var %','LY Sales','LY Var %','YTD Sales','LYTD Sales','LYTD Var %'
                        ])
    # Print the content
    print("The content of the file is:\n", data)

    return data