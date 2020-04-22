import pymysql.cursors

#  Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='my_covid19',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def create_tables():
    with connection.cursor() as Cursor:
        
        create_countries_table = "create table IF NOT EXISTS countries (id int(10) AUTO_INCREMENT PRIMARY KEY NOT NULL, name VARCHAR(100), lng float, lat float)"

        Cursor.execute(create_countries_table)

        create_cases_table = "CREATE table IF NOT EXISTS country_data (id int(10) AUTO_INCREMENT PRIMARY KEY NOT NULL , country_id INT(10), FOREIGN KEY (country_id) REFERENCES countries(id), number_of_cases INT(100), number_of_deaths INT(100), number_of_recoveries INT(100), `date` DATE)"

        Cursor.execute(create_cases_table)
        
        connection.commit()


def write_country(name, lat, lng):

    with connection.cursor() as Cursor:
        
        add_country = f"INSERT INTO countries (name, lat, lng) values('{name}','{lat}','{lng}')"

        Cursor.execute(add_country)
        
        connection.commit()

def write_country_data (country_id, number_of_cases, number_of_deaths, number_of_recoveries, date):

    with connection.cursor() as Cursor:
        
        add_case = f"INSERT INTO country_data (country_id, number_of_cases, number_of_deaths, number_of_recoveries, date) values('{country_id}','{number_of_cases}','{number_of_deaths}', '{number_of_recoveries}', '{date}')"

        Cursor.execute(add_case)
        
        connection.commit()

def check_country(name):
    with connection.cursor() as Cursor:
        
        get_country = f"SELECT * FROM countries where name = '{name}'"

        Cursor.execute(get_country)
        
        return Cursor.fetchall()   

        
def format_time(date):
    
    "1/22/20" # before split
    month, day, year = date.split("/") #["1","22", "20"] #after split
   
    fixed_date = "-".join([year.replace('\n','')+'20', month, day]) #20+20 ==== 2020
    "2020-1-22"
    return fixed_date


create_tables()