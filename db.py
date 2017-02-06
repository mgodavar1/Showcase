db = DAL("sqlite://storage.sqlite")

db.define_table('user',
                Field('name', unique=True),
                Field('email'),
                Field('phone'),
                format = '%(name)s')

db.define_table('project',
                Field('user_id', 'reference user'),
                Field('title'),
                Field('description'))

#User validators
db.user.name.requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, db.user.name)]
db.user.email.requires = [IS_NOT_EMPTY(), IS_EMAIL(error_message='Please enter a valid email!')]
db.user.phone.requires = IS_MATCH('^1?((-)\d{3}-?|\(\d{3}\))\d{3}-?\d{4}$',
         error_message='Please enter in form 1-123-456-7899')

#Project validators
db.project.title.requires = IS_NOT_EMPTY()
db.project.description.requires = IS_NOT_EMPTY()


db.post.user_id.writable = db.post.user_id.readable = False
