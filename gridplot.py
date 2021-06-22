# Making a Bokeh multiplot

# importing bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.layouts import gridplot
# from bokeh.sampledata.periodic_table import elements
# from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, WheelZoomTool
from bokeh.models.sources import ColumnDataSource
from bokeh.models.annotations import Span, BoxAnnotation
# from screeninfo import get_monitors
# import pandas as pd

x1, y1 = list(range(0,10)), list(range(10,20))
x2, y2 = list(range(20,30)), list(range(30,40))
x3, y3 = list(range(40,50)), list(range(50,60))

# Prepare the output file
output_file("grid_plot.html")

# Create a figure object
f1 = figure(width=250, height=250, title="Circles")
f1.circle(x=x1, y=y1, size=10, alpha=0.5, color='navy')

f2 = figure(width=250, height=250, title="Triangles")
f2.triangle(x=x2, y=y2, size=10, alpha=0.5, color='firebrick')

f3 = figure(width=250, height=250, title="Squares")
f3.square(x=x3, y=y3, size=10, alpha=0.5, color='olive')

# create a span (line) annotation
span_4 = Span(location=4, dimension='height', line_color='red', line_width=2)
f1.add_layout(span_4)

box_2_6 =BoxAnnotation(left=2, right=6, fill_color='firebrick', fill_alpha=0.3)
f1.add_layout(box_2_6)

# # Style the plot area
# f.plot_width = get_monitors()[0].width
# f.plot_height = get_monitors()[0].height-50
# #f.plot_width = 1800                       # Width of screen in pixels
# #f.plot_height = 900                       # Height of screen in pixels
# f.sizing_mode = "stretch_both"

# # Visual style the title
# f.title.text = "Periodic Table of the Elements"          # Title text
# f.xaxis.axis_label="Atomic Radius"               # x-axis label
# f.yaxis.axis_label="Boiling Point "                # y-axis lable

# # Set up different colours for different species
# elements.dropna(inplace=True)
# colormap = {'gas':'yellow', 'liquid':'orange', 'solid':'red'}
# elements['color'] = [colormap[x] for x in elements['standard state']]
# elements['size'] = elements['van der Waals radius']/10

# # Set up bokeh column data sources
# gas    = ColumnDataSource(elements[elements['standard state']=='gas'])
# liquid = ColumnDataSource(elements[elements['standard state']=='liquid'])
# solid  = ColumnDataSource(elements[elements['standard state']=='solid'])

# # See https://docs.bokeh.org/en/latest/docs/reference/plotting.html

# f.circle(x='atomic radius', y='boiling point', size='size', fill_alpha=0.2, color='color', legend_label='Gas', source=gas)
# f.circle(x='atomic radius', y='boiling point', size='size', fill_alpha=0.2, color='color', legend_label='Liquid', source=liquid)
# f.circle(x='atomic radius', y='boiling point', size='size', fill_alpha=0.2, color='color', legend_label='Solid', source=solid)

# Write the plot in the figure object
f = gridplot([[f1,f2],[None,f3]])                 # 2 x 2
#f = gridplot([[f1],[f2],[f3]])                    # Column
#f = gridplot([[f1,f2,f3]])                        # Row
show(f)                                            # Show completed figure