from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_vector
from qiskit.quantum_info import Statevector
from numpy import pi
import matplotlib.pyplot as plt
import numpy as np
from bloch_utils import statevector_to_bloch

qc = QuantumCircuit(1)

theta = np.pi / 2
phi = np.pi / 4

qc.ry(theta, 0)
qc.rz(phi, 0)

state = Statevector.from_instruction(qc)
bloch = statevector_to_bloch(state)

plot_bloch_vector(bloch, title = "theta = pi/2, phi = pi/4")
plt.show()





