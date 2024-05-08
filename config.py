from flask import Flask
from flask_caching import Cache
from dotenv import dotenv_values


config = dotenv_values('.env')
app = Flask(__name__)
app.config['CACHE_TYPE'] = config['CACHE_TYPE']
app.config['CACHE_REDIS_HOST'] = config['CACHE_REDIS_HOST']
app.config['CACHE_REDIS_PORT'] = config['CACHE_REDIS_PORT']
app.config['CACHE_REDIS_DB'] = config['CACHE_REDIS_DB']
app.config['CACHE_REDIS_URL'] = config['CACHE_REDIS_URL']
app.config['CACHE_DEFAULT_TIMEOUT'] = config['CACHE_DEFAULT_TIMEOUT']
cache = Cache(app)
