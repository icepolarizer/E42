# E42
E42 - QKD [BB84](https://en.wikipedia.org/wiki/BB84) Chat's Prototype

While we were studying the Quantum Computing, we found the glorious QKD. We loved BB84 algorithm and wanted to make it work in our computer. We found some great example codes from IBM Qiskit's Tutorial Repo, and made them work in real internet chatting.

## How it was done
We don't have real QKD devices. They are *bloody* expensive, and we are just students. So, we decided to use the simulator.  
Problem was, QKD requires some kind of photon transfer mechanism. Basically we have to *send* the qubits from one client to the other, but we couldn't find an example for such operation. Well, it woks in single python code for testing. So we serialized an Quantum Circuit Object, and sent it using socket.  

We used Qiskit in python to prove that it's working. And for our next trick, we implemented them into Javascript...using another quantum-circuit library for js.


## Installation
Clone this repository, and run:
```
pip3 install -r requirements.txt
python3 server.py
```
Then go to [localhost:5000](http://localhost:5000)

## Contribution
Of course, since we made this as an experiment, we can't be sure that it works correctly, following the philosophy of QKD(BB84). Also, since it's built on simulator, we can't expect the real QKD's security. Since the quantum circuit object can be hijacked by hackers, and hackers can predict the result of measurement.  
However, that isn't our point. We just wanted to show how it works, and how amazing Quantum Key Distribution is.  
So, we appriciate any kind of contribution adn contact about this project. Please contribute and contact if you found anything wrong or needs upgrade.

## Credits
* This system's [BB84 Algorithm](https://en.wikipedia.org/wiki/BB84) code is inspired by [Quantum_Cryptography2 of Qiskit](https://github.com/Qiskit/qiskit-tutorials/blob/master/community/awards/teach_me_qiskit_2018/quantum_cryptography_qkd/Quantum_Cryptography2.ipynb). We modified this code so that we can make QKD connection between two function, program, or clients. Finally, we implemented it to Javascript.

* [quantum-circuit js library](https://www.npmjs.com/package/quantum-circuit) is used to make Qubit operations.