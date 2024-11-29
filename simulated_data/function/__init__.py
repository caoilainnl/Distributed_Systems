import logging
import pymssql
import azure.functions as func

DB_CONFIG = {
    'server': 'dist_systems-simulated_data-data_statistics-automated_processing.database.windows.net',
    'user': 'caoilainnl',
    'password': 'C@mpl3xS3rv!ce2025',
    'database': 'dist_systems'
}


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()

        conn = pymssql.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO sensor_data (sensor_id, temperature, wind_speed, humidity, co2_level, timestamp)
            VALUES (%s, %s, %s, %s, %s, GETDATE())
        """, (data['sensor_id'], data['temperature'], data['wind_speed'], data['humidity'], data['co2_level']))
        conn.commit()

        return func.HttpResponse("Data inserted successfully!", status_code=200)
    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse("Failed to insert data.", status_code=500)
    finally:
        if 'conn' in locals():
            conn.close()
