class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
       
  def push(self, data) -> None:
    if self head is None:
      self.data = data
      self.next = next

  def pop(self) -> None:
      self.data = data
      self.next = next                                                                
    

  def status(self):
    """
    It prints all the elements of stack.
    """
    void display() {
      struct Node* ptr;
      if(top==NULL)
      cout<<"stack is empty";
      else {
        ptr = top;
        cout<<"Stack elements are: ";
        while (ptr != NULL) {
          cout<< ptr->data <<" ";
          ptr = ptr->next;
        }
      }
      cout<<endl;
    }


# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
