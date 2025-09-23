from flask import Flask

app = Flask(__name__)

# 1. Basic Hello World
@app.route("/")
def hello():
    return "Hello, World!"


# 2. Reverse String
@app.route("/reverse/<string:text>")
def reverse_string(text):
    reversed_text = text[::-1]
    return f"Original: {text} | Reversed: {reversed_text}"


# 3. Armstrong Number Checker
@app.route("/check/<int:num>")
def check_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)

    if total == num:
        return f"{num} is an Armstrong number!"
    else:
        return f"{num} is NOT an Armstrong number."


if __name__ == "__main__":
    app.run(debug=True)