from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")             #endpoint
@app.route("/home")
def home():
    return render_template("home.html") #looking for project/templates/home.html


@app.route("/digitSum/<int:number>")          #more meaningful example
def digitSum(number):   
    sum = 0
    while (digit := number%10):
        sum += digit
        number = number // 10         

    return f"<h1>The digit sum of the URL number is: {sum}</h1>"    


if __name__ == '__main__':
    app.run(debug=True, port=8080)