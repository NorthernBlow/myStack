from hikerapi import Client
import socks
import socket




proxy_type = socks.SOCKS5
proxy_host = 'localhost'
proxy_port = 1337

socks.set_default_proxy(proxy_type, proxy_host, proxy_port)

socket.socket = socks.socksocket
cl = Client(token="AICzps7doHr9eACOjgD15meap99R6ylL")

def get_followers(cl, user_id):
    followers = {}
    followers_len = -1
    end_cursor = None
    while len(followers) > followers_len:
        followers_len = len(followers)
        res, end_cursor = cl.user_followers_chunk_gql(user_id=user_id, end_cursor=end_cursor)
        followers.update({item['pk']:item for item in res})
    return list(followers.values())

followers = get_followers(cl, "1726342880")

print(followers)
