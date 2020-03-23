import datetime
import logging
import os
import azure.functions as func
import pyodbc



def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    username = os.environ.get('keyvault_db_username')
    password = os.environ.get('keyvault_db_password')

    logging.info('username: %s'%username)
    logging.info('password: %s'%password)

    logging.info('Python timer trigger function ran at %s', utc_timestamp)


    if mytimer.past_due:
        logging.info('The timer is past due!')

    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=covid19dbserver.database.windows.net;"
                      "Database=covid19db;"
                      "Uid=serveradmin;"
                      "Pwd=IlKh1LBn70XcfUCdu8KB;"
                      "Trusted_Connection=no;")

    cursor=cnxn.cursor()

    testquery = "INSERT INTO smalltest (anytext) VALUES ('testfromfunction %s');"%utc_timestamp
    logging.info('testquery: %s'%testquery)

    cursor.execute(testquery)
    cnxn.commit()
