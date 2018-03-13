import os
from random import choice

print(len(os.getcwd().split()))
print(len(os.getcwd().split()))
# f, e,g,h = os.getcwd().split()
# print(f,e)
people=['2','3','66', '22']
def main():
  person=choice(people)
  print(person)
  try:
    f = open(r'c:\a.txt', 'w')
    f.write('hello world 中共')
    print(f.close())
  except Exception as e:
    print(e)


if __name__ == '__main__':
    main()
