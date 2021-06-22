# from __future__ import absolute_import
 
# from bokeh.io import save, show
# from bokeh.models import Plot, Range1d, LabelSet, LinearAxis, ColumnDataSource
 
# #import pytest
# #pytestmark = pytest.mark.integration
 
# HEIGHT = 600
# WIDTH = 600
 
 
# #@pytest.mark.screenshot
# def test_label_set(output_file_url, selenium, screenshot):
 
#     source = ColumnDataSource(data=dict(text=['one', 'two', 'three'],
#                                         x1=[1,4,7],
#                                         x2=[60,240,420]))
 
#     # Have to specify x/y range as labels aren't included in the plot area solver
#     plot.Plot(plot_height=HEIGHT, plot_width=WIDTH,
#                 x_range=Range1d(0, 10), y_range=Range1d(0, 10),
#                 toolbar_location=None)
 
#     label_set1 = LabelSet(x='x1', y=2, x_offset=25, y_offset=25,
#                           text="text", source=source,
#                           text_font_size='38pt', text_color='red', text_alpha=0.9,
#                           text_baseline='bottom', text_align='left',
#                           background_fill_color='green', background_fill_alpha=0.2,
#                           angle=15, angle_units='deg',
#                           render_mode='canvas')
 
#     label_set2 = LabelSet(x='x2', y=4, x_units='screen', x_offset=25, y_offset=25,
#                           text="text", source=source,
#                           text_font_size='38pt', text_color='red', text_alpha=0.9,
#                           text_baseline='bottom', text_align='left',
#                           background_fill_color='green', background_fill_alpha=0.2,
#                           angle=15, angle_units='deg',
#                           render_mode='css')
 
#     plot.add_layout(LinearAxis(), 'below')
#     plot.add_layout(LinearAxis(), 'left')
 
#     plot.add_layout(label_set1)
#     plot.add_layout(label_set2)
 
#     # Save the plot and start the test
#     #save(plot)
#     show(plot)
#     #selenium.get(output_file_url)
 
#     # Take screenshot
#     # assert screenshot.is_valid()

from bokeh.palettes import PuBu
from bokeh.io import show, output_notebook
from bokeh.models import ColumnDataSource, ranges, LabelSet
from bokeh.plotting import figure
#output_notebook()

source = ColumnDataSource(dict(x=['Áætlaðir','Unnir'],y=[576,608]))

x_label = ""
y_label = "Tímar (klst)"
title = "Tímar; núllti til þriðji sprettur."
plot = figure(plot_width=600, plot_height=300, tools="save",
        x_axis_label = x_label,
        y_axis_label = y_label,
        title=title,
        x_minor_ticks=2,
        x_range = source.data["x"],
        y_range= ranges.Range1d(start=0,end=700))


labels = LabelSet(x='x', y='y', y_units='screen', text='y', level='glyph',
        x_offset=-13.5, y_offset=0, source=source, render_mode='css')

plot.vbar(source=source,x='x',top='y',bottom=0,width=0.3,color=PuBu[7][2])

plot.add_layout(labels)
show(plot)