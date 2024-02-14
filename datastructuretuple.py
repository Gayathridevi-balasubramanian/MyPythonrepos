# Tuples are immutable array-like structures
point = (5,2)

x = point[0]
y = point[1]
print(x)
print(y)

def area_perimeter_square(sideofsquare):
  area = sideofsquare * sideofsquare
  perimeter = 4 * sideofsquare
  return(area,perimeter)

result = area_perimeter_square(7)
print(f"area : {result[0]} and perimeter : {result[1]}")