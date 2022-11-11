from Encoder import NpEncoder
from constants import *
from DataInitialize import *

if __name__ == "__main__":
    DateFormat = []  # Data for BarData.json file
    for i in BarChartData['created']:
        DateFormat.append(str(i.date()))  # convert time column to dd-mm-yyyy format
    BarChartData['created'] = DateFormat


    def ListsToWriteData(DataFrame) -> (list, list):  # Making tuple which include dataframe columns and dataframe data.
        columns = list(DataFrame.columns)
        col_data = [list(DataFrame[columns[i]]) for i in range(len(columns))]
        return columns, col_data


    def process_data(columns: list, data_columns: list):
        return dict(zip(columns, data_columns))  # making dictionary


    sample1 = process_data(ListsToWriteData(ChoroplethData)[0], ListsToWriteData(ChoroplethData)[1])
    sample2 = process_data(ListsToWriteData(SunBurstData)[0], ListsToWriteData(SunBurstData)[1])
    sample3 = process_data(ListsToWriteData(BarChartData)[0], ListsToWriteData(BarChartData)[1])
    sample4 = process_data(ListsToWriteData(LineChartData)[0], ListsToWriteData(LineChartData)[1])


    def CreateJsonFile(filename: str, DictForCreate: dict):
        with open(f'{filename}.json', 'w') as fp:
            json.dump(DictForCreate, fp=fp, cls=NpEncoder)


    CreateJsonFile(ChoroplethName, sample1)

    CreateJsonFile(SunburstName, sample2)

    CreateJsonFile(BarName, sample3)

    CreateJsonFile(LinearName, sample4)