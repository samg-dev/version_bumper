import random

with open('example_packages.txt', 'w') as f:
	for i in range(0,100):
            string = '\'example.package.%d==%d.%d.%d\'' % (
	    i,random.randint(0,5),random.randint(0,10),random.randint(0,20))
			    
	    f.write(string + '\n' )
