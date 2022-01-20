from flask import Flask,request
app = Flask(__name__)

@app.route("/losowa_liczba")
def parameter():
 type = request.args.get('typ')
 if(type==None or type==''):  # Parameter is not specified
     return f'Podanie typu jest wymagane.'
 if(type!='parzyste' and type!='nieparzyste'):  # The specified parameter is incorrect
     return f'Podany typ jest niepoprawny.'
 else:
       if type is 'parzyste':
           return type # Code goes here
       else:
           return type # Code goes here
    


if __name__ == '__main__':
    app.run(debug=True)
