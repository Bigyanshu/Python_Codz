# Can we have a set with 18 (int) and '18' (str) as a value in it? 
s = set()

s.add(int(18))
s.add(str(18)) # || s.add('18')

print(s) # Outputs: {18, '18'} 
# printing elements not in any manner due to set has no indexing format.