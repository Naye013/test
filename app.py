import altair as alt
import dash
from dash import dcc as dcc
from dash import html as html
from vega_datasets import data

cars = data.cars()
brush = alt.selection_interval()
chart = (alt.Chart(cars).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color=alt.condition(brush, 'Origin', alt.value('lightgray')))
.add_params(brush))

app = dash.Dash(__name__)
app.layout = html.Div([
        html.Iframe(
            srcDoc=chart.to_html(),
            style={'border-width': '0', 'width': '100%', 'height': '400px'})])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
