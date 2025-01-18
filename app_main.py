from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Define the steps for each attack simulation
MITM_STEPS = [
    {"title": "Intercept Communication", "description": "The attacker positions themselves between two parties, intercepting messages."},
    {"title": "Alter Message", "description": "The attacker modifies the intercepted message before forwarding it."},
    {"title": "Relay Modified Message", "description": "The attacker sends the modified message to the intended recipient."},
]

REPLAY_STEPS = [
    {"title": "Capture Original Message", "description": "The attacker captures a legitimate message during a valid session."},
    {"title": "Replay Message", "description": "The attacker reuses the captured message to gain unauthorized access or perform actions."},
]

DOS_STEPS = [
    {"title": "Send Excessive Requests", "description": "The attacker floods the server with a large number of requests."},
    {"title": "Overload Resources", "description": "The server resources are consumed, leading to denial of service for legitimate users."},
]

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

# Route for MITM attack simulation
@app.route('/mitm_attack')
def mitm_attack():
    return jsonify({
        "attack": "Man-in-the-Middle (MITM) Attack",
        "steps": MITM_STEPS
    })

# Route for Replay attack simulation
@app.route('/replay_attack')
def replay_attack():
    return jsonify({
        "attack": "Replay Attack",
        "steps": REPLAY_STEPS
    })

# Route for DoS attack simulation
@app.route('/dos_attack')
def dos_attack():
    return jsonify({
        "attack": "Denial of Service (DoS) Attack",
        "steps": DOS_STEPS
    })


if __name__ == '__main__':
    app.run(debug=True)