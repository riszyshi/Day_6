rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

row = 0
while row < rows:
  col = 0
  while col < columns:
    if row == 0 or row == rows - 1 or col == 0 or col == columns - 1:
      print("*", end="")
    else:
      print(" ", end="")
    col += 1
  print("")
  row += 1