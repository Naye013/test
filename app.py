import dash
from dash import html

myapp = dash.Dash()
server = myapp.server

myapp.layout = html.Div(
    html.H1(children="Hello World")
)

if __name__=="__main__":
    myapp.run_server(host='0.0.0.0', port=8050, debug=True)
