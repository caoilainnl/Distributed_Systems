import pymssql
import random
import logging
import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    try:
        conn = pymssql.connect(
          server='dist_systems-simulated_data-data_statistics-automated_processing.database.windows.net',
          user='caoilainnl',
          password='C@mpl3xS3rv!ce2025',
          database='dist_systems'
        )
        cursor = conn.cursor()

        for i in range(20):
            cursor.execute("""
                INSERT INTO sensor_data (sensor_id, temperature, wind_speed, humidity, co2_level, timestamp)
                VALUES (%d, %f, %f, %f, %d, GETDATE())
            """, (
                i + 1,  # Sensor ID
                random.uniform(15, 25),  # Temperature
                random.uniform(5, 15),  # Wind speed
                random.uniform(30, 70),  # Humidity
                random.randint(400, 1500)  # CO2 level
            ))
        conn.commit()
        logging.info("Data inserted successfully!")
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
