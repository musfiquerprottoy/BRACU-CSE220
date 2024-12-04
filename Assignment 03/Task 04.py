

#Linked List based Stack is implemented in the following cell.

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

#You can print your stack using this code segment

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

#Task 3: Stack Reverse

def conditional_reverse(stack):
  #To Do
  rev_st = Stack()
  last = None

  while stack.isEmpty() == False:
    present = stack.pop()
    if present != last:
      rev_st.push(present)
      last = present
  return rev_st

def print_stack(stack):
  c_rev = Stack()

  while not stack.isEmpty():
    c_rev.push(stack.pop())

  while not c_rev.isEmpty():
    present = c_rev.pop()
    print(present, end = " ")
    stack.push(present)

  print()

print('Test 01')
st=Stack()
st.push(10)
st.push(10)
st.push(20)
st.push(20)
st.push(30)
st.push(10)
st.push(50)
print('Stack:')
print_stack(st)
print('------')
reversed_stack=conditional_reverse(st)
print('Conditional Reversed Stack:')
print_stack(reversed_stack) # This stack contains 50, 10, 30, 20, 10 in this order whereas top element should be 10
print('------')

