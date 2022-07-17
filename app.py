from operator import truediv
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def creations():
    return render_template("coding.html")
@app.route("/aboutme")
def aboutme():
    return "<h1 style='color:aqua; background-color:black; display:inline; border-radius:10px;'>You know about me now.</h1>"

@app.route('/getlower')
def getlower():
    return render_template('lower.html')

@app.route('/lower')
def lower():
    string=request.args.get('user_string')
    result=string.lower()
    return render_template('lower.html',result=result)

@app.route('/getupper')
def getupper():
    return render_template("upper.html")
@app.route('/upper')
def upper():
    input=request.args.get('user_string')
    answer = input.upper()
    return render_template("upper.html", result=answer)

@app.route('/getmost')
def getmost():
    return render_template("most.html")
    
@app.route('/most')
def most():
    a = []
    number1 = int(request.args.get('user_integer1'))
    a.append(number1)
    number2 = int(request.args.get('user_integer2'))
    a.append(number2)
    number3 = int(request.args.get('user_integer3'))
    a.append(number3)
    b = max(a)
    return render_template("most.html", result=str(b))
@app.route('/getreverse')
def getreverse():
    return render_template("reverse.html")

@app.route('/reverse')
def reverse():
    string =  str(request.args.get("rev"))
    return render_template("reverse.html",result=string[::-1])
@app.route('/getinterest')
def getinterest():
    return render_template("interest.html")
@app.route('/interest')
def interest():
    a = float(request.args.get("principle"))
    b = float(request.args.get("rate"))
    c = float(request.args.get("time"))
    d = b*c + 1
    e = d*a
    return render_template('interest.html',result=str(e))
@app.route('/getbmi')
def getbmi():
    return render_template("bmi.html")
@app.route('/bmi')
def bmi():
    a = float(request.args.get("height"))
    b = float(request.args.get("weight"))
    w = b*703
    h = a**2
    bmi = w/h
    return render_template("bmi.html", result = str(bmi))
@app.route('/getcalc')
def getcalc():
    return render_template("calc.html")
@app.route('/calc')
def calc():
    a = request.args.get("operator")
    b =a.lower()
    c = float(request.args.get("num1"))
    d = float(request.args.get("num2"))
    e = 0
    if b == "add":
        e = c+d
    elif b == "subtract":
        e = c-d
    elif b == "multiply":
        e = c*d
    elif b == "div":
        if d ==0:
            return render_template("calc.html", result = "Don't, just plz don't")
        else:
            e = c/d
    return render_template("calc.html", result = str(e))
if __name__ == "__main__":
    app.run(debug=True)