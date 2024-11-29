import pymssql
import logging


def main(input: str) -> None:
    try:
        conn = pymssql.connect(
          server='dist_systems-simulated_data-data_statistics-automated_processing.database.windows.net',
          user='caoilainnl',
          password='C@mpl3xS3rv!ce2025',
          database='dist_systems'
        )
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                sensor_id,
                MIN(temperature),
                MAX(temperature),
                AVG(temperature)
            FROM sensor_data
            GROUP BY sensor_id
        """)
        stats = cursor.fetchall()
        for row in stats:
            logging.info(
                f"Sensor {row[0]}: Min={row[1]}, Max={row[2]}, Avg={row[3]}"
            )
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
