from flask_restful import Api, Resource

class Index(Resource):

    def get(self):
        
        return {'hello':'world my apps'}

api = Api()

def configure_api(app):

    api.add_resource(Index,'/')

    api.init_app(app)