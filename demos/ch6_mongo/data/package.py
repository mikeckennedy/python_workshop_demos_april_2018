import datetime
import mongoengine


class Package(mongoengine.Document):
    name = mongoengine.StringField(required=True, unique=True)
    created = mongoengine.DateTimeField(default=datetime.datetime.now)
    maintainers = mongoengine.ListField(mongoengine.ObjectIdField())

    meta = {
        'collection': 'packages',
        'db_alias': 'core',
        'indexes': [
        ]
    }
