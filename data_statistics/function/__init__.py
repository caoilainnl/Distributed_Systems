import logging
import pymssql
import azure.functions as func
import json

DB_CONFIG = {
  "server": 'dist_systems-simulated_data-data_statistics-automated_processing.database.windows.net',
  "user": 'caoilainnl',
  "password": 'C@mpl3xS3rv!ce2025',
  "database": 'dist_systems'
}


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        conn = pymssql.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                sensor_id,
                MIN(temperature) AS min_temp,
                MAX(temperature) AS max_temp,
                AVG(temperature) AS avg_temp
            FROM sensor_data
            GROUP BY sensor_id
        """)
        rows = cursor.fetchall()

        stats = [{
            'sensor_id': row[0],
            'min_temp': row[1],
            'max_temp': row[2],
            'avg_temp': row[3]
        } for row in rows]

        return func.HttpResponse(json.dumps(stats), status_code=200, mimetype="application/json")
    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse("Failed to retrieve statistics.", status_code=500)
    finally:
        if 'conn' in locals():
            conn.close()
