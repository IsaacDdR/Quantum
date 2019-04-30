from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

def build_bell_circuit():
    q = QuantumRegister(2)
    c = ClassicalRegister(2)

    qc = QuantumCircuit(q,c)

    qc.h(q[0])

    qc.cx(q[0], q[1])

    qc.measure(q, c)

    return qc

build_circuit = build_bell_circuit()

print(build_circuit)

