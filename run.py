from zaneapi import create_app
#from config import Config
Config = {'OAUTH2_CLIENT_ID': 793100907403411508}
app = create_app(Config)

if __name__ == "__main__":
    app.run("0.0.0.0", port=80)
