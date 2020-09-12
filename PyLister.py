import sys 
import itertools

def Banner():
	print("""
  _____       _      _     _            
 |  __ \     | |    (_)   | |           
 | |__) |   _| |     _ ___| |_ ___ _ __ 
 |  ___/ | | | |    | / __| __/ _ \ '__|
 | |   | |_| | |____| \__ \ ||  __/ |   
 |_|    \__, |______|_|___/\__\___|_|   
         __/ |                          
        |___/                           
                             By Mazy_Lan""")


def payload():
	if len(sys.argv)>=5:
		minL=int(sys.argv[1])
		maxL=int(sys.argv[2])
		char=sys.argv[3]
		file=open(sys.argv[4], 'w')
		for n in range(minL, maxL+1):
			for xs in itertools.product(char, repeat=n):
				string=''.join(xs)
				file.write(string+'\n')
		file.close()
	else:
		print("Usage: pylister Min Max Char OutFil")
def main():
	Banner()
	payload()

main()