import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset 
df = pd.read_csv('data/Cleaned_ObesityDataSet_raw_and_data_sinthetic.csv')

# Selecting relevant features
features = list(df.columns)
df = df[features]

numerical_cols = df.select_dtypes(['float64', 'int64']).columns
categorical_cols = df.select_dtypes(['object']).columns[:-1]
# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server  # For deployment

# Define app layout
app.layout = html.Div([
    html.H1("Obesity Levels Dashboard", style={'textAlign': 'center', 'fontWeight': 'bold', 'fontSize': 30}),
    
    # Dropdown for selecting a feature
    html.Label("Select a Feature to Visualize Against Obesity Level:", style={'fontWeight': 'bold'}),
    dcc.Dropdown(
        id='feature-dropdown',
        options=[{'label': col, 'value': col} for col in features if col != 'NObeyesdad'],
        value='Age',
        clearable=False
    ),
    
    dcc.Graph(id='visualization-output'),
])

# Define callback to update graph
@app.callback(
    Output('visualization-output', 'figure'),
    Input('feature-dropdown', 'value')
)
def update_graph(selected_feature):
    if selected_feature in numerical_cols:#['Age', 'Height', 'Weight', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE', 'CALC']:
        fig = px.box(df, x='NObeyesdad', y=selected_feature, color='NObeyesdad',
                     title=f'Distribution of {selected_feature} Across Obesity Levels')
    else:
        fig = px.histogram(df, x=selected_feature, color='NObeyesdad', barmode='group',
                           title=f'{selected_feature} Distribution by Obesity Level')

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
