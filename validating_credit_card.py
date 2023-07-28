# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

# compile the patterns
pattern = re.compile(
    r'^'
    r'(?!.*(\d)(-?\1){3})'
    r'[456]\d{3}'
    r'(?:-?\d{4}){3}'
    r'$')


for _ in range(int(input().strip())):
    
    #using pattern to search if the number is valid
    print('Valid' if pattern.search(input().strip()) else 'Invalid')
