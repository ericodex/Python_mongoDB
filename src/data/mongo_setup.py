import mongoengine as me # MongoEngine é igual a me

def global_init():
    ''' Registro e definição do alias e nome da base de dados '''
    me.register_connection(alias='core', name='snake_bnb')
