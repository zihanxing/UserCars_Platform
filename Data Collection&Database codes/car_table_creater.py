#create car
import mysql.connector
connection = mysql.connector.connect (host = "172.16.199.140",
                                user = "1930026136", # use your username
                                passwd = "dsbaoganren",# use your password
                                db = "test")  # specify the database
cursor = connection.cursor()
cursor.execute ("DROP TABLE IF EXISTS car1")
sql_command = """
CREATE TABLE car1 ( 
carID INTEGER PRIMARY KEY, 
brand VARCHAR(20), 
model VARCHAR(30),
volume FLOAT,
gearbox VARCHAR(20),
original_price FLOAT,
price FLOAT, 
year INTEGER,
age INTEGER,
mileage FLOAT,
horsepower INTEGER,
torque INTEGER,
transfer_number INTEGER,
fuel FLOAT,
image VARCHAR(200)
);"""
cursor.execute(sql_command)