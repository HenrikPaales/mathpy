import time
# Using readlines()
start_time = time.time()
file1 = open('lemmad2013.txt', 'r')
Lines = file1.readlines()
fiveList = []
 
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    if len(line.strip()) == 5:
        fiveList += [line.strip()]


# writing to file
file1 = open('fiveword-est.txt', 'w')
file1.writelines(str(len(fiveList)))
file1.writelines(" Words")
for i in range(len(fiveList)):
    file1.writelines(fiveList[i])
    file1.writelines("\n")
    # print(fiveList[i])
file1.close()
print("{:.0e}".format(count), " cycles in %s seconds" % round((time.time() - start_time), 3))