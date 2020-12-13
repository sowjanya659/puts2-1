from flask import Flask, request
from fractions import Fraction
import json
import statistics
import decimal
from decimal import Decimal

app = Flask(__name__)

@app.route('/')
def index():

    if request.method == 'GET':
        value1 = request.args.get('X', default=0, type=str)

    else:
        value1 = request.values.get('X', default=0, type=str)
    try:
        value1 = [Fraction(value) for value in value1.split(',')]
    except ValueError:
        error = "please enter proper input"
        return error

    return value1


@app.route('/min')#as per requiremet
def minimum():
    try:
        value1 = index()
        result = min(value1)#takes minimum value
    except ValueError:
        error = index()
        return error
    else:
        if float(result).is_integer():
            answer = int(result)
            return "%d" % result
        return str(float(round(result)))#displays output in the form of 1.0

if __name__ == "__main__":
    app.run()

