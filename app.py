from flask import Flask,request
from flask_restful import Resource, Api
import random

app = Flask(__name__)
api = Api(app)

class parameter(Resource):
    def get(self):
        type = request.args.get('typ')
        if type==None or type=='':  # Parameter is not specified
         return f'Podanie typu jest wymagane.'
        if(type!='parzyste' and type!='nieparzyste'):  # The specified parameter is incorrect
         return 'Parametr typ musi miec wartosc parzyste lub nieparzyste.'
        else:
         if type == 'parzyste':
            return str(random.randrange(0,101,2))  # Generates a pseudo-random even number
         else:
           return str(random.randrange(1,100,2))  # Generates a pseudo-random odd number

api.add_resource(parameter, '/losowa_liczba')
 
if __name__ == '__main__':
    app.run(debug=True)
