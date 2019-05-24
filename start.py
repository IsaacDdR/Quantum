import numpy as np

from qiskit import *

#Create quantum register with two qbits

q = QuantumRegister(3, 'q')

#Create a Quantum Circuit acting on the q register

circ = QuantumCircuit(q)

#Add a H gate on qubit 0, putting this qubit in superposition
circ.h(q[0])

#Add a CX (CNOT) gate on control qubit 0 and target qubit 1 putting the qubits on a bell state
