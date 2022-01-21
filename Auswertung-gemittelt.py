#!/usr/bin/env python
# coding: utf-8

# In[2]:



print("Programm startet")
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime
df = pd.read_csv('C:\\Users\\User\\Documents\\Python-Ausgabe\\T1.csv')
Tan1 = df[df[' Tanlstelle'].astype(str).str.contains('21974')]
Tan2 = df[df[' Tanlstelle'].astype(str).str.contains('10063')]
Tan3 = df[df[' Tanlstelle'].astype(str).str.contains('37955')]
Tan4 = df[df[' Tanlstelle'].astype(str).str.contains('40018')]



## Daten für Tankstelle 1 (Rapp in Vaihingen an der Enz) aufbereiten
Tan1Datum = pd.to_datetime(Tan1[' Uhrzeit'])
Tan1LPG = Tan1[' LPG']
Tan1E10 = Tan1[' Benzin E10']
Tan1E5= Tan1['Benzin E5']
Tan1Diesel= Tan1['Diesel']
# Daten mitteln für Tankstelle 1, Anfang
for i in range(7):
    # Wir bilden von zwei Werten jeweils den Mittelwert und behalten im Datensatz den Mittelwert. Dies machen wir 7 Mal. Somit haben wir noch 1,8 Werte pro Tag, welche auf 240 Messpunkten basieren. 
   Tan1Datum = Tan1Datum.groupby(np.arange(len(Tan1Datum))//2).mean()
   Tan1LPG = Tan1LPG.groupby(np.arange(len(Tan1LPG))//2).mean()
   Tan1E10 = Tan1E10.groupby(np.arange(len(Tan1E10))//2).mean()
   Tan1E5 = Tan1E5.groupby(np.arange(len(Tan1E5))//2).mean()
   Tan1Diesel = Tan1Diesel.groupby(np.arange(len(Tan1Diesel))//2).mean()
# Daten mitteln für Tankstelle 1, Ende    



## Daten für Tankstelle 2 (Agip in Stuttgart) aufbereiten
Tan2Datum = pd.to_datetime(Tan2[' Uhrzeit'])
Tan2LPG = Tan2[' LPG']
Tan2E10 = Tan2[' Benzin E10']
Tan2E5= Tan2['Benzin E5']
Tan2Diesel= Tan2['Diesel']
# Daten mitteln für Tankstelle 2, Anfang
for i in range(7):
    # Wir bilden von zwei Werten jeweils den Mittelwert und behalten im Datensatz den Mittelwert. Dies machen wir 7 Mal. Somit haben wir noch 1,8 Werte pro Tag, welche auf 240 Messpunkten basieren. 
   Tan2Datum = Tan2Datum.groupby(np.arange(len(Tan2Datum))//2).mean()
   Tan2LPG = Tan2LPG.groupby(np.arange(len(Tan2LPG))//2).mean()
   Tan2E10 = Tan2E10.groupby(np.arange(len(Tan2E10))//2).mean()
   Tan2E5 = Tan2E5.groupby(np.arange(len(Tan2E5))//2).mean()
   Tan2Diesel = Tan2Diesel.groupby(np.arange(len(Tan2Diesel))//2).mean()
# Daten mitteln für Tankstelle 2, Ende 



## Daten für Tankstelle 3 (Wilfried Ermler in Heiligenberg (Rickerstreute)) aufbereiten
Tan3Datum = pd.to_datetime(Tan3[' Uhrzeit'])
Tan3LPG = Tan3[' LPG']
Tan3E10 = Tan3[' Benzin E10']
Tan3E5= Tan3['Benzin E5']
Tan3Diesel= Tan3['Diesel']
# Daten mitteln für Tankstelle 3, Anfang
for i in range(7):
    # Wir bilden von zwei Werten jeweils den Mittelwert und behalten im Datensatz den Mittelwert. Dies machen wir 7 Mal. Somit haben wir noch 1,8 Werte pro Tag, welche auf 240 Messpunkten basieren. 
   Tan3Datum = Tan3Datum.groupby(np.arange(len(Tan3Datum))//2).mean()
   Tan3LPG = Tan3LPG.groupby(np.arange(len(Tan3LPG))//2).mean()
   Tan3E10 = Tan3E10.groupby(np.arange(len(Tan3E10))//2).mean()
   Tan3E5 = Tan3E5.groupby(np.arange(len(Tan3E5))//2).mean()
   Tan3Diesel = Tan3Diesel.groupby(np.arange(len(Tan3Diesel))//2).mean()
# Daten mitteln für Tankstelle 3, Ende 



## Daten für Tankstelle 4 (Roth Energie in Frankfurt am Main) aufbereiten
Tan4Datum = pd.to_datetime(Tan4[' Uhrzeit'])
Tan4LPG = Tan4[' LPG']
Tan4E10 = Tan4[' Benzin E10']
Tan4E5= Tan4['Benzin E5']
Tan4Diesel= Tan4['Diesel']
# Daten mitteln für Tankstelle 4, Anfang
for i in range(7):
    # Wir bilden von zwei Werten jeweils den Mittelwert und behalten im Datensatz den Mittelwert. Dies machen wir 7 Mal. Somit haben wir noch 1,8 Werte pro Tag, welche auf 240 Messpunkten basieren. 
   Tan4Datum = Tan4Datum.groupby(np.arange(len(Tan4Datum))//2).mean()
   Tan4LPG = Tan4LPG.groupby(np.arange(len(Tan4LPG))//2).mean()
   Tan4E10 = Tan4E10.groupby(np.arange(len(Tan4E10))//2).mean()
   Tan4E5 = Tan4E5.groupby(np.arange(len(Tan4E5))//2).mean()
   Tan4Diesel = Tan4Diesel.groupby(np.arange(len(Tan4Diesel))//2).mean()
# Daten mitteln für Tankstelle 4, Ende 

## Plat Tankstelle 1, Anfang
fig = go.Figure()

fig.add_trace(
    go.Scatter( x=Tan1Datum, y=Tan1LPG, name='LPG',
               #Aussehen des Graphen bestimmen
               mode='lines',
        # Setzen der Farbe und Graphenbreite   
        line=dict(color='rgb(49,130,189)', width=3),    
    ))
fig.add_trace(
    go.Scatter( x=Tan1Datum, y=Tan1E10, 
               mode='lines', name='E10',
        line=dict( color='rgb(49, 189, 82)', width=3)
    ))
fig.add_trace(
    go.Scatter(x=Tan1Datum,y=Tan1E5,
               mode='lines',name='E5',
        line=dict(color='rgb(189, 49, 84)', width=3)
    ))
fig.add_trace(
    go.Scatter(x=Tan1Datum,y=Tan1Diesel,
               mode='lines',name='Diesel',
        line=dict(color='rgb(255, 165, 0)', width=3)
    ))
fig.update_layout(
    #Titel
    title="Tankstellenpreise (Rapp in Vai, freie Tankstelle, gemittelt)",
    #Achsenbeschriftungen
    yaxis_title="Preis in Euro pro Liter",
    xaxis_title="Datum",
    
    #Setzen eines Hovertools 
    hovermode="x unified",
    #Hintergrundfarbe
    plot_bgcolor='rgb(242,242,242)' ,
    #Anpassen der Größe des Graphen    
    autosize=False,
    width=610,
    height=450,  
)
fig.write_image("C:\\Users\\User\\Documents\\Python-Ausgabe\\fig1-gemittelt.pdf")     
#Abbilden des Graphen    
fig.show()
## Plat Tankstelle 1, Ende



## Plat Tankstelle 2, Anfang
fig = go.Figure()

fig.add_trace(
    go.Scatter( x=Tan2Datum, y=Tan2LPG, name='LPG',
               #Aussehen des Graphen bestimmen
               mode='lines',
        # Setzen der Farbe und Graphenbreite   
        line=dict(color='rgb(49,130,189)', width=3),    
    ))
fig.add_trace(
    go.Scatter( x=Tan2Datum, y=Tan2E10, 
               mode='lines', name='E10',
        line=dict( color='rgb(49, 189, 82)', width=3)
    ))
fig.add_trace(
    go.Scatter(x=Tan2Datum,y=Tan2E5,
               mode='lines',name='E5',
        line=dict(color='rgb(189, 49, 84)', width=3)
    ))
fig.add_trace(
    go.Scatter(x=Tan2Datum,y=Tan2Diesel,
               mode='lines',name='Diesel',
        line=dict(color='rgb(255, 165, 0)', width=3)
    ))
fig.update_layout(
    #Titel
    title="Tankstellenpreise (Agip Stuttgart HeilbronnerStr, gemittelt)",
    #Achsenbeschriftungen
    yaxis_title="Preis in Euro pro Liter",
    xaxis_title="Datum",
    
    #Setzen eines Hovertools 
    hovermode="x unified",
    #Hintergrundfarbe
    plot_bgcolor='rgb(242,242,242)' ,
    #Anpassen der Größe des Graphen    
    autosize=False,
    width=610,
    height=450,  
)
fig.write_image("C:\\Users\\User\\Documents\\Python-Ausgabe\\fig2-gemittelt.pdf")     
#Abbilden des Graphen    
fig.show()
## Plat Tankstelle 2, Ende


## Plat Tankstelle 3, Anfang
fig = go.Figure()

fig.add_trace(
    go.Scatter( x=Tan3Datum, y=Tan3LPG, name='LPG',
               #Aussehen des Graphen bestimmen
               mode='lines',
        # Setzen der Farbe und Graphenbreite   
        line=dict(color='rgb(49,130,189)', width=3),    
    ))
fig.add_trace(
    go.Scatter( x=Tan3Datum, y=Tan3E10, 
               mode='lines', name='E10',
        line=dict( color='rgb(49, 189, 82)', width=3)
    ))
fig.add_trace(
    go.Scatter(x=Tan3Datum,y=Tan3E5,
               mode='lines',name='E5',
        line=dict(color='rgb(189, 49, 84)', width=3)
    ))
fig.add_trace(
    go.Scatter(x=Tan3Datum,y=Tan3Diesel,
               mode='lines',name='Diesel',
        line=dict(color='rgb(255, 165, 0)', width=3)
    ))
fig.update_layout(
    #Titel
    title="Tankstellenpreise (Heiligenberg Rickertsreute, gemittelt)",
    #Achsenbeschriftungen
    yaxis_title="Preis in Euro pro Liter",
    xaxis_title="Datum",
    
    #Setzen eines Hovertools 
    hovermode="x unified",
    #Hintergrundfarbe
    plot_bgcolor='rgb(242,242,242)' ,
    #Anpassen der Größe des Graphen    
    autosize=False,
    width=610,
    height=450,  
)
fig.write_image("C:\\Users\\User\\Documents\\Python-Ausgabe\\fig3-gemittelt.pdf")     
#Abbilden des Graphen    
fig.show()
## Plat Tankstelle 3, Ende


## Plat Tankstelle 4, Anfang
fig = go.Figure()

fig.add_trace(
    go.Scatter( x=Tan4Datum, y=Tan4LPG, name='LPG',
               #Aussehen des Graphen bestimmen
               mode='lines',
        # Setzen der Farbe und Graphenbreite   
        line=dict(color='rgb(49,130,189)', width=3),    
    ))
fig.add_trace(
    go.Scatter( x=Tan4Datum, y=Tan4E10, 
               mode='lines', name='E10',
        line=dict( color='rgb(49, 189, 82)', width=3)
    ))
fig.add_trace(
    go.Scatter(x=Tan4Datum,y=Tan4E5,
               mode='lines',name='E5',
        line=dict(color='rgb(189, 49, 84)', width=3)
    ))
fig.add_trace(
    go.Scatter(x=Tan4Datum,y=Tan4Diesel,
               mode='lines',name='Diesel',
        line=dict(color='rgb(255, 165, 0)', width=3)
    ))
fig.update_layout(
    #Titel
    title="Tankstellenpreise (Roth Energie in FRA, gemittelt)",
    #Achsenbeschriftungen
    yaxis_title="Preis in Euro pro Liter",
    xaxis_title="Datum",
    
    #Setzen eines Hovertools 
    hovermode="x unified",
    #Hintergrundfarbe
    plot_bgcolor='rgb(242,242,242)' ,
    #Anpassen der Größe des Graphen    
    autosize=False,
    width=610,
    height=450,  
)
fig.write_image("C:\\Users\\User\\Documents\\Python-Ausgabe\\fig4-gemittelt.pdf")     
#Abbilden des Graphen    
fig.show()
## Plat Tankstelle 4, Ende


## Plat Tankstelle im Vergleich, Anfang
fig = go.Figure()

fig.add_trace(
    go.Scatter( x=Tan1Datum, y=Tan1E10, name='E10 Rapp in Vai',
               #Aussehen des Graphen bestimmen
               mode='lines',
        # Setzen der Farbe und Graphenbreite   
        line=dict(color='rgb(49,130,189)', width=3),    
    ))
fig.add_trace(
    go.Scatter( x=Tan2Datum, y=Tan2E10, 
               mode='lines', name='E10 Agip Stuttgart',
        line=dict( color='rgb(49, 189, 82)', width=3)
    ))
fig.add_trace(
    go.Scatter(x=Tan3Datum,y=Tan3E10,
               mode='lines',name='E10 Heiligenberg',
        line=dict(color='rgb(189, 49, 84)', width=3)
    ))
fig.add_trace(
    go.Scatter(x=Tan4Datum,y=Tan4E10,
               mode='lines',name='E10 in FRA',
        line=dict(color='rgb(255, 165, 0)', width=3)
    ))
fig.update_layout(
    #Titel
    title="Tankstellenpreise im Vergleich, gemittelt",
    #Achsenbeschriftungen
    yaxis_title="Preis in Euro pro Liter",
    xaxis_title="Datum",
    
    #Setzen eines Hovertools 
    hovermode="x unified",
    #Hintergrundfarbe
    plot_bgcolor='rgb(242,242,242)' ,
    #Anpassen der Größe des Graphen    
    autosize=False,
    width=610,
    height=450,  
)
fig.write_image("C:\\Users\\User\\Documents\\Python-Ausgabe\\fig5-gemittelt.pdf")   
#Abbilden des Graphen    
fig.show()


# In[ ]:




