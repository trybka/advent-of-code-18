#!/usr/local/bin/python
"""Thing"""
def do():
  seen = {}
  res = 0
  freqs = []
  with open('input.txt') as f:
    freqs = f.readlines()
  while True:
    for l in freqs:
      l = l.strip()
      l = l.rstrip('+')
      res += int(l)
      if res not in seen:
        seen[res] = True
      else:
        print res
        exit(1)

do()

