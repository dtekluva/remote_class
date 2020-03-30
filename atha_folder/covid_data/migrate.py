from db_funcs import *

file = open("C:/Users/inyang/Desktop/class online/covid_data/time_series_covid19.csv")
file = open("C:/Users/inyang/Desktop/class online/covid_data/time_series_covid19.csv")

countries_of_choice = ["Italy",'Jamaica','Japan','Jordan']
heading = file.readlines(1)

for line in file.readlines():
    line_data = line.split(",")
    country_name = line_data[1]

    if country_name in countries_of_choice:
        country_exists = check_country(country_name)
    #     # print(country_exists)

        if country_exists:

            for data in list(zip(line_data, heading[0].split(",")))[4:]:
                # print(format_time(data[1]), data[1])
                write_case(country_exists[0]['id'], format_time(data[1]),data[0] )

        else:
            write_country(country_name, line_data[2], line_data[3])



