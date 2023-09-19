<h1 align="center">PROYECTO INDIVIDUAL Nº1</h1>

## Funciones desarrolladas en la API

Archivos incluidos en el positorio

1. Carpeta data: Se encuentran todos los archivos csv ya transformados y listos para usar en las funciones.
2. Archivo main.py: Incluye el código de las transformaciones realizadas y el desarrollo de las funciones.
3. Archivo análisisSent.ipynb: Incluye el código realizado para hacer un análisis de sentimientos de los comentarios de los usuarios.
4. Archivo requirements.txt: Inlcuye las librerías que deben instalarse para el proyecto.
   
## Funciones desarrolladas en la API

1. **userdata(User_id: str):** Debe devolver cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items.

2. **countreviews(YYYY-MM-DD y YYYY-MM-DD: str):** Cantidad de usuarios que realizaron reviews entre las fechas dadas y, el porcentaje de recomendación de los mismos en base a reviews.recommend.

3. **genre(género: str):** Devuelve el puesto en el que se encuentra un género sobre el ranking de los mismos analizado bajo la columna PlayTimeForever.

4. **userforgenre(género: str):** Top 5 de usuarios con más horas de juego en el género dado, con su URL (del user) y user_id.

5. **developer(desarrollador: str):** Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.

6. **sentiment_analysis( año : int ):** Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
