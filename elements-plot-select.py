# Making a basic Bokeh line graph

# importing bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.sampledata.periodic_table import elements
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, WheelZoomTool
from bokeh.models.sources import ColumnDataSource
from bokeh.models.annotations import Span, BoxAnnotation, Label, LabelSet
from bokeh.layouts import layout
from bokeh.models.widgets import Select

#from screeninfo import get_monitors
#import pandas as pd

# Prepare the output file
# output_file("elements.html")

# Create a figure object
f = figure()

# Style the plot area
#f.plot_width = get_monitors()[0].width
#f.plot_height = get_monitors()[0].height-50
f.plot_width = 1800                       # Width of screen in pixels
f.plot_height = 900                       # Height of screen in pixels
#f.sizing_mode = "stretch_both"

# Visual style the title
f.title.text = "Periodic Table of the Elements"          # Title text
f.xaxis.axis_label="Atomic Radius"                       # x-axis label
f.yaxis.axis_label="Boiling Point"                       # y-axis lable

# Set up different colours for different species
elements.dropna(inplace=True)
colormap = {'gas':'yellow', 'liquid':'orange', 'solid':'red'}
elements['color'] = [colormap[x] for x in elements['standard state']]
elements['size'] = elements['van der Waals radius']/10

# Set up bokeh column data sources
gas    = ColumnDataSource(elements[elements['standard state']=='gas'])
liquid = ColumnDataSource(elements[elements['standard state']=='liquid'])
solid  = ColumnDataSource(elements[elements['standard state']=='solid'])

# See https://docs.bokeh.org/en/latest/docs/reference/plotting.html

f.circle(x='atomic radius', y='boiling point', size='size', fill_alpha=0.2, color='color', legend_label='Gas', source=gas)
f.circle(x='atomic radius', y='boiling point', size='size', fill_alpha=0.2, color='color', legend_label='Liquid', source=liquid)
f.circle(x='atomic radius', y='boiling point', size='size', fill_alpha=0.2, color='color', legend_label='Solid', source=solid)

# create a span (line) annotation
av_gas_boil = sum(gas.data['boiling point'])/len(gas.data['boiling point'])
span_gas = Span(location=av_gas_boil, dimension='width', line_color='yellow', line_width=2)
gas_label = Label(x=80, y=av_gas_boil, text='Gas - average boiling point', render_mode='css')
f.add_layout(span_gas)
f.add_layout(gas_label)

av_liquid_boil = sum(liquid.data['boiling point'])/len(liquid.data['boiling point'])
span_liquid = Span(location=av_liquid_boil, dimension='width', line_color='orange', line_width=2)
liquid_label = Label(x=80, y=av_liquid_boil, text='Liquid - average boiling point', render_mode='css')
f.add_layout(span_liquid)
f.add_layout(liquid_label)

av_solid_boil  = sum(solid.data['boiling point'])/len(solid.data['boiling point'])
min_solid_boil = min(solid.data['boiling point'])
max_solid_boil = max(solid.data['boiling point'])
span_solid = Span(location=av_solid_boil, dimension='width', line_color='red', line_width=2)
solid_label = Label(x=80, y=av_solid_boil, text='Solid - average boiling point', render_mode='css')
f.add_layout(span_solid)
f.add_layout(solid_label)

def update_span(attr, old, new):
    span_solid.location=float(select.value)

option = [(str(av_solid_boil),"Solid Average Boiling Point"),(str(min_solid_boil),"Solid Minimum Boiling Point"),(str(max_solid_boil),"Solid Maximum Boiling Point")]

select = Select(title="Select Span Value", options=option)
select.on_change("value", update_span)

# Write the plot in the figure object
lay_out = layout([[select]])
curdoc().add_root(f)
curdoc().add_root(lay_out)