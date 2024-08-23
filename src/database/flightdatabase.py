import mysql.connector
from src.logger.logging import logging
from src.exception.exception import CustomExcepttion
import sys

class Database:
    def __init__(self, host: str, user: str, password: str):
        self.host = host
        self.user = user
        self.password = password
        self.conn = None
        self.mycursor = None

    def databaseConnection(self):
        try:
            logging.info("Initiating connection to the database server...")
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            self.mycursor = self.conn.cursor()
            logging.info("Successfully connected to the database server.")
        except Exception as e:
            raise CustomExcepttion(e, sys)

    def useDatabase(self, databasename: str):
        if self.conn is None:
            logging.error("Failed to use the database as the connection has not been established.")
            return
        try:
            logging.info(f"Switching to database '{databasename}'...")
            self.conn.database = databasename
            logging.info(f"Now using database '{databasename}'.")
        except Exception as e:
            raise CustomExcepttion(e, sys)

    def closeConnection(self):
        if self.conn:
            logging.info("Closing the database connection...")
            self.conn.close()
            logging.info("Database connection closed successfully.")
            
    def fetch_city_names(self):
        try:
            self.mycursor.execute("""
            SELECT DISTINCT Destination FROM flights.flight
            UNION
            SELECT DISTINCT Source FROM flights.flight
            """)
            data = self.mycursor.fetchall()
            city = [item[0] for item in data]
            return city
        except Exception as e:
            raise CustomExcepttion(e, sys)
        
    def fetch_all_flights(self, source, destination):
        try:
            query = """
            SELECT Airline, Dep_Time, Duration, Price FROM flights.flight
            WHERE Source = %s AND Destination = %s
            """
            logging.info(f"Executing query: {query} with source={source} and destination={destination}")
            self.mycursor.execute(query, (source, destination))
            data = self.mycursor.fetchall()
            return data
        except Exception as e:
            raise CustomExcepttion(e, sys)
        
        
    def fetch_airline_frequency(self):
        try:
            airline = []
            frequency = []
            query = """
            SELECT Airline, COUNT(*) FROM flights.flight
            GROUP BY Airline
            """
            self.mycursor.execute(query)
            data = self.mycursor.fetchall()
            
            for item in data:
                airline.append(item[0])
                frequency.append(item[1])
            return airline,frequency
        except Exception as e:
            raise CustomExcepttion(e,sys)
        
    def busy_airport(self):
        try:
            city = []
            frequency = []
            query = """
            SELECT Source, COUNT(*) as freq
            FROM (
                SELECT Source FROM flights.flight
                UNION ALL
                SELECT Destination FROM flights.flight
            ) t
            GROUP BY Source
            ORDER BY freq DESC
            """
            self.mycursor.execute(query)
            data = self.mycursor.fetchall()
            
            for item in data:
                city.append(item[0])
                frequency.append(item[1])
            
            return city, frequency
            
        except Exception as e:
            raise CustomExcepttion(e, sys)
