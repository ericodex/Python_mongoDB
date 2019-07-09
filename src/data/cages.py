import datetime # Date time, otimização do uso de unidade de tempo no banco de dados.
import mongoengine as me

from data.bookings import Booking

class Cage(me.Document): 
    ''' Estruturação de definição de propriedade do objeto Cage '''
    registered_date = me.DateTimeField(default=datetime.datetime.now)

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    square_meters = me.FloatField(required=True)
    is_carpeted = me.BooleanField(required=True)
    has_toys = me.BooleanField(required=True)
    allow_dangerous_snakes = me.BooleanField(default=False)

    bookings = me.EmbeddedDocumentListField(Booking)

    meta = { 
        'db_alias': 'core',
        'collection': 'cages'
    }
