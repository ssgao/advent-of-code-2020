seats = []
with open('day5input') as f:
  seats = f.readlines()

def seat_number(seat: str) -> int:
  row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
  col = int(seat[7:].replace('L', '0').replace('R', '1'), 2)
  return row * 8 + col

seats = [seat_number(s) for s in seats]
seats.sort()
print(seats[-1]) # part 1

mid = len(seats) // 2
for i in range(1, 500):
  if seats[mid+i] > seats[mid] + i:
    print(f'{seats[mid]+i}')
    break
  elif seats[mid-i] < seats[mid] - i:
    print(f'{seats[mid]-i}')
    break
