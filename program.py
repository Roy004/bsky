from atproto import Client
import json

def main():
    client=Client()

    try:
        client.login('roinelperez.bsky.social','lhj5-tnbz-o7xq-36hn')
        termino_busq='#cuba'
        respuesta=client.app.bsky.feed.search_posts({'q':termino_busq, 'limit':25})

        posts=respuesta.model_config

        print(posts)
        exit()
        posts_lista=[]
        for post in posts:
            posts_lista.append(post.model_dump())

        with open('datos.json','w',encoding='utf-8') as archivo:
            json.dump(posts_lista, archivo, ensure_ascii=False, indent=4)

        

    except Exception as e:
        print("Error: ", e)
        return


if __name__=="__main__":
    main()