# WAP to generate Multiplication table from 2 to 20 & write it to different files

def genMul(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} * {i} = {n*i}\n "
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)
for i in range(2,100):
    genMul(i)