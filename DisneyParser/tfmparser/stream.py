



#                https://safemarket.xyz | https://safemarket.xyz/discord
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#  | | ____     _     _____  _____      __  __     _     ____   _  __ _____  _____ | |  
#  | |/ ___|   / \   |  ___|| ____|    |  \/  |   / \   |  _ \ | |/ /| ____||_   _|| |  
#  | |\___ \  / _ \  | |_   |  _|      | |\/| |  / _ \  | |_) || ' / |  _|    | |  | |  
#  | | ___) |/ ___ \ |  _|  | |___     | |  | | / ___ \ |  _ < | . \ | |___   | |  | |  
#  | ||____//_/   \_\|_|    |_____|    |_|  |_|/_/   \_\|_| \_\|_|\_\|_____|  |_|  | |  
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#                               https://github.com/Jodis974                           



from struct import unpack

class Stream:
	def __init__(self, src):
		self.src = src
		self.bits = None
		self.count = 0

	def get_bin(self, quant):
		if not quant:
			return

		_bin = []
		while quant:
			if self.count == 0:
				a = self.src.read(1)
				b = unpack("<B", a)[0]
				self.bits = bin(b)[2:].zfill(8)
				self.count = 8
			if quant > self.count:
				quant -= self.count
				n, self.count = self.count, 0
			else:
				self.count -= quant
				n, quant = quant, 0
			_bin.append(self.bits[:n])
			self.bits = self.bits[n:]
		return int("".join(_bin), 2)

	def calc_bin(self, quant):
		if quant < 2:
			return self.get_bin(quant)

		a, b = self.get_bin(1), self.get_bin(quant - 1)
		if a == 0:
			return b
		c = 2 ** (quant - 1) - 1
		return -1 * ((b ^ c) + 1)



#                https://safemarket.xyz | https://safemarket.xyz/discord
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#  | | ____     _     _____  _____      __  __     _     ____   _  __ _____  _____ | |  
#  | |/ ___|   / \   |  ___|| ____|    |  \/  |   / \   |  _ \ | |/ /| ____||_   _|| |  
#  | |\___ \  / _ \  | |_   |  _|      | |\/| |  / _ \  | |_) || ' / |  _|    | |  | |  
#  | | ___) |/ ___ \ |  _|  | |___     | |  | | / ___ \ |  _ < | . \ | |___   | |  | |  
#  | ||____//_/   \_\|_|    |_____|    |_|  |_|/_/   \_\|_| \_\|_|\_\|_____|  |_|  | |  
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#                               https://github.com/Jodis974                           



