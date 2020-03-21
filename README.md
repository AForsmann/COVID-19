# COVID-19
public accessible data for COVID-19 in Germany

## RKI
As the Robert Koch Institute does not publish data in a computer consumable format, we decided to grab the information from their website and make this dataset public available. 

This dataset is going to be updated daily, as soon as the information from the Robert Koch Institute is available. 

Source: https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Situationsberichte/Archiv.html

### use the provided files
Just download the files from here and use them as they are. We are providing a CSV format and an Excel format to use. 

### get access to our database
If you would like to connect to our database, feel free to use this information for login:
```
Server: covid19dbserver.database.windows.net
Authentication type: SQL Login
username: datareader
password: eg4?%bKrY.T#SpBhEBk8DmH9
database: covid19db
table: [dbo].[RKI]
view: [dbo].[vRKI]
```
