from flask import Flask, request
import random
app = Flask(__name__)


@app.route("/losowa_liczba")
def parameter():
    type = request.args.get('typ')

    # Parameter is not specified
    if(type is None or type == ''):
        return f'Podanie typu jest wymagane.'

    # The specified parameter is incorrect
    if(type != 'parzyste' and type != 'nieparzyste'):
        return f'Parametr "typ" musi mieć wartość \
        "parzyste" lub "nieparzyste".'
    else:
        if type == 'parzyste':
            return str(random.randrange(0, 101, 2))
        else:
            return str(random.randrange(1, 100, 2))


if __name__ == '__main__':
    app.run(debug=False)
