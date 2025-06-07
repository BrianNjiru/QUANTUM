from qiskit import QuantumCircuit, Aer, transpile
from qiskit.visualization import plot_bloch_vector
from qiskit.quantum_info import Statevector
import numpy as np

qc = QuantumCircuit(1)

theta = np.pi / 2
phi = np.pi / 4

qc.ry(theta, 0)
qc.rz(phi, 0)

sv = Statevector.from_instruction(qc)
vloch = sv.data
bloch_vec = sv.to_bloch_vector()
plot_bloch_vector(bloch_vec, title = "theta = pi/2, phi = pi/4")
