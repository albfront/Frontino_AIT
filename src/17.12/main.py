a=range(10)
b=[el*2 for el in a]
print(b)

l=[1,2]
l2=['a','b']
l3=[4,5]
f=[(e1,e2,e3) for e1 in l for e2 in l2 for e3 in l3]
print(f)

stack=[1, 2, 3, 4]
print("Initial Stack : ", stack)
for i in range(5,7):stack.append(i)
print ("Append: ", stack)
stack.pop()
print ("Pop: " , stack)
queue=[ "a","b","c","d" ]
print("Initial Queue : ", queue)
queue.append("e")
queue.append("f")
print("Append : ", queue)
queue.pop(0)
print("Pop : ", queue)

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print(tup1)
print("tup1[0]: ", tup1[0])         

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares: print(squares[i])