#imports
from peewee import *
import datetime

#blog posts database using peewee sqlite


#db = SqliteDatabase('posts.db')
#entries db with two test entries
db = SqliteDatabase('entries.sql')

class Post(Model):
	id = PrimaryKeyField()
	#date will be presented at the point of submission to database so date will be truely representitive of actual submission
	date = DateTimeField(default = datetime.datetime.now)
	#could have unique=true titles may add feature in future but need to add warnings at time of creation to avoid post being lost, not essencial
	#need to set max lengths for titles and posts and prevent null/empty entries
	title = CharField()
	#text field for the post being exponentially larger
	text = TextField()
	#text field for the post being exponentially larger
	content = TextField()
	#specifies the db created
	class Meta:
		database = db


#initialise the blog database to connect and create the post table
def initialise_db():
	db.connect()
	db.create_tables([Post], safe=True)
	
