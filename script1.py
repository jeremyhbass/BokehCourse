# Making a basic bokeh graph

# import numpy as np
# import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show

# Create some data
x = [ 1, 2, 3, 4, 5]
y = [ 6, 7, 8, 9,10]

# Prepare the output file
output_file("test.html")

# Create a figure output
f = figure()

# Create a line plot
f.line(x,y)
# f.triangle(x,y)
# f.circle(x,y,)

# Now show the figure
show(f)