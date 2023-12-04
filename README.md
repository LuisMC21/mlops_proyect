<h1 align="center">PROYECTO INDIVIDUAL Nº1</h1>

## Descripción del proyecto

El proyecto consta de un análisis exploratorio de datos de películas, crear una API para acceder a información sobre películas y entrenar un modelo de recomendación basado en similitud de géneros.

## Archivos incluidos en el repositorio

1. Carpeta data: Se encuentran todos los archivos csv ya transformados y listos para usar en las funciones.
2. Archivo proyecto.ipynb: Contiene el código con las transformaciones desarrrolladas en los datasets.
3. Archivo main.py: Incluye el código con la creación de funciones para la API.
4. Archivo análisisSent.ipynb: Incluye el código realizado para hacer un análisis de sentimientos de los comentarios de los usuarios.
5. Archivo recomendacion.ipynb: Incluye el código realizado para hacer un sistema de recomendación según los géneros de los juegos.
6. Archivo requirements.txt: Inlcuye las librerías que deben instalarse para el proyecto.

Datasets originales se encuentran en el siguiente link: <a href="https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj">https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj</a>
   
## Funciones desarrolladas en la API

1. **userdata(User_id: str):** Debe devolver cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items.

2. **countreviews(YYYY-MM-DD y YYYY-MM-DD: str):** Cantidad de usuarios que realizaron reviews entre las fechas dadas y, el porcentaje de recomendación de los mismos en base a reviews.recommend.

3. **genre(género: str):** Devuelve el puesto en el que se encuentra un género sobre el ranking de los mismos analizado bajo la columna PlayTimeForever.

4. **userforgenre(género: str):** Top 5 de usuarios con más horas de juego en el género dado, con su URL (del user) y user_id.

5. **developer(desarrollador: str):** Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.

6. **sentiment_analysis( año : int ):** Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
   
7. **def recomendacion_juego( id de producto ):** Ingresando el id del juego, retorna una lista de 5 juegos recomendados similares al ingresado.

## Deploy del proyecto

   En el archivo main.py incluye las funciones para la API, para la cual se usó la librería FastAPI (<a href="https://fastapi.tiangolo.com/">https://fastapi.tiangolo.com/</a>) y como      servidor se usó la plataforma Render (<a href="https://render.com/">https://render.com/</a>)

## Link del proyecto

   <h2><a href="https://mlops-proyect-t1ab.onrender.com/docs">https://mlops-proyect-t1ab.onrender.com/docs</a></h2>
   
