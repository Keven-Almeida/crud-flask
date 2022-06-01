"""
flask SECRET_KEY generator.
"""
import secrets

CONFIG_STRING = """
DEBUG=True
SECRET_KEY=%s
HOST=127.0.0.1
PORT=5000
""".strip() % secrets.token_urlsafe(50)



# Writing our configuration file to '.env'
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)