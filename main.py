from flask import Flask, request
from fractions import Fraction
import json, statistics
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
        error = "Please enter proper input"
        return error

    return value1
@app.route('/average')#to support all three functions
@app.route('/mean')
@app.route('/avg')
def mean():
    try:
        value1 = index()
        result = statistics.mean(value1)
    except ValueError:
        error = index()
        return error
    else:
        if float(result).is_integer():
            result = int(result)
            return result
        return str(float(result))#display the solution in float i.e. in the form of 1.0


if __name__ == "__main__":
    app.run()

