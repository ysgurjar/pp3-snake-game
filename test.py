input=[(1,2),(2,3),(3,4)]

# Output-1 when moving the snake, all coordinates with change
# output [(2,3),(3,4), algebric sum of two tuples for ex (3,4) + (0,-1) = (3,3)

def move(direction):
  head=input.pop(0)
  zip_obj=zip(head,direction)
  coordinate= [sum(x) for x in zip_obj]
  new_head=tuple(coordinate)
  input.insert(0, new_head)
  print(input)
move((0,-1))