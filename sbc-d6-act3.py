string = "*"
rows = int(input("Enter number of rows: "))

for i in range(rows, 1, -1):
    print(string * i)
for l in range (1):
    spaces = " " * (rows - i) 
    stars = string * 1  
    line_ = stars + spaces + stars
    print(line_)
for i in range(2,rows + 1):
    print(string * i)