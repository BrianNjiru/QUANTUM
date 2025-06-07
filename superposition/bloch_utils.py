import numpy as np

def statevector_to_bloch(statevector):
	"""
	Converts a single-qubit statevector into a Bloch vector.
	Args:
		statevector (qiskit.quantum_info.Statevector): The qubit statevector.
	Returns:
		list: [x,y,z] coordinates of the Bloch vector.
	"""
	alpha = statevector.data[0]
	beta = statevector.data[1]

	x = 2 * np.real(np.conj(alpha)*beta)
	y = 2 * np.imag()np.conj(alpha)*beta)
	z = np.abs(alpha)**2 - np.abs(beta)**2

	return [x,y,z]
