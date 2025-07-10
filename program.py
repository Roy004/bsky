from atproto import Client
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json
from collections import Counter


client=Client()

def main():

    try:
        client.login('roinelperez.bsky.social','lhj5-tnbz-o7xq-36hn')
    except Exception as e:
        print("Error: ", e)
        return

def buscar_posts_palabras_clave(palabras_clave:list,limite=50):
    resultados=[]

    for palabra in palabras_clave:
        respuesta=client.app.bsky.feed.search_posts({'q':palabra, 'limit':limite})

        posts=respuesta.posts

        for post in posts:
            resultados.append(post.model_dump())

    return resultados

# if __name__=="__main__":
#     main()

def obtener_datos_json(archivo:str):
    with open(archivo, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
    
    
    
def contar_publicaciones_autor(handle_autor, fuente_datos:str='datos.json'):
    '''
    Permite contar la cantidad de publicaciones para un autor
    
    '''
    
    data= obtener_datos_json(fuente_datos)
    cont=0
    for d in data:
        autor=d.get('author',{})

        handle=autor.get('handle',{})

        if(handle==handle_autor):
            cont+=1

    return cont


es=Elasticsearch("localhost:9200")

with open('datos.json') as f:
    datos=json.load(f)

actions=[
    {
        "_index":
    }
]

result=es.index(index='indice_bsky',body=datos)

print(f'Estado: {result}')