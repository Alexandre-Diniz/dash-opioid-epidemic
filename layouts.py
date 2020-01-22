import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

layout = html.Div(className='root', children=[
	
	html.Div(className='box', children=[

		html.Div(className='head', children=[
			html.P(className='head-text', children=[
				'Rate of US Poison-Induced Deaths'
			]),
			html.Div(className='head-sub', children=[

				html.Div(className='vertical-line', children=[]),

				html.Div(className='head-sub-sub', children=[
					html.P(className='head-sub-text', children=[
						"""Deaths are classified using the Internertional Classification of Diseases, 
						Tenth Revision (ICD-10). Drug-poisoning deaths are defining as having
						ICD-10 underlying cause-of-death codes X40-X44 (unintentional), X60-X64
						(suicide), X85 (homicide), or Y10-Y14 (undertermined intent)"""
						])
				])
			])
			
		]),

		html.Div(className='div1', children=[
			
			html.Div(className='div1-1', children=[

				html.Div(className='div1-1-1', children=[
					html.P(className='P', children=['This div should have a slider range'])
				]),
				html.Div(className='div1-1-2', children=[
					html.Div(className='P', children=['This div should have a map'])
				])
				
			]),

			html.Div(className='div1-2', children=[
				html.P(className='P', children=['This div should have a dropdown']),
				html.P(className='P', children=['This div shoulb have a graph'])
			])
		])

	]),

])