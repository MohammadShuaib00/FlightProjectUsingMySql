import streamlit as st

class ProjectDescription:
    @staticmethod
    def display():
        st.title("Project Description")
        st.write("""
        Welcome to the **Flights Analytics** project!

        This application is designed to help users explore and analyze flight data. It provides two main functionalities:

        **1. Check Flights:** 
        - This section allows users to search for flights between different cities. Users can select a source city and a destination city from the available options. The application will then display a list of flights that match the selected criteria, including details such as airline, departure time, duration, and price.

        **2. Analytics:**
        - In this section, you can perform various types of data analysis on the flight data. This could include visualizations, statistical analysis, or other forms of data exploration to gain insights into flight patterns, pricing trends, or other relevant metrics.

        **Key Features:**
        - **Dynamic City Selection:** Choose from a list of cities based on the available flight data.
        - **Flight Search:** Get a detailed view of flights between selected cities with essential details.
        - **Data Analysis:** Explore and analyze flight data to uncover insights.

        **Technologies Used:**
        - **Database:** MySQL for storing and retrieving flight data.
        - **Backend:** Python with the `mysql-connector` library for database interactions.
        - **Frontend:** Streamlit for creating an interactive and user-friendly web application.
        - **Logging and Error Handling:** Custom logging and exception handling to track application performance and troubleshoot issues.

        Feel free to explore the features of the application and analyze flight data to make informed decisions or gain insights into flight trends. If you have any questions or feedback, please let us know!
        """)
