import pandas as pd
import requests
import plotly.express as px
import json
from geopy.geocoders import Nominatim
import pandas as pd
import pylab 
import networkx as nx
import pickle



usStates = {
  "Alabama": 0,
  "Alaska": 0,
  "American Samoa": 0,
  "Arizona": 0,
  "Arkansas": 0,
  "California": 0,
  "Colorado": 0,
  "Connecticut": 0,
  "Delaware": 0,
  "District Of Columbia": 0,
  "Federated States Of Micronesia": 0,
  "Florida": 0,
  "Georgia": 0,
  "Guam": 0,
  "Hawaii": 0,
  "Idaho": 0,
  "Illinois": 0,
  "Indiana": 0,
  "Iowa": 0,
  "Kansas": 0,
  "Kentucky": 0,
  "Louisiana": 0,
  "Maine": 0,
  "Marshall Islands": 0,
  "Maryland": 0,
  "Massachusetts": 0,
  "Michigan": 0,
  "Minnesota": 0,
  "Mississippi": 0,
  "Missouri": 0,
  "Montana": 0,
  "Nebraska": 0,
  "Nevada": 0,
  "New Hampshire": 0,
  "New Jersey": 0,
  "New Mexico": 0,
  "New York": 0,
  "North Carolina": 0,
  "North Dakota": 0,
  "Northern Mariana Islands": 0,
  "Ohio": 0,
  "Oklahoma": 0,
  "Oregon": 0,
  "Palau": 0,
  "Pennsylvania": 0,
  "Puerto Rico": 0,
  "Rhode Island": 0,
  "South Carolina": 0,
  "South Dakota": 0,
  "Tennessee": 0,
  "Texas": 0,
  "Utah": 0,
  "Vermont": 0,
  "Virgin Islands": 0,
  "Virginia": 0,
  "Washington": 0,
  "West Virginia": 0,
  "Wisconsin": 0,
  "Wyoming" : 0

}

geolocator = Nominatim(user_agent="Nominatim")

cantProductos = {'ems': 0, 'trafico': 0, 'fire': 0}

filtro = pd.read_excel('911.xls')
i = 0
direcciones = []
incidentestipo = []
while (i < 5):
  tipo = filtro['title'][i]
  raw = (geolocator.reverse(str(filtro['lat'][i])+','+str(filtro['lng'][i]))).raw
  try:
    direcciones.append(raw['address']['state'])
    if tipo[:4] == 'EMS:':
      usStates[raw['address']['state']] += 1
    elif tipo[:5] == 'Fire:':
      incidentestipo.append('Fire')
      cantProductos['fire'] += 1
    elif tipo[:8] == 'Traffic:':
      incidentestipo.append('Traffic')
      cantProductos['trafico'] += 1
  except:
   direcciones.append("???")
  
  i += 1
  print(i)


df= pd.DataFrame([[key,usStates[key]] for key in usStates.keys()], columns=['Estado', 'Casos'])
print(df)
with open('usa.json') as file:
  mx_regions_geo = json.load(file)

fig = px.choropleth(data_frame=df, 
                    geojson=mx_regions_geo, 
                    locations='Estado', # nombre de la columna del Dataframe
                    featureidkey='properties.name',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
                    color='Casos', #El color depende de las cantidades
                    color_continuous_scale="burg", #greens
                    #scope="north america"
                   )
fig.update_geos(showcountries=True, showcoastlines=True, showland=True, fitbounds="locations")

fig.update_layout(
    title_text = 'Casos de accidentes en UA',
    font=dict(
        #family="Courier New, monospace",
        family="Ubuntu",
        size=18,
        color="#7f7f7f"
    ),
    annotations = [dict(
        x=0.55,
        y=-0.1,
        xref='paper',
        yref='paper',
        text='Proyecto Python',
        showarrow = False
    )]
)

fig.show()