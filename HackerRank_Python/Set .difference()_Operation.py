# Enter your code here. Read input from STDIN. Print output to STDOUT

num1,str1,num2,str2=(set(input().split()) for i in range(4))
print(len(str1.difference(str2)))