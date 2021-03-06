#Plotting flower species

#Importing libraries
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers
# from bokeh.models import Range1d, PanTool, ResetTool, HoverTool

#Define the output file path
output_file("iris.html")

#Create the figure object
f=figure()

#Style the plot area
f.plot_width=1800
f.plot_height=900
f.background_fill_color="olive"
f.background_fill_alpha=0.3

#Style the title
f.title.text="Iris Morphology"
f.title.text_color="olive"
f.title.text_font="Agency FB"
f.title.text_font_size="25px"
f.title.align="center"

#Style the axes
f.xaxis.minor_tick_line_color="blue"
f.yaxis.major_label_orientation="vertical"
f.xaxis.visible=True
f.xaxis.minor_tick_in=-6
f.xaxis.axis_label="Petal Length"
f.yaxis.axis_label="Petal Width"
f.axis.axis_label_text_color="blue"
f.axis.major_label_text_color="orange"

#Save and show the figure
show(f)
