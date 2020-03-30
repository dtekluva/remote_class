from my_db_functions import *

confirmed_file_name = "C:/Users/INYANG/Desktop/class online/dhammey/My_covid_data/timeseriescovid19confirmedglobal.csv"
death_file_name = "C:/Users/INYANG/Desktop/class online/dhammey/My_covid_data/timeseriescovid19deathsglobal.csv"
recovery_file_name = "C:/Users/INYANG/Desktop/class online/dhammey/My_covid_data/timeseriescovid19recoveredglobalnarrow.csv"
countries_of_choice = ['Nigeria','Italy','Switzerland','Iran', 'US']


for country in countries_of_choice:

    confirmed_file = open(confirmed_file_name, "r")
    death_file = open(death_file_name, "r")
    recovery_file = open(recovery_file_name, "r")
    
    heading = confirmed_file.readlines(1)

    # for line in recovery_file.readlines():
    #     country_recovery_data = line.split(",")

        # if country_recovery_data[1] == country:
        #     data_recoveries = country_recovery_data[5:]
        #     break
    
    for country_death in death_file.readlines():
        death_data = country_death.split(",")

        if death_data[1] == country:
            number_of_deaths = death_data[4:]
            break

    for country_cases in confirmed_file.readlines():
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

            for cases, deaths, date in list(zip(number_of_cases, number_of_deaths, heading[0].split(",")[4:])):
                # pass
                # print(data)
                recoveries = 0 #ASSUMING RECOVERIES IS ZERO TO AVOID MORE WORK
                write_case(country_exists[0]['id'], cases, deaths, recoveries, format_time(date))

        else:
            write_country(country_name, lat, lng)