#def reverse(string):
 #   string = string[::-1]
  #  return string
#s = "Anusha"
#s = input()
#print(s)
#print(reverse(s[2::]))
lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = input()
    lst.append(ele)

a = ""
for j in lst:
    a += j
print(a)
def reverse(string):
   string = string[::-1]
   return string
print(reverse(a[2::]))

