from flask import Flask, render_template, request

app = Flask(__name__, template_folder="template")


@app.route('/')
def index():
    return render_template('calculator.html')


@app.route('/calc', methods=['POST'])
def calc():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operator = request.form['operator']
        result = ""
        if operator == 'add':
            result = num1 + num2
        elif operator == 'subtract':
            result = num1 - num2
        elif operator == 'multiply':
            result = num1 * num2
        elif operator == 'divide':
            result = num1 / num2
        else:
            result = 'Invalid operator'
    except ZeroDivisionError:
        result = 'You cant divide on zero osyol!'

    return render_template('calculator.html', result=result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
