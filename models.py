
import datetime
from peewee import *
DATABASE = SqliteDatabase('kids.sqlite') 

class Kid(Model):
	name = CharField() 
	age = IntegerField() 
	gender = CharField()
	created_at = DateTimeField(default=datetime.datetime.now) 

	class Meta:
		database = DATABASE 


def initialize(): 
	DATABASE.connect() 

	DATABASE.create_tables([Kid], safe=True)
	print("Connected to DB and created tables if they weren't already there")

	DATABASE.close()

