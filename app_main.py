from flask import Flask, render_template

app = Flask(__name__)

# Route for the main page (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Route for the Home page (home.html)
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/attack-simulator')
def attack():
    return render_template('Simulator.html')

@app.route('/vulnerable-scanner')
def vulnerable():
    return render_template('vulnerability.html')

@app.route('/gamify-learning')
def gamify():
    return render_template('gamify.html')

@app.route('/algorithm-visualizer')
def visualizer():
    return render_template('visualizer.html')

if __name__ == '__main__':
    app.run(debug=True)
