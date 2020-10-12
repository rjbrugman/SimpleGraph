from django.shortcuts import render
from GraphApp.forms import GraphInputForm

from plotly.offline import plot
from plotly.graph_objs import Scatter, Layout

import numpy as np
# Create your views here.


def hello_world(request):
    return render(request, 'GraphApp/hello.html', {})

def graph_input(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GraphInputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            x_coefficient = int(form['x_coefficient'].value()) # seems that int format from model only used when saved to db
            x_exponent = int(form['x_exponent'].value())
            c_constant = int(form['c_constant'].value())

            x2_coefficient = int(form['x2_coefficient'].value())
            x2_exponent = int(form['x2_exponent'].value())
            c2_constant = int(form['c2_constant'].value())

            return graph_view(request,x_coefficient, x_exponent, c_constant,x2_coefficient, x2_exponent, c2_constant)
            # return render(request, 'GraphApp/graphInput.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GraphInputForm()
    return render(request, 'GraphApp/graphInput.html', {'form': form})

def graph_view(request, x_coef=1, x_exp=1, c_const=1, x2_coef=1, x2_exp=1, c2_const=1):

    x_data = np.arange(-10.05,10.05,0.1)
    y_data = [x_coef*x**x_exp + c_const for x in x_data]
    y2_data = [x2_coef * x ** x2_exp + c2_const for x in x_data]
    # plot_div = plot([Scatter(x=x_data, y=y_data,
    #                     mode='lines', name='test',
    #                     opacity=0.8, marker_color='green')],
    #            output_type='div')
    trace1 = Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')
    trace2 = Scatter(x=x_data, y=y2_data,
                     mode='lines', name='test2',
                     opacity=0.8, marker_color='red')
    plot_div = plot({"data":[trace1, trace2]}, output_type='div')

    # trace1 = Scatter(x=[1, 2, 3, 4], y=[0, 2, 3, 5], showlegend=True, marker=dict(color='rgb(128, 0, 0)', ),
    #                  name='Trace_1', fill='tozeroy')
    # trace2 = Scatter(x=[1, 2, 3, 4], y=[3, 5, 1, 7], showlegend=True, marker=dict(color='rgb(0, 128, 0)', ),
    #                  name='Trace_2', fill='tonexty')

    # Create chart
    # Output will be stored as a html file.
    # Whenever we will open output html file, one popup option will ask us about if want to save it in jpeg format.
    # Font family can be used in a layout to define font type, font size and font color for title
    # plotly.offline.plot({
    #     "data": [
    #         trace1, trace2
    #     ],
    #     "layout": Layout(title="Area Chart", font=dict(family='Courier New, monospace', size=18, color='rgb(0,0,0)'))
    # }, filename='Area_chart.html', image='jpeg')

    return render(request, "GraphApp/graphView.html", context={'plot_div': plot_div, 'x_coef': x_coef, 'x_exp': x_exp, 'c_const': c_const,
                                                               'x2_coef': x2_coef, 'x2_exp': x2_exp, 'c2_const': c2_const})

