# %% [markdown]
# <img src="https://pandas.pydata.org/static/img/pandas.svg" width="250">
# 
# ## <center> Beyond Pandas with GeoPandas

# %%
import pandas as pd
import geopandas

# %%
peaks = pd.DataFrame(
    {'Peak Name': ['Green Mtn.', 'So. Boulder Peak', 'Bear Peak', 'Flagstaff Mtn.', 'Mt. Sanitas'],
     'Latitude': [39.9821, 39.9539, 39.9603, 40.0017, 40.0360968],
     'Longitude': [-105.3016, -105.2992, -105.2952, -105.3075, -105.3061024]})

# %%
gdf = geopandas.GeoDataFrame(
    peaks, geometry=geopandas.points_from_xy(peaks.Longitude, peaks.Latitude))
gdf

# %%
import plotly.express as px
px.set_mapbox_access_token(token)
gdf['size'] = 65

fig = px.scatter_mapbox(gdf,
                        lat=gdf.geometry.y,
                        lon=gdf.geometry.x,
                        color="Peak Name",
                        hover_name="Peak Name",
                        mapbox_style='outdoors',
                        size='size',
                        zoom=10)

fig.show()

# %%



