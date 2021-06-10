from zaneapi import create_app
#from config import Config
Config = {'OAUTH2_CLIENT_ID': '793100907403411508', 'OAUTH2_CALLBACK_URL': 'https://gaming-links.herokuapp.com/callback', 'OAUTH2_CLIENT_SECRET': 'Z-YbaXlSnplgcGwpiitq4YFt-Qf3S2ZM'}
app = create_app(Config)

if __name__ == "__main__":
    app.run("0.0.0.0", port=80)
