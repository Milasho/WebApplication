from flask import Flask,request
import random
app = Flask(__name__)

@app.route("/losowa_liczba")
def parameter():
 type = request.args.get('typ')
 if(type==None or type==''):  # Parameter is not specified
     return f'Podanie typu jest wymagane.'
 if(type!='parzyste' and type!='nieparzyste'):  # The specified parameter is incorrect
     return f'Parametr "typ" musi mieć wartość "parzyste" lub "nieparzyste".'
 else:
       if type == 'parzyste':
           return str(random.randrange(0,101,2))  # Generates a pseudo-random even number
       else:
           return str(random.randrange(1,100,2))  # Generates a pseudo-random odd number

if __name__ == '__main__':
    app.run(debug=False)
