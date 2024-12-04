class Node:
  def __init__(self,elem=None,next=None):
    self.elem = elem
    self.next = next

class Stack:
  def __init__(self):
    self.__top = None

  def push(self,elem):
    nn = Node(elem,self.__top)
    self.__top = nn

  def pop(self):
    if self.__top == None:
      #print('Stack Underflow')
      return None
    e = self.__top
    self.__top = self.__top.next
    return e.elem

  def peek(self):
    if self.__top == None:
      #print('Stack Underflow')
      return None
    return self.__top.elem

  def isEmpty(self):
    return self.__top == None


#You can run this driver code cell to understand the methods of Stack class
st = Stack()
st.push(4)
st.push(3)
st.push(5)
st.push(1)
st.push(9)

print('Peeked Element: ',st.peek())
print('Popped Element: ',st.pop())
print('Popped Element: ',st.pop())
print('Popped Element: ',st.pop())
print('Peeked Element: ',st.peek())
print('Popped Element: ',st.pop())
print('Popped Element: ',st.pop())
print('Peeked Element: ',st.peek())
print('Popped Element: ',st.pop())
print(st.isEmpty())

def print_stack(st):
  if st.isEmpty():
    return
  p = st.pop()
  print('|',p,end=' ')
  if p<10:
    print(' |')
  else:
    print('|')
  #print('------')
  print_stack(st)
  st.push(p)

# st = Stack()
# st.push(4)
# st.push(3)
# st.push(5)
# st.push(1)
# st.push(9)
# print_stack(st)
# print('------')

def diamond_count(stack,string):
  #TO DO
  diamond_count = 0
  for n in string:
    if n == "<":
      stack.push(n)
    elif n == ">":
      if stack.pop() ==  "<":
        diamond_count+=1
  return diamond_count

print('Test 01')
stack = Stack()
string = '<..><.<..>> '
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 3
unittest.output_test(returned_value, 3)
print('-----------------------------------------')


print('Test 02')
stack = Stack()
string = '<<<..<......<<<<....>'
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 1
unittest.output_test(returned_value, 1)
print('-----------------------------------------')


print('Test 03')
stack = Stack()
string = '>>><...<<..>>...>...>>>'
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 3
unittest.output_test(returned_value, 3)
print('-----------------------------------------')