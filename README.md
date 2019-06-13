# E42
E42 - QKD [BB84](https://en.wikipedia.org/wiki/BB84) Chat's Prototype

## Installation
Clone this repository, and run:
```
pip3 install -r requirements.txt
python3 server.py
```
Then go to [localhost:5000](http://localhost:5000)

## Credits
* This system's [BB84 Algorithm](https://en.wikipedia.org/wiki/BB84) code is inspired by [Quantum_Cryptography2 of Qiskit](https://github.com/Qiskit/qiskit-tutorials/blob/master/community/awards/teach_me_qiskit_2018/quantum_cryptography_qkd/Quantum_Cryptography2.ipynb). We modified this code so that we can make QKD connection between two function, program, or clients. Finally, we implemented it to Javascript.

* [quantum-circuit js library](https://www.npmjs.com/package/quantum-circuit) is used to make Qubit operations.