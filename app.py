from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])

def calculate():
    expression = request.form['expression']
    
    try:
        result = eval(expression)
        return render_template('index.html', result=result)
    except (SyntaxError, TypeError):
        error_message = "Invalid expression"
        return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
