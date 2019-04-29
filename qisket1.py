from qiskit import *

from qiskit.tools.visualization import plot_state_city

q = QuantumRegister(3, 'q')

circ = QuantumCircuit(q)

#Add a H gate (Hammard gate) in qbit 0,
#putting this qbit in superposition

circ.h(q[0])

#Add CX (CNOT) gate on control of qbit 0 and target qbit 1, putting
#the qbits in a Bell state

circ.cx(q[0], q[1])

#Add CX (CNOT) gate on control of qbit 0 and target qbit 1, putting
#the qbits in a GHZ state

circ.cx(q[0], q[2])

circ.draw(output='mpl')

backend = BasicAer.get_backend('statevector_simulator')

job = execute(circ, backend)

result = job.result()

outputstate = result.get_statevector(circ, decimals=3)

print(plot_state_city(outputstate))
