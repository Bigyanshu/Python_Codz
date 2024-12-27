# Accordingly q6 find line no of Python

with open('log.txt') as f:
    lines = f.readlines()
lineno = 1

for line in lines:
    if ("Python" in line):
        print(f"Python found in line : {lineno}")
        # lines[lineno] = line
        break # after if block excuted then not executed else block
    lineno += 1
else:
    print("Python not found in the file")