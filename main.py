from flask import Flask, render_template, request, session
from datetime import datetime
import random

app = Flask(__name__)
a = datetime.today().strftime("%Y%m%d%H") 
print (a)
app.secret_key = a

def generate_problem(max, max2):
    num1 = random.randint(1, max)
    num2 = random.randint(1, max2)
    if max > 10:
        operator = random.choice(['+', '-', '*', '/'])
    else:
        operator = random.choice(['+', '-'])
    sik = f"{num1} {operator} {num2}"
    return sik

def verify_problem(user_answer, user_answer2, nowtime_sik):
    try:
        num1, operator, num2 = nowtime_sik.split()
        num1 = int(num1)
        num2 = int(num2)
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '÷':
            result = num1 // num2
            result2 = num1 % num2
        elif operator == '*':
            result = num1 * num2

        if operator != "÷":
            if int(user_answer) == result:
                result = "정답입니다!"  
                return result

            else:
                result = "NONE"
                return result
        else:
            if int(user_answer) == result:
                if int(user_answer2) == result2:
                    result = "정답입니다!"
                    return render_template(f'result.html', result=result)                 
                
    except Exception as e:
        typed_answer = request.form['answer']
        sik = request.form['sik']
        print (e)

        num1, operator, num2 = request.form['sik'].split()
        return render_template('problem_1.html', sik=sik)

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
    try:
        correct_count = session['correct_count']
    except:
        correct_count = 0

    sik = generate_problem(9, 9)

    return render_template('problem_1.html', sik=sik, correct_count=correct_count)

@app.route('/problem_4')
def problem_4(): 
    try:
        correct_count = session['correct_count']
    except:
        correct_count = 0

    sik = generate_problem(9999, 9999)

    return render_template('problem_4.html', sik=sik, correct_count=correct_count)


@app.route('/problem_money')
def problem_money():  
    return render_template('problem_money.html')


@app.route('/check_p1', methods=['post'])
def check1_p1():
    try:
        result = verify_problem(request.form['answer'], 0, request.form['sik'])
        sik = request.form['sik']
        print(f"이용자의 답안: {request.form['answer']}, 주어진 식: {request.form['sik']}")
        if result == "정답입니다!":
            session['correct_count'] = session.get('correct_count', 0) + 1
            correct_count = session['correct_count']
            print (session['correct_count'])
            return render_template('problem_1.html', sik=sik, correct_count=correct_count)
        else:
            return render_template('problem_1_fail.html', sik=sik)
                
    except Exception as e:
        sik = request.form['sik']
        print (e)
        return render_template('problem_1.html', sik=sik)

if __name__ == '__main__':
    app.run(debug=True)
