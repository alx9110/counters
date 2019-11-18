"""Api"""
from flask_restful import Api
from smartcounters.resources.counters import Counter 


def register_resources(app, prefix):
    """
    Register API resources
    Args:
        app: flask application
        prefix: URL prefix for resources
    """

    api = Api(app, prefix=prefix)

    api.add_resource(
        Counter,
        '/counters',
    )