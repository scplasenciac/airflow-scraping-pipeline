# Airflow Scraping Pipeline

Este proyecto implementa un **pipeline de scraping con Apache Airflow**.  
El DAG `scraping_carga` extrae citas y autores desde [quotes.toscrape.com](https://quotes.toscrape.com), guarda los datos en un archivo CSV y registra mensajes de confirmación en los logs.

## Tecnologías usadas
- [Apache Airflow](https://airflow.apache.org/) para la orquestación de tareas.
- [Python](https://www.python.org/) como lenguaje principal.
- [Requests](https://docs.python-requests.org/) para realizar la petición HTTP.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) para parsear HTML.
- [Pandas](https://pandas.pydata.org/) para manipulación y exportación de datos.

## Estructura del proyecto
```airflow-scraping-pipeline/
│
├── dags/
│   └── scraping_carga.py
├── requirements.txt
└── README.md
