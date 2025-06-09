from qiskit import QuantumCircuit
import numpy as np

qc = QuantumCircuit(1)
qc.rx(np.pi/2, 0)
qc.ry(np.pi/3, 0)
qc.rz(np.pi, 0)

qc.draw('mpl')
