import numpy as np
from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_vector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
from numpy import pi

qc = QuantumCircuit(1)
qc.ry = (pi/2, 0)
qc.rz = (pi/4, 0)

state = Statevector.from_instruction(qc)

alpha, beta = state.data[0], state.data[1]

x=2*np.real(np.conj(alpha)*beta)
y=2*np.imag(np.conj(alpha)*beta)
z=np.abs(alpha)**2-np.abs(beta)**2

bloch = [x,y,z]

print("Bloch vector: ", bloch)

plot_bloch_vector(bloch, title = "Manual Bloch vector calculation")
plt.show()
