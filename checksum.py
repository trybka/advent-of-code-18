from collections import defaultdict

def part1():
  barcodes = []
  check_input = defaultdict(int)
  with open('codes.txt') as f:
    barcodes = f.readlines()
    for b in barcodes:
      for c in [chr(x) for x in range(97,97+26)]:
        if b.count(c) == 2:
          check_input[2] += 1
          break
      for c in [chr(x) for x in range(97,97+26)]:
        if b.count(c) == 3:
          check_input[3] += 1
          break
  print check_input[2] * check_input[3]

#part1()

def part2():
  barcodes = []
  with open('codes.txt') as f:
    barcodes = f.readlines()
    for i in barcodes:
      for j in barcodes:
        if i == j:
          continue
        for n in range(len(i)):
          i_cmp = i[0:n] + '.' + i[n+1:]
          j_cmp = j[0:n] + '.' + j[n+1:]
          if i_cmp == j_cmp:
            print i_cmp


part2()
