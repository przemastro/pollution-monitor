import requests
import sys
import pyodbc


def getData(cityId):
 try:
   cityId = str(cityId) 
   request=requests.get('https://api.waqi.info/api/feed/@'+cityId+'/aqi.json', headers={"content-type":"text","Host": "api.waqi.info","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "pl,en-US;q=0.7,en;q=0.3","Accept-Encoding": "gzip, deflate, br","Connection": "keep-alive","Upgrade-Insecure-Requests": "1","Cache-Control": "max-age=0"})
   json = request.json()
   aqi = json['rxs']['obs'][0]['msg']['aqi']
   aqitime = json['rxs']['obs'][0]['msg']['time']['s']
   idx = json['rxs']['obs'][0]['msg']['idx']
   city = json['rxs']['obs'][0]['msg']['city']['name']
   #pm10 = json['rxs']['obs'][0]['msg']['iaqi']['pm10']['v']
   #pm10time = json['rxs']['obs'][0]['msg']['iaqi']['pm10']['t']
   #o3 = json['rxs']['obs'][0]['msg']['iaqi']['o3']['v']
   #o3time = json['rxs']['obs'][0]['msg']['iaqi']['o3']['t']
   no2 = json['rxs']['obs'][0]['msg']['iaqi']['no2']['v']
   no2time = json['rxs']['obs'][0]['msg']['iaqi']['no2']['t']
   #so2 = json['rxs']['obs'][0]['msg']['iaqi']['so2']['v']
   #so2time = json['rxs']['obs'][0]['msg']['iaqi']['so2']['t']
   #wind = json['rxs']['obs'][0]['msg']['iaqi']['wg']['v']
   #windtime = json['rxs']['obs'][0]['msg']['iaqi']['wg']['t']
   #pressure = json['rxs']['obs'][0]['msg']['iaqi']['p']['v']
   #pressuretime = json['rxs']['obs'][0]['msg']['iaqi']['p']['t']
   #humidity = json['rxs']['obs'][0]['msg']['iaqi']['h']['v']
   #humiditytime = json['rxs']['obs'][0]['msg']['iaqi']['h']['t']
   #temperature = json['rxs']['obs'][0]['msg']['iaqi']['t']['v']
   #temperaturetime = json['rxs']['obs'][0]['msg']['iaqi']['t']['t']
   print aqi

   cnx = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};Server=localhost\SQLEXPRESS;Database=PollutionMonitor;Trusted_Connection=yes;uid=IMPAQ\pjag;pwd=")
   cursor = cnx.cursor()
   cursor.execute("insert into [dbo].[data](idx, city, aqi, aqitime, no2, no2time) values(?,?,?,?,?,?);",idx,city,aqi,aqitime,no2,no2time)
   cnx.commit()
   cursor.close()

 except:
   print 'errors in getData function'
 else:
   cnx.close()
