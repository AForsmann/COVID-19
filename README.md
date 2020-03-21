# COVID-19
public accessible data for COVID-19 in Germany

## RKI
As the Robert Koch Institute does not publish data in a computer consumable format, we decided to grab the information from their website and make this dataset public available. 

This dataset is going to be updated daily, as soon as the information from the Robert Koch Institute is available. 

Source: https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Situationsberichte/Archiv.html
Source: https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/917fc37a709542548cc3be077a786c17_0/data?selectedAttribute=GEN

### use the provided csv file
Just download the files from here and use them as they are. We are providing a CSV format. 

https://covid19publicdata.blob.core.windows.net/rki/covid19-germany-federalstates.csv
https://covid19publicdata.blob.core.windows.net/rki/covid19-germany-counties.csv

The URL will stay the same even when data is updated. So feel free to grab this url in an automated manner. 

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
