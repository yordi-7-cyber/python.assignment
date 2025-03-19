def list1(n):
    return n
num=input("Enter your number:")
n=list(map(int,num.split()))
result=list1(n)
print("current list is:",result)
add=int(input("enter a value to add to the list:"))
result.append(add)
print("List after adding a number:",result)
remove=int(input("Enter a value to remove from the list:"))
if remove in result:
    result.remove(remove)
    print("After removing the value the list will be:", result)
else:
    print("Not found.")

if result:
    print("maximum value:",max(result),"\nMinimum value:",min(result))
