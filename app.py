from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def home():
    return redirect("/overview")

@app.route("/overview/")
def overview():
    return render_template('overview.html')

@app.route("/todos/")
def todos():
    return render_template('todos.html')

@app.route("/calendar/")
def calendar():
    return render_template('calendar.html')

if __name__ == "__main__":
    app.run(debug=True)