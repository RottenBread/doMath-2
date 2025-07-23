from flask import Flask, render_template, request, session
import random

app = Flask(__name__)

def generate_problem():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*', '/'])

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    else:
        num2 = random.randint(1, 10)
        result = round(num1 / num2, 2)

    problem = f"{num1} {operator} {num2}"
    return problem, result

@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        correct_count = session['correct_count']
    except:
        correct_count = 0

    problem, result = generate_problem()
    answer = result if request.method == 'POST' else None
    return render_template("index.html", problem=problem, answer=answer, correct_count=correct_count)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/problem_1')
def problem_1():
    operator = random.choice(['+', '-'])
    
    try:
        correct_count = session['correct_count']
    except:
        correct_count = 0

    if operator == '+':
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)

    elif operator == '-':
        num1 = random.randint(3, 9)
        num2 = random.randint(2, num1)
        if num1 == num2:
            num2 = num2 - 1

    sik = f"{num1} {operator} {num2}"

    return render_template('problem_1.html', sik=sik, correct_count=correct_count)

@app.route('/problem_4')
def problem_4():  
    operator = random.choice(['+', '-'])
    
    try:
        correct_count = session['correct_count']
    except:
        correct_count = 0

    if operator == '+':
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)

    elif operator == '-':
        num1 = random.randint(3, 9)
        num2 = random.randint(2, num1)
        if num1 == num2:
            num2 = num2 - 1

    sik = f"{num1} {operator} {num2}"

    return render_template('problem_1.html', sik=sik, correct_count=correct_count)
    return render_template('problem_4.html')


@app.route('/problem_money')
def problem_money():  
    return render_template('problem_money.html')


@app.route('/check_p1', methods=['post'])
def check1_p1():
    try:
        typed_answer = request.form['answer']
        sik = request.form['sik']

        num1, operator, num2 = request.form['sik'].split()
        num1 = int(num1)
        num2 = int(num2)
        if operator == '+':
            result = num1 + num2

        elif operator == '-':
            result = num1 - num2

        if operator != "÷":
            if int(typed_answer) == result:
                result = "정답입니다!"
                session['correct_count'] = session.get('correct_count', 0) + 1

                correct_count = session['correct_count']

                print (session['correct_count'])
                return render_template('result.html', result=result, correct_count=correct_count)

            else:
                return render_template('problem_1.html', sik=sik, result=result)
                
    except Exception as e:
        typed_answer = request.form['answer']
        sik = request.form['sik']
        print (e)

        num1, operator, num2 = request.form['sik'].split()
        return render_template('problem_1.html', sik=sik)

if __name__ == '__main__':
    app.run(debug=True)