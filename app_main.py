from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
import RSA
import AES
import AffineCipher
import base64
import hmac

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

class CryptoChallenge:
    def __init__(self):
        self.current_level = 1
        self.max_level = 5
        self.score = 0
        self.flags = self._generate_flags()

    def _generate_flags(self) -> dict:
        """Generate unique flags for each level."""
        return {
            1: "FLAG{weak_des_not_recommended}",
            2: "FLAG{ecb_mode_reveals_patterns}",
            3: "FLAG{padding_oracle_vulnerability}",
            4: "FLAG{key_reuse_danger}",
            5: "FLAG{timing_attack_possible}"
        }

    def get_challenge(self):
        """Return the current challenge based on level."""
        challenges = {
            1: self._create_level_one,
            2: self._create_level_two,
            3: self._create_level_three,
            4: self._create_level_four,
            5: self._create_level_five
        }
        return challenges[self.current_level]()

    def _create_level_one(self):
        """Level 1: Identify weak encryption (DES)"""
        return {
            "level": 1,
            "title": "Basic Encryption Vulnerability",
            "description": "Identify and fix the weak encryption algorithm being used.",
            "hint": "Modern applications should avoid using DES.",
            "encrypted_data": base64.b64encode(b"sample_encrypted_data").decode(),
            "key": base64.b64encode(b"12345678").decode()
        }

    def _create_level_two(self):
        """Level 2: ECB Mode Pattern Recognition"""
        return {
            "level": 2,
            "title": "Block Cipher Mode Analysis",
            "description": "Detect the vulnerable encryption mode and suggest a secure alternative.",
            "hint": "Look for patterns in the encrypted data blocks.",
            "encrypted_data": base64.b64encode(b"pattern_data" * 4).decode(),
            "key": base64.b64encode(b"1234567890123456").decode()
        }

    def _create_level_three(self):
        """Level 3: Padding Oracle Challenge"""
        return {
            "level": 3,
            "title": "Padding Oracle Detection",
            "description": "Find and fix the padding oracle vulnerability in the decryption process.",
            "hint": "Check how padding errors are handled during decryption.",
            "encrypted_data": base64.b64encode(b"paddingvulnerable").decode(),
            "iv": base64.b64encode(b"1234567890123456").decode(),
            "key": base64.b64encode(b"1234567890123456").decode()
        }

    def _create_level_four(self):
        """Level 4: Key Reuse Detection"""
        return {
            "level": 4,
            "title": "Key Management Security",
            "description": "Identify the key management vulnerability in the encryption process.",
            "hint": "Look for patterns that might emerge from key reuse.",
            "encrypted_messages": [
                base64.b64encode(b"message1").decode(),
                base64.b64encode(b"message2").decode()
            ],
            "key": base64.b64encode(b"1234567890123456").decode()
        }

    def _create_level_five(self):
        """Level 5: Timing Attack Vulnerability"""
        return {
            "level": 5,
            "title": "Advanced Security Analysis",
            "description": "Identify and fix the timing-based vulnerability in the comparison function.",
            "hint": "Consider how execution time might reveal information.",
            "secret": base64.b64encode(b"secret_data_here").decode()
        }

    def submit_solution(self, solution):
        """Verify the submitted solution and return result"""
        try:
            required_fields = ["identified_vulnerability", "proposed_fix", "flag"]
            if not all(field in solution for field in required_fields):
                return False, "Missing required solution fields"

            if solution["flag"] != self.flags[self.current_level]:
                return False, "Incorrect flag"

            if not self._verify_solution(solution):
                return False, "Incorrect vulnerability identification or fix"

            self.score += 10
            if self.current_level < self.max_level:
                self.current_level += 1

            return True, f"Level {self.current_level - 1} completed! Score: {self.score}"

        except Exception as e:
            return False, f"Error processing solution: {str(e)}"

    def _verify_solution(self, solution):
        """Verify if the proposed solution correctly identifies and fixes the vulnerability"""
        verification_checks = {
            1: lambda s: "des" in s["identified_vulnerability"].lower() and "aes" in s["proposed_fix"].lower(),
            2: lambda s: "ecb" in s["identified_vulnerability"].lower() and (
                        "cbc" in s["proposed_fix"].lower() or "gcm" in s["proposed_fix"].lower()),
            3: lambda s: "padding" in s["identified_vulnerability"].lower() and "constant time" in s[
                "proposed_fix"].lower(),
            4: lambda s: "key reuse" in s["identified_vulnerability"].lower() and "unique key" in s[
                "proposed_fix"].lower(),
            5: lambda s: "timing" in s["identified_vulnerability"].lower() and "constant time" in s[
                "proposed_fix"].lower()  # Added check for constant-time comparison
        }
        return verification_checks[self.current_level](solution)

    def get_progress(self):
        """Return current progress and score"""
        return {
            "current_level": self.current_level,
            "max_level": self.max_level,
            "score": self.score,
            "completion_percentage": (self.current_level - 1) * 100 // self.max_level
        }



# Initialize game instance globally
game = CryptoChallenge()


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
    challenge = game.get_challenge()
    return render_template('challenge.html', challenge=challenge)

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

@app.route('/submit_solution', methods=['POST'])
def submit_solution():
    """Route for submitting a solution"""
    identified_vulnerability = request.form['identified_vulnerability']
    proposed_fix = request.form['proposed_fix']
    flag = request.form['flag']

    solution = {
        "identified_vulnerability": identified_vulnerability,
        "proposed_fix": proposed_fix,
        "flag": flag
    }

    success, message = game.submit_solution(solution)
    flash(message)

    if success:
        progress = game.get_progress()
        return render_template('progress.html', progress=progress)

    return redirect(url_for('gamify'))

@app.route('/game_over')
def game_over():
    """End game route"""
    return render_template('game_over.html', score=game.score)

if __name__ == '__main__':
    app.run(debug=True)
