"""
setosa
https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg/800px-Kosaciec_szczecinkowaty_Iris_setosa.jpg

versicolor
https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Blue_Flag%2C_Ottawa.jpg/800px-Blue_Flag%2C_Ottawa.jpg

virginica
https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Iris_virginica.jpg/800px-Iris_virginica.jpg
"""
# Making a basic Bokeh line graph

# importing bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show, save, curdoc
# import pandas as pd
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, WheelZoomTool
from bokeh.models.sources import ColumnDataSource
from screeninfo import get_monitors

# Prepare the output file
output_file("iris2.html")

# Create a figure object
f = figure()

# Style the available tools
f.tools = [PanTool(), ResetTool()]        # Define items in toolbat
f.add_tools(WheelZoomTool())              # Add additional item to toolbar
#f.add_tools(HoverTool())                 # Add additional item to toolbar
f.toolbar_location = "above"              # Determine location for toolbar
#f.toolbar.logo = None                     # Turn off bokeh logo
# hover = HoverTool(tooltips=[("Species","@species"), ("Sepal Width","@sepal_width")])
hover = HoverTool(tooltips="""
    <div>
        <div>
            <img
                src="@imgs" height="82" alt="@imgs" width = "82"
                style="float: left; margin: 0px 15px 15px 0px;"
                border="2"
            ></img>
        </div>
        <div>
            <span style="font-size: 18px; font-weight: bold;">@species</span>
        </div>
        <div>
            <span style="font-size: 12px; color: #696;">Petal length: @petal_length</span>
            <span style="font-size: 12px; color: #696;">Petal width: @petal_width</span>
        </div>
    </div>
""")
f.add_tools(hover)                        # Add additional item to toolbar

# Style the plot area
f.plot_width = get_monitors()[0].width
f.plot_height = get_monitors()[0].height-50
#f.plot_width = 1800                       # Width of screen in pixels
#f.plot_height = 900                       # Height of screen in pixels

f.background_fill_color="olive"         # Colour of background
f.background_fill_alpha = 0.3             # Transparency of background
# f.border_fill_color = "red"             # Colour of border / background
f.sizing_mode = "stretch_both"

# Visual style the title
f.title.text = "IRIS MORPHOLOGY"          # Title text
f.title.text_color = "red"                # Text / font colour
f.title.text_font = "verdana"             # Font type
f.title.text_font_size = "25px"           # Text / font size
f.title.align = "center"                  # Location of title

# Visual style the plot axes
# f.axis.minor_tick_line_color = "blue"         # 
# f.xaxis.minor_tick_line_color = "blue"        # 
# f.yaxis.minor_tick_line_color = "red"         # 
# f.yaxis.minor_tick_line_color = None          # 
f.xaxis.major_label_orientation = "horizontal"  # 
f.yaxis.major_label_orientation = "horizontal"  # 
f.xaxis.visible = True                          # 
#f.xaxis.minor_tick_in = 6                       # 
#f.xaxis.minor_tick_out = 10                     # 
f.xaxis.axis_label="Petal Length"               # x-axis label
f.yaxis.axis_label="Petal Width"                # y-axis lable
f.axis.axis_label_text_color="blue"             # Define both axes label colour
f.axis.major_label_text_color="orange"          # Define both axes major label (numbering) colour

# Axes geometry
# f.x_range = Range1d(start=0, end=10, bounds = (3,5)) # Limit action of panning tool
f.x_range = Range1d(start=0, end=7)            # 
f.y_range = Range1d(start=0, end=3)             # 
#f.xaxis.bounds = (2, 5)                         # 
#f.yaxis.bounds = (2, 4)                         # 
#f.xaxis[0].ticker.desired_num_ticks = 2         # 
#f.yaxis[0].ticker.desired_num_ticks = 2         # 
#f.yaxis[0].ticker.num_minor_ticks = 10          # 

# Style the grid
# f.xgrid.grid_line_color = "gray"              # Define line colour for x-axis
# f.xgrid.grid_line_color = None                # Define line colour for x-axis
# f.ygrid.grid_line_color = "gray"              # Define line colour for y-axis
f.grid.grid_line_color = "gray"                 # Define line colour for both axes
f.grid.grid_line_alpha = 0.95                   # Define line transparency for both axes
f.grid.grid_line_dash = [5, 3]                  # Define dash line ratio in pixels for both axes

# Set up different colours for different species
colormap = {'setosa':'red', 'versicolor':'green', 'virginica':'blue'}
flowers['color'] = [colormap[x] for x in flowers['species']]
# flowers['size'] = flowers['sepal_width']*flowers['sepal_width']
flowers['size'] = flowers['sepal_width']*4
urlmap = {'setosa':'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg/800px-Kosaciec_szczecinkowaty_Iris_setosa.jpg',
          'versicolor':'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Blue_Flag%2C_Ottawa.jpg/800px-Blue_Flag%2C_Ottawa.jpg',
          'virginica':'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Iris_virginica.jpg/800px-Iris_virginica.jpg'}
flowers['imgs'] = [urlmap[x] for x in flowers['species']]

# Set up bokeh column data sources
setosa     = ColumnDataSource(flowers[flowers['species']=='setosa'])
versicolor = ColumnDataSource(flowers[flowers['species']=='versicolor'])
virginica  = ColumnDataSource(flowers[flowers['species']=='virginica'])

# See https://docs.bokeh.org/en/latest/docs/reference/plotting.html

f.circle(x='petal_length', y='petal_width', size='size', fill_alpha=0.2, color='color', legend_label='Setosa', source=setosa)
f.circle(x='petal_length', y='petal_width', size='size', fill_alpha=0.2, color='color', legend_label='Versicolour', source=versicolor)
f.circle(x='petal_length', y='petal_width', size='size', fill_alpha=0.2, color='color', legend_label='Virginica', source=virginica)

# Style the legend
f.legend.location = "top_left"                     # Location in text
# f.legend.location = [77, 555]                    # Location in pixels
f.legend.background_fill_color = "pink"
f.legend.background_fill_alpha = 0.3
f.legend.border_line_color = None
f.legend.margin = 10
f.legend.padding = 10
f.legend.label_text_color = "olive"
f.legend.label_text_font = "verdana"
f.legend.label_text_font_size = "15px"

# Write the plot in the figure object
show(f)                                            # Show completed figure