from flask import Flask, render_template, jsonify, request
import RSA
import AES
import AffineCipher

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

# RSA Route
@app.route("/rsa", methods=["GET"])
def rsa():
    p = RSA.generate_large_prime()
    q = RSA.generate_large_prime()
    while p == q:
        q = RSA.generate_large_prime()
    auto = request.args.get("auto", type=bool)  # Query parameter
    if not auto:
        p = int(request.args.get("p"))
        q = int(request.args.get("q"))
    public_key, private_key, n, phi, d, e = RSA.generate_keys(p, q)
    plaintext = request.args.get("plaintext")
    ciphertext = RSA.encrypt(public_key, plaintext)
    decrypted_text = RSA.decrypt(private_key, ciphertext)
    data = {
        "p": p,
        "q": q,
        "n": n,
        "phi": phi,
        "d": d,
        "e": e,
        "public_key": public_key,
        "private_key": private_key,
        "ciphertext": ciphertext,
        "decrypted_text": decrypted_text,
        "plaintext": plaintext
    }
    response = {
        "success": True,
        "data": data,
    }
    return jsonify(response), 200

# AES Route
# AES Route
@app.route("/aes", methods=["GET"])
def aes():
    key = request.args.get("key")  # Get the key
    message = request.args.get("plaintext")  # Get the message
    aes128 = AES.AES()
    encryption_result = aes128.encrypt(key, message)
    ciphertext = encryption_result['encrypted']
    decryption_result = aes128.decrypt(key, ciphertext)
    data = {
        "key": key,
        "message": message,
        "ciphertext": ciphertext,
        "encryption_result": encryption_result['encryption_details'],
        "decryption_result": decryption_result['decryption_details'],
        "decrypted": decryption_result['decrypted'],
    }
    response = {
        "success": True,
        "data": data,
    }
    return jsonify(response), 200

# AffineCipher Route
@app.route("/affinecipher", methods=["GET"])
def affine_cipher():
    a, b = 5, 11
    plaintext = request.args.get("plaintext")
    encrypted_text, encryption_steps = AffineCipher.affine_encrypt(plaintext, a, b)
    decrypted_text, decryption_steps = AffineCipher.affine_decrypt(encrypted_text, a, b)
    data = {
        "encrypted_text": encrypted_text,
        "decrypted_text": decrypted_text,
        "encryption_steps": encryption_steps,
        "decryption_steps": decryption_steps
    }
    response = {
        "success": True,
        "data": data,
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)