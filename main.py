from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/ferrari')
def ferrari():
    return render_template('ferrari.html')

@app.route('/porsche')
def porsche():
    return render_template('porsche.html')

@app.route('/bmw')
def bmw():
    return render_template('bmw.html')

if __name__ == '__main__':
    app.run(debug=True)