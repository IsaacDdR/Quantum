from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import IBMQ, BasicAer, execute
from qiskit.providers.ibmq import least_busy

try:
    IBMQ.load_accounts()
except:
    print("There's no connection with the API")

try:
    # Create a Quantum Register with 2 qubits.
    q = QuantumRegister(2)

    # Create a Classical Register with 2 qubits.
    c = ClassicalRegister(2)

    # Create a Quantum Circuit.
    qc = QuantumCircuit(q, c)

    # Add a H gate on qbit 1, putting this qubit in superposition.
    qc.h(q[0])

    # Add a CX (CNOT) gate on control of qubit 0 and target qubit 1, putting 
    # the qubits in a Bell state.
    qc.cx(q[0], q[1])

    # Add a Measure gate to see the state.
    qc.measure(q, c) 


    # See a list of available local simulators
    print("BasicAer backends: ", BasicAer.backends())
    backend_sim = BasicAer.get_backend('qasm_simulator')

    # Compile and run the Quantum circuit on a simulator backend.
    job_sim = execute(qc, backend_sim)
    result_sim = job_sim.result()

    # Show the results
    print(result_sim.get_counts(qc))

    # see a list of available results
    print(result_sim.get_counts(qc))

    # see a list of available remote backends
    ibmq_backends = IBMQ.backends()

    print("Remote backends: ", ibmq_backends)

    # Compile and run the Quantum Program an a real device backend
    try: 
        least_busy_device = least_busy(IBMQ.backends(simulator=False))
    except:
        print("All devices are currently busy")
    
    print("Running on current least busy device: ", least_busy_device)

    # Running the job

    job_exp = execute(qc, least_busy_device, shots=1024, max_credits=10)
    result_exp = job_exp.result()

    # Show the results

    print("Counts: ", result_exp.get_counts(qc))

except QiskitError as ex:
    print("There was an error in the circuit!. Error = {}".format(ex))


