import plotly.plotly as py
import plotly.graph_objs as go
import plotly 
import sys
import pyodbc

plotly.tools.set_credentials_file(username='pjag', api_key='YA121gXBTHzLxlWJvA1V')


def plotData():
 try:
   cnx = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};Server=localhost\SQLEXPRESS;Database=PollutionMonitor;Trusted_Connection=yes;uid=IMPAQ\pjag;pwd=")
   cursor = cnx.cursor()

   getDataForPoznan = "SELECT max(aqi) as aqi, aqitime FROM [dbo].[data] WHERE idx = 6531 group by aqitime"
   getDataForCordoba = "SELECT max(aqi) as aqi, aqitime FROM [dbo].[data] WHERE idx = 8461 group by aqitime"
   getDataForLiverpool = "SELECT max(aqi) as aqi, aqitime FROM [dbo].[data] WHERE idx = 3187 group by aqitime"
   getDataForNijmegen = "SELECT max(aqi) as aqi, aqitime FROM [dbo].[data] WHERE idx = 6477 group by aqitime"
   getDataForToulouse = "SELECT max(aqi) as aqi, aqitime FROM [dbo].[data] WHERE idx = 3835 group by aqitime"
   getDataForHanover = "SELECT max(aqi) as aqi, aqitime FROM [dbo].[data] WHERE idx = 6205 group by aqitime"
   getDataForGent = "SELECT max(aqi) as aqi, aqitime FROM [dbo].[data] WHERE idx = 8904 group by aqitime"

   xP = []
   yP = []
   cursor.execute(getDataForPoznan)
   valueP = cursor.fetchall()
   for i in valueP:
      xP.insert(1, i[1])
      yP.insert(2, i[0]) 
   tracePoznan = {"x": xP, "y": yP, "marker": {"color": "green", "size": 12}, "mode": "markers", "name": "Poznan", "type": "scatter"}
   
   xC = []
   yC = []
   cursor.execute(getDataForCordoba)
   valueC = cursor.fetchall()
   for i in valueC:
      xC.insert(1, i[1])
      yC.insert(2, i[0])   
   traceCordoba = {"x": xC, "y": yC, "marker": {"color": "blue", "size": 12}, "mode": "markers", "name": "Cordoba", "type": "scatter"}
   
   xL = []
   yL = []
   cursor.execute(getDataForLiverpool)
   valueL = cursor.fetchall()
   for i in valueL:
      xL.insert(1, i[1])
      yL.insert(2, i[0])   
   traceLiverpool = {"x": xL, "y": yL, "marker": {"color": "red", "size": 12}, "mode": "markers", "name": "Liverpool", "type": "scatter"}
   
   xN = []
   yN = []
   cursor.execute(getDataForNijmegen)
   valueN = cursor.fetchall()
   for i in valueN:
      xN.insert(1, i[1])
      yN.insert(2, i[0])   
   traceNijmegen = {"x": xN, "y": yN, "marker": {"color": "orange", "size": 12}, "mode": "markers", "name": "Nijmegen", "type": "scatter"}
   
   xT = []
   yT = []
   cursor.execute(getDataForToulouse)
   valueT = cursor.fetchall()
   for i in valueT:
      xT.insert(1, i[1])
      yT.insert(2, i[0])  
   traceToulouse = {"x": xT, "y": yT, "marker": {"color": "black", "size": 12}, "mode": "markers", "name": "Toulouse", "type": "scatter"}
   
   xH = []
   yH = []
   cursor.execute(getDataForHanover)
   valueH = cursor.fetchall()
   for i in valueH:
      xH.insert(1, i[1])
      yH.insert(2, i[0])   
   traceHanover = {"x": xH, "y": yH, "marker": {"color": "grey", "size": 12}, "mode": "markers", "name": "Hanover", "type": "scatter"}
   
   xG = []
   yG = []
   cursor.execute(getDataForGent)
   valueG = cursor.fetchall()
   for i in valueG:
      xG.insert(1, i[1])
      yG.insert(2, i[0])   
   traceGent = {"x": xG, "y": yG, "marker": {"color": "pink", "size": 12}, "mode": "markers", "name": "Gent", "type": "scatter"}


   data = [tracePoznan, traceCordoba, traceLiverpool, traceNijmegen, traceToulouse, traceHanover, traceGent]
   layout = {"title": "Pollution Monitoring", "xaxis": {"title": "Date", }, "yaxis": {"title": "Air Quality Index"}}

   fig = go.Figure(data=data, layout=layout)
   py.plot(fig, filenmae='basic_dot-plot')
   cursor.close()

 except:
   print 'errors in plotData function'
 else:
   cnx.close()