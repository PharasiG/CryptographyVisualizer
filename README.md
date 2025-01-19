# CipherHaven
CipherHaven is an advanced cryptography platform that integrates multiple cryptographic algorithms, vulnerability scanning, attack simulations, and best practices to help users understand and enhance their security posture. This project leverages visualizations of popular cryptographic algorithms, including RSA, AES, and Affine ciphers, and gamifies learning by providing interactive experiences that simulate attacks and vulnerabilities.

## Features

- **Cryptography Visualizer**: 
  - Visualize how RSA, AES, and Affine ciphers work in real-time.
  - Interactive tools for learning and experimenting with encryption and decryption processes.
  
- **Vulnerability Scanner**:
  - Detect vulnerabilities in cryptographic implementations.
  - Analyze the strength of cryptographic keys, identify weaknesses, and suggest improvements.

- **Attack Simulation**:
  - Simulate various attack vectors such as brute force, chosen plaintext, and side-channel attacks.
  - Understand the effects of each attack on different cryptographic algorithms.

- **Best Practices**:
  - Display recommended encryption standards and configurations for better security.
  - Guidelines for generating strong keys and securely storing cryptographic information.

- **Gamification**:
  - Engage users with challenges and simulations that reward learning and mastery of cryptographic concepts.
  - Progress through levels, solve puzzles, and unlock advanced features as you gain experience.
   
 ### Question/Answer
```
1)
Weak encryption algorithm: DES
Replace DES with AES, which is more secure and modern.
FLAG{weak_des_not_recommended}

2)
Vulnerable encryption mode: ECB
Switch from ECB mode to CBC or GCM, which hide patterns in the data.
FLAG{ecb_mode_reveals_patterns}

3)
Padding oracle vulnerability exists in the decryption process where error messages reveal information about padding
Implement constant time padding validation and use generic error messages that don't reveal padding information
FLAG{padding_oracle_vulnerability}

4)
Key reuse across multiple messages allows attackers to perform cryptanalysis by comparing ciphertexts encrypted with the same key
Use unique keys for each encryption operation and implement proper key rotation policies
FLAG(key_reuse_danger}

5)
Try it yourself!!😁
```

## Supported Algorithms

- **RSA**:
  - Public-key encryption algorithm widely used for secure data transmission.
  - Visualize key generation, encryption, and decryption steps.

- **AES**:
  - Symmetric-key block cipher, considered secure for data encryption.
  - Explore how different key sizes and modes of AES impact encryption and decryption.

- **Affine Cipher**:
  - A classical substitution cipher based on linear algebra.
  - Learn how encryption and decryption work with mathematical principles.

## Installation

To get started with CipherHaven, follow the installation instructions below:

### Prerequisites

- Python 3.7 or later
- Pip (Python package installer)
- Flask
- Pycryptodome
- HTML, CSS, JavaScript


