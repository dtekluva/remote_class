from my_db_functions import *

countries_of_choice = ['Nigeria','Italy','Switzerland','Iran', 'US']

for country in countries_of_choice:
    file1 = open("C:/Users/BABATOLA/Documents/Pandemic period/My_covid19/My_covid_data/time_series_covid19_confirmed_global.csv")
    file2 = open("C:/Users/BABATOLA/Documents/Pandemic period/My_covid19/My_covid_data/time_series_covid19_deaths_global.csv")
    file3 = open("C:/Users/BABATOLA/Documents/Pandemic period/My_covid19/My_covid_data/time_series_covid19_recovered_global.csv")

    heading = file1.readlines(1)
    for country_recovered in file3.readlines():
        recovered_data = country_recovered.split(",")
        if recovered_data[1] == country:
            number_of_recoveries = recovered_data[4:] 
            break

    for country_death in file2.readlines():
        death_data = country_death.split(",")
        if death_data[1] == country:
            number_of_deaths = death_data[4:]
            break

    for country_cases in file1.readlines():
        cases_data = country_cases.split(",")
        if cases_data[1] == country:
            number_of_cases = cases_data[4:] 
            break

    country_name = country
    lat = cases_data[2]
    lng = cases_data[3]

    if country_name == country:
        country_exists = check_country(country_name)
        if country_exists:
            for data in list(zip(number_of_cases, number_of_deaths, number_of_recoveries, heading[0].split(",")[4:])):
                write_country_data(country_exists[0]['id'], data[0], data[1], data[2], format_time(data[3]))

        else:
            write_country(country_name, lat, lng)




