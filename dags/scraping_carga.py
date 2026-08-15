from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

def scrape_data():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = [q.text for q in soup.find_all("span", class_="text")]
    authors = [a.text for a in soup.find_all("small", class_="author")]
    df = pd.DataFrame({"quote": quotes, "author": authors})

    # Ruta de salida en tu escritorio de Windows
    output_path = "/mnt/c/Users/Sebas/Desktop/quotes.csv"
    df.to_csv(output_path, index=False)

    # Mensajes de confirmación en los logs
    logging.info(f"Archivo CSV creado en {output_path}")
    print(f"Archivo CSV creado en {output_path}")
    print(df.head())

with DAG(
    dag_id="scraping_carga",
    start_date=datetime(2023, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    scrape_task = PythonOperator(
        task_id="scrape",
        python_callable=scrape_data,
    )
