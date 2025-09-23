from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def first():
    return "<h3>Welcome To Flask Tutorial Pease write the Age of the preson in the url like this /age/20</h3>"

    
@app.route("/age/<int:age>")
def age(age):
    if age >=    18:
        return render_template("eligible.html", age=age)
    else:
        return render_template("noteligible.html", age=age)

if __name__ == "__main__":
    app.run(debug=True)