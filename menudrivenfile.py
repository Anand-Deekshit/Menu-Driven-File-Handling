import os
os.chdir("C:\\Users\\Anand\\Desktop\\")
class File:
  def __init__(self):
    self.menu()

  def ip(self):
    self.f = input("Enter the path")
    return self.f
    
  def dir_tree(self, f):
    path = os.getcwd()
    folders = path.split("\\")
    folders.append(f)
    i = 0
    for folder in folders:
      print(i * "|_" + folder)
      i += 1

  def create(self):
    f = self.ip()
    if os.path.exists(f) == False:
      with open(f, "w") as file:
        print("File created")
      self.menu()
    else:
      print("File already exists")
      self.dir_tree(f)
      self.menu()

  def write(self):
    self.f = self.ip()
    if os.path.exists(self.f):
      i = input()
      with open(self.f, 'w') as file:
        file.write(str(i))
      self.dir_tree(self.f)
      self.menu()
    else:
      print("File does not exist or it is not empty. Do you want to append?")
      choice = input()
      if choice == 'Yes' or 'yes':
        self.append(self.f)
        self.dir_tree()
      self.menu()
  def append(self, f):
    try:
      if os.path.exists(self.f):
        self.f.append(input())
        self.menu()
    except:
      print("File does not exist")
      self.menu()

  def append(self):
    self.f = self.ip()
    try:
      if os.path.exists(self.f):
        self.f.append(input())
        self.dir_tree()
        self.menu()
    except:
      print("File does not exist")
      self.menu()

  def read(self):
    self.f = self.ip()
    if os.path.exists(self.f):
      with open(self.f) as file:
        k = tuple(file.read().split(" "))
        k = " ".join(k)
        print(k)
        self.dir_tree(self.f)
      self.menu()
    else:
      print("File does not exist")
      self.menu()

  def delete(self):
    self.f = self.ip()
    try:
      if os.path.exists(self.f):
        os.remove(self.f)
        self.dir_tree()
        self.menu()
    except:
      print("File does not exists")
      self.menu()

  def red(self):
    d1 = input("Enter the first directory")
    d2 = input("Enter the second directory")
    s1 = set(os.listdir())
    s2 = set(os.listdir())
    if s1 & s2 != 0:
      print(len(s1 & s2), " redundant files exist")
      print(s1 & s2)
    else:
      print('No redundant files exits')
      
  

  def menu(self):
    print("1. Create\n2. Write\n3. Append\n4. Read\n5. Delete\n6. Check redundant files")
    ch = int(input("Enter an operation"))
    if ch == 1:
      self.create()
    elif ch == 2:
      self.write()
    elif ch == 3:
      self.append()
    elif ch == 4:
      self.read()
    elif ch == 5:
      self.delete()
    elif ch == 6:
      self.red()
    else:
      print("Enter a valid choice")

  

File()
    
