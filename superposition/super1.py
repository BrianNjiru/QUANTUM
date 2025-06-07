from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_vector
from qiskit.quantum_info import Statevector
from numpy import pi
import matplotlib.pyplot as plt
import numpy as np


qc = QuantumCircuit(1)

theta = np.pi / 2
phi = np.pi / 4

qc.ry(theta, 0)
qc.rz(phi, 0)

backend = Aer.get_backend('statevector_simulator')
compiled_circuit = transpile(qc, backend)
job = backend.run(compiled_circuit)
result = job.result()
raw_statevector = result.get_statevector()
statevector = Statevector(raw_statevector)
bloch = statevector.bloch_vector()


plot_bloch_vector(bloch, title = "theta = pi/2, phi = pi/4")
plt.show()
