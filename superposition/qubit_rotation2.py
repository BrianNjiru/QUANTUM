from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_vector
import numpy as np
import matplotlib.pyplot as plt

def get_bloch_vec(circuit):
	state = Statevector.from_instruction(circuit)
	return state.to_dict()['bloch_vector']

def plot_vec(vec, title):
	plot_bloch_vector(vec, title=title)
	plt.show()

qc_rx = QuantumCircuit(1)
qc_rx.rx(np.pi/2, 0)
vec_rx = Statevector.from_instruction(qc_rx).bloch_vector()
plot_bloch_vector(vec_rx, title="Rx(pi/2)")

qc_ry = QuantumCircuit(1)
qc_ry.ry(np.pi/2, 0)
vec_ry = Statevector.from_instruction(qc_ry).bloch_vector()
plot_bloch_vector(vec_ry, title="Ry(pi/2)")

qc_rz = QuantumCircuit(1)
qc_rz.h(0)
qc_rz.rz(np.pi/2, 0)
vec_rz = Statevector.from_instruction(qc_rz).bloch_vector()
plot_bloch_vector(vec_rz, title="Rz(pi/2)")
