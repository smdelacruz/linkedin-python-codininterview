# Linkedin Learning tutorial
Get_Ready_Coding_Interview by CS Dojo


#### Installation
1. [Anaconda](https://www.anaconda.com/products/individual) (mine was installed on Users>username>Anaconda3)
2. 


#### Notes:
1. Anaconda will install a new instance of Python3
2. List 
3. String are like List
4. 2-dimentional array example:
```
--initialize
a = [[2,4,1,4],[9,2,5,4]]

--retrieve
a[0] #[2,4,1,4]
a[0][2] #1

--setting
a[0][1] = 100
print(a) # [[2,100,1,4],[9,2,5,4]]

--iteration method1
a = [[2,4,1,4],[9,2,5,4]]
for row in a:
    for item in row:
        print(item) #24149254 (printed vertically)

--iteration method2
a = [[2,4,1,4],[9,2,5,4]]
for i in range(len(a)): #2 rows
    for j in range(len(a[i])):
        print(a[i][j])  #24149254 (printed vertically)
```

Time Complexity
good way to get rough idea of efficiency
--how much time does this function take ? 
- Linear time complexity - for loop increment base on total # of input
```
t = an + b = O(n)
```
- Constant time complexity - the same output regardless of input
```
t = O(1)
```
- Quadratic time complexity - 2d array example
```
t = an^2 + c = O(n^2)

ie
array_2d = [[1,2], [3,4]]
def total(array_2d):
x = 0 ------------------------------------> O(i)
for row in array_2d: ---------------------> O(n)--- O(n^2)
    for item in row:----------------------> O(n)---^
        x+= item--------------------------> O(1)---^
return x ---------------------------------> o(i)
```
   