import simplexml
from flask import request,make_response, Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app, default_mediatype='application/json')

@api.representation('application/xml')
def xml(data, code, headers=None):
    resp = make_response(simplexml.core.dumps({'response': data}), code)
    resp.headers.extend(headers or {})
    return resp



class dump(Resource):
    def get(self):
        attrib=request.args.get('attrib1',type=int)
        return {'result':attrib**2}
      
    
   


api.add_resource(dump, '/square') 



