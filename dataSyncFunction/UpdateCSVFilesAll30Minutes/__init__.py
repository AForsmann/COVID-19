import logging
import azure.functions as func
import datetime
import pyodbc
import csv
from azure.storage.blob import BlockBlobService


def main(mytimer: func.TimerRequest) -> None:
    

    if mytimer.past_due:
        logging.info('The timer is past due!')

    block_blob_service = BlockBlobService(account_name='covid19publicdata', account_key='iX7ih9IjJd91YYJkCrZQ6peacQdI+ylBa5RoA6NY5LxMW9O9NAS1/AUQ3pskgM6wMNcNZPxFvb1dQd9p6sVxDw==')

    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                        "Server=covid19dbserver.database.windows.net;"
                        "Database=covid19db;"
                        "Uid=serveradmin;"
                        "Pwd=IlKh1LBn70XcfUCdu8KB;"
                        "Trusted_Connection=no;")

    cursor=cnxn.cursor()
    #FEDERALVIEW
    selectQuery = "SELECT * FROM vRKI ORDER BY [date],[federalstate];"
    rows = cursor.execute(selectQuery)

    with open('covid19-germany-federalstates.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([x[0] for x in cursor.description])  # column headers
        for row in rows:
            writer.writerow(row)

    block_blob_service.create_blob_from_path('rki','covid19-germany-federalstates.csv','covid19-germany-federalstates.csv')

    #COUNTIES VIEW
    selectQueryCounties = "SELECT * FROM vRKICounties ORDER BY [date], [county];"
    rows = cursor.execute(selectQueryCounties)

    with open('covid19-germany-counties.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([x[0] for x in cursor.description])  # column headers
        for row in rows:
            writer.writerow(row)

    block_blob_service.create_blob_from_path('rki','covid19-germany-counties.csv','covid19-germany-counties.csv')

    #HOPKINS VIEW
    selectQueryHopkins = "SELECT * FROM vHopkins ORDER BY [date], [Country/Region];"
    rows = cursor.execute(selectQueryHopkins)

    with open('covid19-hopkins.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([x[0] for x in cursor.description])  # column headers
        for row in rows:
            writer.writerow(row)

    block_blob_service.create_blob_from_path('hopkins','covid19-hopkins.csv','covid19-hopkins.csv')    

    #ECDC VIEW
    selectQueryECDC= "SELECT * FROM vECDC ORDER BY [date],[Country/Region];"
    rows = cursor.execute(selectQueryECDC)

    with open('covid19-ECDC.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([x[0] for x in cursor.description])  # column headers
        for row in rows:
            writer.writerow(row)

    block_blob_service.create_blob_from_path('ecdc','covid19-ECDC.csv','covid19-ECDC.csv')    
