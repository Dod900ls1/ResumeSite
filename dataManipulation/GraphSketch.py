import plotly.express as px
import plotly
import json
import pandas as pd


class Sketch:
    def __init__(self, filename: str):
        self.filename = filename

    def SimpleDataGraph(self, ChartName: str, x: str, y: str):
        # In this function you can sketch graphs that need only two lists
        if not self.filename.endswith('.json'):
            self.filename = self.filename + ".json"

        with open(self.filename, 'r') as data_file:
            json_load = json.load(data_file)
        SimpleData = pd.DataFrame(json_load)

        fig = plotly.plot(SimpleData, x=x, y=y, kind=ChartName)
        return fig

    def ChoroplethGraph(self, locations, hover_name, color):  # Reading json file
        # Choropleth Graph
        if not self.filename.endswith('.json'):
            self.filename = self.filename + ".json"

        with open(self.filename, 'r') as data_file:  # Reading json file
            json_load = json.load(data_file)
        ChoroplethData = pd.DataFrame(json_load)

        fig = px.choropleth(ChoroplethData, locations=locations, hover_name=hover_name, color=color)
        return fig

    def SunburstGraph(self, path, values):
        if not self.filename.endswith('.json'):
            self.filename = self.filename + ".json"

        with open(self.filename, 'r') as data_file:  # Reading json file
            json_load = json.load(data_file)
        SunburstData = pd.DataFrame(json_load)

        fig = px.sunburst(SunburstData, path=path, values=values)
        return fig
