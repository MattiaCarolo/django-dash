from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
# Create your views here.
import datetime
import numpy as np


def home(request):
    def scatter():
        np.random.seed(1)

        programmers = ['Alex','Nicole','Sara','Etienne','Chelsea','Jody','Marianne']

        base = datetime.datetime.today()
        dates = base - np.arange(180) * datetime.timedelta(days=1)
        z = np.random.poisson(size=(len(programmers), len(dates)))

        fig = go.Figure(data=go.Heatmap(
                z=z,
                x=dates,
                y=programmers,
                colorscale='Viridis'))

        fig.update_layout(
            title='GitHub commits per day',
            xaxis_nticks=36)

        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context ={
        'plot1': scatter()
    }

    return render(request, 'home/welcome.html', context)