# Making a basic Bokeh line graph

# importing bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.periodic_table import elements
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, WheelZoomTool
from bokeh.models.sources import ColumnDataSource
from screeninfo import get_monitors
import pandas as pd
from bokeh.layouts import gridplot

# Prepare the output file
output_file("elements_grid.html")

# Create a figure object
f1 = figure(width=500, height=500, title="Gas")

f2 = figure(width=500, height=500, title="Liquid")

f3 = figure(width=500, height=500, title="Solid")

# Set up different colours for different species
elements.dropna(inplace=True)
colormap = {'gas':'green', 'liquid':'blue', 'solid':'red'}
elements['color'] = [colormap[x] for x in elements['standard state']]
elements['size'] = elements['van der Waals radius']/10

# Set up bokeh column data sources
gas    = ColumnDataSource(elements[elements['standard state']=='gas'])
liquid = ColumnDataSource(elements[elements['standard state']=='liquid'])
solid  = ColumnDataSource(elements[elements['standard state']=='solid'])

# See https://docs.bokeh.org/en/latest/docs/reference/plotting.html

f1.circle(x='atomic radius', y='boiling point', size='size', fill_alpha=0.2, color='color', legend_label='Gas', source=gas)
f2.circle(x='atomic radius', y='boiling point', size='size', fill_alpha=0.2, color='color', legend_label='Liquid', source=liquid)
f3.circle(x='atomic radius', y='boiling point', size='size', fill_alpha=0.2, color='color', legend_label='Solid', source=solid)

# Write the plot in the figure object
f = gridplot([[f1,f2],[None,f3]])                  # 2 x 2
show(f)                                            # Show completed figure