
from atproto import Client
import json

def main():
    client=Client()

    try:
        client.login('roinelperez.bsky.social','lhj5-tnbz-o7xq-36hn')
        termino_busq='#cuba'
        respuesta=client.app.bsky.feed.search_posts({'term':termino_busq, 'limit':25})

        posts=respuesta.posts

        for post in posts:
            print(post)

    except Exception as e:
        print("Error: ", e)
        return


if __name__=="__main__":
    main()