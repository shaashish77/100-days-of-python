# # with open("weather-data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
# # with open("weather-data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
import pandas

#
# data = pandas.read_csv("weather-data.csv")
# # print(data)
# # print(type(data))
# # print(data["temp"])
# # data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = (data["temp"].to_list())
# # average_temp = sum(temp_list) / len(temp_list)
# # print(average_temp)
# #
# # print(data["temp"].mean())
# # print(data["temp"].max())
#
# # get data from a column
# # print(data.condition)
#
# # get data in row
# #  print(data[data.day == "Sunday"])
# # print(data.temp.max())
# print(data[data.temp == data.temp.max()])

data = pandas.read_csv("004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
grey_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
grey_black = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel)
print(grey_cinnamon)
print(grey_black)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_black, grey_cinnamon, grey_squirrel]
}
df = pandas.DataFrame(data_dict)
df.to_csv("Square_count_csv")

