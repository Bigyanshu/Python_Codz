file = open('text.txt','r')
content = file.read()
file.close()
print(f"Content of 'text.txt' : {content}")
