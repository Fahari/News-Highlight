import os
class Config:
    SOURCE_API_BASE_URL ='https://newsapi.org/v2/sources?category={}&apiKey={}'



class ProdConfig(Config):
    pass


class DevConfig(Config):

    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}
