import mongoengine as me

class Booking(me.EmbeddedDocument):
    guest_owner_id = me.ObjectIdField()
    guest_snake_id = me.ObjectIdField()

    booked_date = me.DateTimeField()
    check_in_date = me.DateTimeField(required=True)
    check_out_date = me.DateTimeField(required=True)

    review = me.StringField()
    rating = me.IntField(default=0)

    @property   # Definição de expressão como propriedade da estrutura da classe 
    def duration_in_days(self):
        dt = self.check_out_date - self.check_in_date
        return dt.days
