# FINAL_CASTILLO_TEJADA_ROSA
Este proyecto contiene un pipeline ETL con Python integrado a Jenkins y GitHub para automatizar el procesamiento de datos.

## Funcionalidad
- Lee un archivo CSV (`input.csv`) con valores de productos.
- Calcula el IGV (18%) y el total.
- Clasifica los productos en bajo, medio o alto según su valor.
- Genera un archivo `output.csv` con los resultados.

## Tecnologías usadas
- Python (pandas)
- Docker
- Jenkins
- Git y GitHub

## Cómo ejecutar el ETL
```bash
python3 etl.py
