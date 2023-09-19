import pandas as pd
from fastapi import FastAPI
import numpy as np

app = FastAPI()

@app.get("/userdata/{user_id}")
def userdata(user_id):
    
    df_user_reviews_final = pd.read_csv("data/df_user_reviews_final.csv")
    df_user_items_final = pd.read_csv("data/df_user_items_final.csv")
    df_steam_games_copy = pd.read_csv("data/df_steam_games_final.csv")

    df_user_items_id = df_user_items_final[df_user_items_final['user_id']==user_id]['item_id']
    respuesta = ''
    
    items = df_user_items_id.values
    precios =  []
    for i in items:
        precio = df_steam_games_copy[df_steam_games_copy['id']== i]['price2']
        if not precio.empty:
            precios.append(precio.values[0])

    df_user_reviews_id = df_user_reviews_final[df_user_reviews_final['user_id']==user_id]['recommend']

    j = 0
    for i in df_user_reviews_id.values:
        if(i == True):
            j = j + 1

    recomendacion = j/len(df_user_reviews_id.values)*100

    precios_np = np.array(precios)
    precios_np.sum()

    item_count = int(df_user_items_final[df_user_items_final['user_id']=='js41637']['items_count'].iloc[0])

    respuesta = {'recomendación:': recomendacion, 
                'Cantidad de dinero:' : precios_np.sum(), 
                'Cantidad de items': item_count}
    
    return respuesta

@app.get("/genre/{genero}")
async def genre(genero: str):
    df = pd.read_csv('data/rankgenres.csv')
    df = df[df['genero'] == genero]
    respuesta = ''
    if(len(df)==0):
        respuesta = 'Genero no existe'
    else:
        rank = int(df['Rank'].values[0]) 
        respuesta = {"Género": genero, "Rank": rank}

    return respuesta

@app.get("/developer/{developer}")
def developer(developer: str):
    df_developer = pd.read_csv('data/developerByAño.csv')
    df_developer = df_developer[df_developer['developer']==developer]

    if(len(df_developer)==0):
        respuesta = 'No hay developer con ese nombre'
    else:
        respuesta = df_developer.to_dict(orient='records')

    return respuesta

@app.get("/contreviews/{fecha1}/{fecha2}")
def countreviews(fecha1: str, fecha2: str):
    df_user_reviews_final = pd.read_csv("data/df_user_reviews_final.csv")

    df_user_fechas=df_user_reviews_final[['user_id']][df_user_reviews_final['fecha']
                                                  .between(fecha1, fecha2)].value_counts()
                                                  
    primeros_valores = df_user_fechas.index.get_level_values('user_id').tolist()

    recomendaciones = []
    for i in primeros_valores:
        recomendacion = (userdata(i)[list(userdata(i).keys())[0]])
        recomendaciones.append(recomendacion)
    
    respuesta = {'usuario': primeros_valores, 'recomendación':recomendaciones}

    df = pd.DataFrame(respuesta)

    respuesta = df.to_dict(orient='records')

    return respuesta


@app.get("/userforgenre/{genre}")
def userforgenre(genre: str):

    df_steam_games_copy = pd.read_csv("data/df_steam_games_final.csv")
    df_user_items_final = pd.read_csv("data/df_user_items_final.csv")

    df_steam_games_copy_dropna = df_steam_games_copy.dropna(subset=['genres'])

    df_steam_games_copy_generos = df_steam_games_copy_dropna[df_steam_games_copy_dropna['genres']
                                                      .apply(lambda generos: genre in generos)]

    juegos = df_steam_games_copy_generos['id'].values
    df_user_items_final_genres = df_user_items_final[df_user_items_final['item_id'].isin(juegos)]

    df_top_users = df_user_items_final_genres[['user_id','user_url', 'playtime_forever']].groupby(['user_id', 'user_url']).sum('playtime_forever')

    df_top_users_reset = df_top_users.reset_index().head(5)

    respuesta = df_top_users_reset.to_dict(orient='records')
    
    return respuesta

@app.get("/sentiment_analysis/{anio}")
def sentiment_analysis(anio : int):
    df_user_reviews = pd.read_csv('data/df_user_reviews_sentimientos.csv')
    df_steam_games = pd.read_csv('data/df_steam_games_final.csv')

    juegos = df_steam_games[df_steam_games['Año']==anio]['id'].to_list()

    df_user_reviews_filtrado = df_user_reviews[df_user_reviews['item_id'].isin(juegos)]
    conteo_sentimientos = df_user_reviews_filtrado['Sentimiento'].value_counts()

    # Crear un diccionario personalizado
    diccionario_conteo = {
        'Negative': int(conteo_sentimientos.loc['negativo']),
        'Neutral': int(conteo_sentimientos.loc['neutral']),
        'Positive': int(conteo_sentimientos.loc['positivo'])
    }

    return diccionario_conteo