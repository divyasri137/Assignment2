from collections import OrderedDict
  
od = OrderedDict()
od['a'] = input("input1\n")
od['b'] = input("input2\n")
od['c'] = input("input3\n")
od['d'] = input("input4\n")
od['e'] = input("input5\n")
 

if od.values() % 2==0:
    print(od.values() + "0")
else:
    print(od.values()+"1")