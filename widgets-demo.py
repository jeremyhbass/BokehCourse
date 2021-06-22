# Import bokeh modules
# from bokeh.io import output_file, show
from bokeh.io import curdoc
from bokeh.models.widgets import TextInput, Button, Paragraph
from bokeh.layouts import layout

# output_file("widget_demo.html")

text_input = TextInput(value="Enter name:")
button = Button(label="Generate text")
output = Paragraph()

def update():
    output.text = "Hello, " + text_input.value

button.on_click(update)

layoutx = layout([[button, text_input], [output]])

# show(layoutx)
curdoc().add_root(layoutx)