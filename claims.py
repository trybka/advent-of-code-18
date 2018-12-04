from collections import defaultdict
from functools import partial

def fill(matrix, left, top, width, height):
  for x in range(left, left+width):
    for y in range(top, top+height):
      matrix[x][y] += 1

def check(matrix, left, top, width, height):
  for x in range(left, left+width):
    for y in range(top, top+height):
      if matrix[x][y] > 1:
        return False
  return True

def part1():
  m = defaultdict(partial(defaultdict, int))
  claims = []    
  with open("claims.txt") as f:
    claims = f.readlines()

  for claim in claims:
    spatial = claim.split('@')[1].strip()
    coords, dims = spatial.split(':')
    top, left = coords.strip().split(',')
    width, height = dims.strip().split('x')
    fill(m, int(top), int(left), int(width), int(height))

  ret = 0
  for row in range(999):
    for col in range(999):
      if m[row][col] > 1:
        ret += 1
  print ret

def part2():
  m = defaultdict(partial(defaultdict, int))
  claims = []    
  with open("claims.txt") as f:
    claims = f.readlines()

  for claim in claims:
    spatial = claim.split('@')[1].strip()
    coords, dims = spatial.split(':')
    top, left = coords.strip().split(',')
    width, height = dims.strip().split('x')
    fill(m, int(top), int(left), int(width), int(height))

  for claim in claims:
    claimid, spatial = claim.split('@')
    coords, dims = spatial.strip().split(':')
    top, left = coords.strip().split(',')
    width, height = dims.strip().split('x')
    if check(m, int(top), int(left), int(width), int(height)):
      print claimid 

#part1()
part2()
