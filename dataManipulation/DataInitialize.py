import pandas as pd
import json
import pycountry

with open('data.json') as json_data:
    data = json.load(json_data)

# Data
MainData = pd.DataFrame(data['data'])
MainData = MainData[['cc', 'lc', 'unique', 'so', 'created']]


# Data manipulation


MainData['created'] = pd.to_datetime(MainData['created'], errors='coerce')

ChoroplethData = MainData[['cc', 'unique']]
ChoroplethData.dropna(subset=['cc'])
ChoroplethData.reset_index(drop=True, inplace=True)
ChoroplethData = ChoroplethData.groupby(['cc'], as_index=False).count()

BarChartData = MainData.resample('M', on='created').count()
BarChartData.reset_index(inplace=True)
BarChartData = BarChartData[['created', 'unique']]

LineChartData = MainData[['created', 'unique']]
LineChartData['hour'] = LineChartData['created'].dt.hour
LineChartData.drop(columns=['created'], inplace=True)
LineChartData.sort_values(by=['hour'], inplace=True)
LineChartData = LineChartData.groupby(['hour'], as_index=False).count()


contryName = []
for i in range(len(ChoroplethData)):
    x1 = pycountry.countries.get(alpha_2=ChoroplethData['cc'][i])
    if x1 != None:
        ChoroplethData.replace({'cc': ChoroplethData['cc'][i]}, x1.alpha_3,
                               inplace=True)
        contryName.append(x1.name)
    else:
        ChoroplethData.drop(i, inplace=True)

ChoroplethData['countryName'] = contryName

SunBurstData = ChoroplethData.groupby(['countryName', 'unique'],
                                      as_index=False).sum()
# Data for sunburst graph (country, add advertising

print(ChoroplethData)