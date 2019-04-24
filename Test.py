'''name,ch = input('enter your name and character: ').split(',')
print(f'the length of your name is {len(name)}')
print(f'the number of times {ch} appeared are {name.count(ch.upper())+name.count(ch.lower())}')
'''
name = "sumit saurav"
print(f'{name.center(1+len(name),"*")}')

str = 'string'
str = str.replace('t','T')
print(str)