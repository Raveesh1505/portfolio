"""
----- Scrript file -----
Contains the code to additional fucntions required
in the website.
"""

from pyairtable import Api
import pandas as pd

def read_airtable(token:str, baseID:str, table_name:str):
    '''
    Function to read data from airtable.
    '''

    api = Api(token)   # Fetch api token from env var
    table = api.table(baseID, table_name)
    response = table.all()

    # Converting the extracted JSON format to
    # pandas for printing
    dataFrame = pd.json_normalize(response)
    dataFrame = dataFrame.drop(columns=["id", "createdTime", "fields.S.No"])  # Removing unwanted cols

    # Renaming cols
    dataFrame = dataFrame.rename(
        columns = {
            "fields.Notes" : "Notes",
            "fields.Link" : "Link",
            "fields.Project" : "Project"
        }
    )
    return dataFrame