from flask import Flask, render_template, request, redirect

app = Flask(__name__)

checkloan = []


@app.route('/')
def hello_world():  # put application's code here
    return render_template("form.html")


def check(loan, salary):
    checks = salary / (loan * 3)
    if checks >= 1:
        qualifys = "Your application has been approved"
    else:
        qualifys = "Your application has not been approved"
    return qualifys, checks


@app.route('/calc', methods=['POST', 'GET'])
def calc():
    if request.method == 'POST':

        loan = int(request.form['loan'])
        salary = int(request.form['salary'])
        qualify, checks = check(loan, salary)
        if loan:
            new = {
                "loan": loan,
                "salary": salary,
                "check": checks,
                "qualify": qualify
            }
            checkloan.append(new)
        return render_template("display.html", checkloan=checkloan)
    return redirect('/')


if __name__ == '__main__':
    app.run()
