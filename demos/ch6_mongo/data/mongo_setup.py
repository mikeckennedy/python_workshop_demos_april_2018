import mongoengine


def init_mongo():
    mongoengine.register_connection('core', name='pypi2')
