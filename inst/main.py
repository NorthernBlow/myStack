from instagrapi import Client
from os import environ
from os.path import join, dirname
from dotenv import load_dotenv



dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


cl = Client()
cl.delay_range = [1, 3]

before_ip = cl._send_public_request("https://api.ipify.org/")
cl.set_proxy("http://<api_key>:wifi;ca;;;toronto@proxy.soax.com:9137")
after_ip = cl._send_public_request("https://api.ipify.org/")
print(f"Before (before_ip)")
print(f"After (after_ip)")


cl.login(eviron.get('ACCOUNT_USERNAME'), eviron.get('ACCOUNT_PASSWORD'))
cl.dump_settings("session.json")

user_id = cl.user_id_from_username(environ.get('ACCOUNT_USERNAME')
medias = cl.user_medias(user_id, 20)
