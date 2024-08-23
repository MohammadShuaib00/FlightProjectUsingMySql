import sys
from src.exception.exception import CustomExcepttion
from src.logger.logging import logging
from src.database.flightdatabase import Database
import plotly.graph_objects as go
import streamlit as st
import plotly.express as px
import pandas as pd

class AnalyticGraph:
    def __init__(self, db: Database):
        self.db = db

    def plot_airline_frequency(self):
        try:
            airline, frequency = self.db.fetch_airline_frequency()
            fig = go.Figure(data=[go.Pie(
                labels=airline,
                values=frequency,
                hole=.3,
                textinfo='label+percent',
                textfont=dict(size=20),
                insidetextorientation='radial'
            )])

            fig.update_layout(
                title_text="Airline Frequency Distribution",
                title_font_size=24,
                width=800,
                height=600,
                autosize=False,
            )

            st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            logging.error("Error occurred while plotting airline frequency.")
            raise CustomExcepttion(e, sys)

    def plot_busy_airports(self):
        try:
            # Fetch data
            city, frequency = self.db.busy_airport()

            # Debugging: Print the lengths and contents of the data
            logging.info(f"Number of cities: {len(city)}, Number of frequencies: {len(frequency)}")
            logging.info(f"Cities: {city}")
            logging.info(f"Frequencies: {frequency}")

            # Check if lengths match
            if len(city) != len(frequency):
                raise ValueError("Length of 'city' and 'frequency' must be the same.")

            # Convert to DataFrame for better compatibility with Plotly Express
            df = pd.DataFrame({
                'City': city,
                'Frequency': frequency
            })

            # Generate unique colors for each bar
            color_palette = px.colors.qualitative.Plotly
            df['Color'] = [color_palette[i % len(color_palette)] for i in range(len(df))]

            # Plotting with different colors for each bar
            fig = px.bar(
                df,
                x='City',
                y='Frequency',
                color='Color',  # Use the color column
                labels={'City': 'City', 'Frequency': 'Frequency'},
                title='Busy Airports',
                color_discrete_sequence=df['Color']  # Use the color sequence
            )
            st.plotly_chart(fig, theme='streamlit', use_container_width=True)
            
        except Exception as e:
            logging.error(f"Error occurred while plotting busy airports: {str(e)}")
            raise CustomExcepttion(e, sys)