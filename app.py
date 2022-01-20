from flask import Flask,request
app = Flask(__name__)

@app.route("/losowa_liczba")
def parameter():
 type = request.args.get('typ')
 if(type==None or type==''):  # Parameter is not specified
     return f'Podanie typu jest wymagane.'


if __name__ == '__main__':
    app.run(debug=True)
