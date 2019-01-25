class Network:
	# The network manages the whole of the GRID energy network.
	# Lets make the minds tinkers and blow up.
	def __init__(self, devices):
		# A network cannot exist without devices and a connection
		# Yes, I am playing god but this a decentralized energy. So how is our world going to look like.	
		self.devices = devices
		self.device_count = len(self.devices)

	def network_state(self):
		pass
		


a = Network([2, 3, 4, 5])
