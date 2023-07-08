from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/overview/")
def overview():
    return render_template('overview.html')

@app.route("/todos/")
def todos():
    return render_template('todos.html')

if __name__ == "__main__":
    app.run(debug=True)