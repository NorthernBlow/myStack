from instagrapi import Client


cl = Client()
cl.login(USERNAME, PASSWORD)
cl.dump_settings("session.json")
