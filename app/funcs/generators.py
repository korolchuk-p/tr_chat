import random 



def get_rnd_hex():
	return random.choice('0123456789abcdef')

def get_rand_hex(Len=64):
	res = ""
	for x in xrange(1, Len + 1):
		res += get_rnd_hex()
		if x % 4 == 0 and x!=0 and x!=Len:
			res += "-"
	return res




print get_rand_hex(256)

