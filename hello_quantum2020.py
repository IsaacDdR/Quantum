import numpy as np

from qiskit import(
  QuantumCircuit,
  execute,
  Aer,
  IBMQ)

from qiskit.visualization import plot_histogram

IBMQ.save_account('f3ab4eb0aa3946185519e07e636619e2e6e2a96f01a2dee60a0a727b354bba7e5a2ade73a410276f3f0c7ae95a260ac0ce4b742d779f2d18e9f020745f0d1e95')

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(2, 2)

# Add a H gate on qubit 0
circuit.h(0)

# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)

# Map the quantum measurement to the classical bits
circuit.measure([0,1], [0,1])

# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)

# Draw the circuit
circuit.draw()
