import datetime
import mongoengine as me

class Owner(me.Document):
    '''Classe que estrutura as propriedades de uma coleção.'''
    registered_date = me.DateTimeField(default=datetime.datetime.now)
    name = me.StringField(required=True) # Texto, obrigatório
    email = me.StringField(required=True) # Texto, obrigatório

    snake_ids = me.ListField() # lista
    cage_ids = me.ListField() # lista

    meta = { 
        'db_alias': 'core',
        'collection': 'owners'
    }
