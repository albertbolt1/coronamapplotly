from django.shortcuts import render
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go



def some(request):
	df = pd.read_csv("https://gist.githubusercontent.com/albertbolt1/7d618295b0845f645d7d92db632534e6/raw/d84d0cc0fd634195bb0fbe14f3f7d5fcd3ba87e7/corona.csv")
	fig = go.Figure(data=go.Choropleth(
		geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    	featureidkey='properties.ST_NM',
    	locationmode='geojson-id',
   	 	locations=df['state'],
    	z=df['deaths'],

    	autocolorscale=False,
    	colorscale='Blues',
    	marker_line_color='peachpuff',

    	colorbar=dict(
    		title={'text': "Active Cases"},

        	thickness=15,
        	len=0.35,
        	bgcolor='rgba(255,255,255,0.6)',

        	tick0=0,
        	dtick=20000,

        	xanchor='left',
        	x=0.01,
        	yanchor='bottom',
        	y=0.05
    	)
	))

	fig.update_geos(
    	visible=False,
    	projection=dict(
        	type='conic conformal',
        	parallels=[12.472944444, 35.172805555556],
        	rotation={'lat': 24, 'lon': 80}
    	),
    	lonaxis={'range': [68, 98]},
    	lataxis={'range': [6, 38]}
	)

	fig.update_layout(
    	title=dict(
        	text="No of Corona Death Cases in India by State as of Nov 5, 2020",
        	xanchor='center',
        	x=0.5,
        	yref='paper',
        	yanchor='bottom',
        	y=1,
        	pad={'b': 10}
    	),
    	margin={'r': 30, 't': 30, 'l': 30, 'b': 30},
    	height=600,
    	width=1000
		)

	graph = fig.to_html(full_html=False, default_height=600, default_width=1000)
	return render(request, 'maps/home.html', {'graph':graph})
