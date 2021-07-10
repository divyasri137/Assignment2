f = open('list1.txt')
f1 = open('output.txt', 'a')

doIHaveToCopyTheLine=False

for line in f.readlines():

    if 'tests/file/myword' in line:
        doIHaveToCopyTheLine=True

    if doIHaveToCopyTheLine:
        f1.write(line)

f1.close()
f.close()