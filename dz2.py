var1 = []
var2 = []
def name1(func):
    def _handler(arg):
        var1.append(func.__name__)
        return func(arg)
    return _handler
   

@name1
def function(a):
    return a**a
for i in range(2, 10, 2):
    print(function(i), i)

@name1
def func1(a):
    return a + a
for i in range(1, 10, 3):
    print(func1(i), i)

print(var1) 
print (set(var1))

for i in var1:
  if i not in var2:
    var2.append(i)
print(var2)