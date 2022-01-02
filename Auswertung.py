#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("Programm startet")
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
df = pd.read_csv('C:\\Users\\User\\Desktop\\T1.csv')
Tan1 = df[df[' Tanlstelle'].astype(str).str.contains('21974')]
Tan2 = df[df[' Tanlstelle'].astype(str).str.contains('10063')]
Tan3 = df[df[' Tanlstelle'].astype(str).str.contains('37955')]
Tan4 = df[df[' Tanlstelle'].astype(str).str.contains('40018')]
Tan1Datum = Tan1[' Uhrzeit']
Tan1LPG = Tan1[' LPG']
Tan1E10 = Tan1[' Benzin E10']
Tan1E5= Tan1['Benzin E5']
Tan1Diesel= Tan1['Diesel']

Tan2Datum = Tan2[' Uhrzeit']
Tan2LPG = Tan2[' LPG']
Tan2E10 = Tan2[' Benzin E10']
Tan2E5= Tan2['Benzin E5']
Tan2Diesel= Tan2['Diesel']

Tan3Datum = Tan3[' Uhrzeit']
Tan3LPG = Tan3[' LPG']
Tan3E10 = Tan3[' Benzin E10']
Tan3E5= Tan3['Benzin E5']
Tan3Diesel= Tan3['Diesel']

Tan4Datum = Tan4[' Uhrzeit']
Tan4LPG = Tan4[' LPG']
Tan4E10 = Tan4[' Benzin E10']
Tan4E5= Tan4['Benzin E5']
Tan4Diesel= Tan4['Diesel']
#print(covidDE)
#fig = px.line(df, x = ' Uhrzeit', y = 'Diesel', title='Apple Share Prices over time (2014)')
#fig2 = px.line(Tan1, x = ' Uhrzeit', y = 'Diesel', title='Diese 21974')
#fig.show()
#fig2.show()
#fig2 = px.line(Tan2, x = ' Uhrzeit', y = ' Benzin E10', title='Diese 10063')
#fig2.show()

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
    title="Tankstellenpreise (Rapp in Vai, freie Tankstelle)",
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
fig.write_image("C:\\Users\\User\\Desktop\\fig1.pdf")     
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
    title="Tankstellenpreise (Agip Stuttgart HeilbronnerStr)",
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
fig.write_image("C:\\Users\\User\\Desktop\\fig2.pdf")     
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
    title="Tankstellenpreise (Heiligenberg Rickertsreute)",
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
fig.write_image("C:\\Users\\User\\Desktop\\fig3.pdf")     
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
    title="Tankstellenpreise (Roth Energie in FRA)",
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
fig.write_image("C:\\Users\\User\\Desktop\\fig4.pdf")     
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
    title="Tankstellenpreise (Roth Energie in FRA)",
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
fig.write_image("C:\\Users\\User\\Desktop\\fig5.pdf")   
#Abbilden des Graphen    
fig.show()
## Plat Tankstelle im Vergleich, Ende


# In[ ]:




