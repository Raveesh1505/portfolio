"""
----- Script file -----
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
    return dataFrame


def send_query_to_airtable(token:str, baseID: str, table_name:str, queryDetails:dict):
    '''
    Function to send the query to airtable.
    '''
    api = Api(token)   # Fetch api token from env var
    table = api.table(baseID, table_name)
    if table.create(queryDetails):
        return True
    else:
        return False
    

def clean_projects_data(dataFrame:pd.DataFrame):
    '''
    Function to clean the porjects data read from Airtable.
    '''
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


def clean_work_data(dataFrame:pd.DataFrame):
    '''
    Function to clean wokr experience data extracted
    from Airtable.
    '''
    dataFrame = dataFrame.drop(columns=["id", "createdTime", "fields.S.no"])   # Remove unwanted columns
    dataFrame = dataFrame.rename(columns={
        "fields.Title" : "Title",
        "fields.Duration" : "Duration",
        "fields.Description" : "Description"
    })
    return dataFrame