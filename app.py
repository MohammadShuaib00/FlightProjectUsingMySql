import streamlit as st
import sys
from src.logger.logging import logging  
from src.exception.exception import CustomExcepttion
from src.database.flightdatabase import Database
from src.AnaylticsGraph.graph import AnalyticGraph 
import pandas as pd 
from src.description import ProjectDescription
# Initialize the database connection
db = Database("127.0.0.1", "root", "Shu@ib99")
db.databaseConnection()
db.useDatabase("flights")

# Initialize the AnalyticGraph with the existing database connection
analytics = AnalyticGraph(db)

# Logging for the Streamlit app start
logging.info("Streamlit app started successfully.")

# Sidebar menu for the Streamlit app
st.sidebar.title("Flights Analytics")
user_option = st.sidebar.selectbox('Menu', ['Select One', 'Check Flights', 'Analytics'])

try:
    logging.info(f"User selected option: {user_option}")
    
    # Respond to user selection
    if user_option == 'Check Flights':  
        st.title('Check Flights')
        col1, col2 = st.columns(2)
        city = db.fetch_city_names()
        with col1:
            source = st.selectbox('Source', sorted(city))
            
        with col2:
            destination = st.selectbox('Destination', sorted(city))
            
        if st.button('Search Flights'):
            results = db.fetch_all_flights(source, destination)
            if results:
                st.dataframe(pd.DataFrame(results, columns=['Airline', 'Dep_Time', 'Duration', 'Price']))
            else:
                st.write("No flights found.")
        
        logging.info("Navigated to 'Check Flights' section.")
    elif user_option == 'Analytics':
        st.title("Analytics")
        analytics.plot_airline_frequency()
        analytics.plot_busy_airports()
        logging.info("Navigated to 'Analytics' section.")
    else:
        st.title("Tell about the project")
        descrip = ProjectDescription()
        descrip.display()
        logging.info("Default selection: 'Tell about the project'.")
except Exception as e:
    logging.error("An error occurred in the Streamlit app.")
    raise CustomExcepttion(e, sys)
