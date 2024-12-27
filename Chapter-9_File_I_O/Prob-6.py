# WAP to mine a log file & find out wheather it contains "Python"

with open('log.txt', 'r') as f:
    v = f.read()
if "Python" in v:
    print("Yes, Present")
else:
    print("No, Absent")