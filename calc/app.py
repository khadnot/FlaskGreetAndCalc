from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def to_add():
    """Add a and b params."""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)

    return str(result)

@app.route('/sub')
def to_sub():
    """Substract a and b params."""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)

    return str(result)

@app.route('/mult')
def to_mult():
    """Multiply a and b params."""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)

    return str(result)

@app.route('/div')
def to_div():
    """Divide a and b params."""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)

    return str(result)

### All IN ONE FUNCTION

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
    }

@app.route('/math/<operator>')
def to_calc(operator):
    """Calculate a and b params."""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operators[operator](a, b)

    return str(result)
