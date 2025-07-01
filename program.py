from atproto import Client

client=Client()

client.login('roinelperez.bsky.social','vagsZa5r')

post = client.send_post('Este es un post enviado con python!')

