import glob
import random
import dpll

def load(fn):
  f = open(fn, 'r')
  data = f.read()
  f.close()
  clauses = []
  lines = data.split("\n")
  for line in lines:
    if len(line) == 0 or line[0] in ['c', 'p', '%', '0']:
      continue
    clause = [int(x) for x in line.split()[0:-1]]
    clauses.append({x for x in clause})
  return clauses

#[(fn, True) for fn in glob.glob("sat_tests/SAT/*.cnf")]
files = [(fn, True) for fn in glob.glob("sat_tests/SAT/*.cnf")]+[(fn, False) for fn in glob.glob("sat_tests/UNSAT/*.cnf")]
random.shuffle(files)

for (fn, sat) in files:
  print(fn, end=': ')
  s = dpll.Solver(load(fn))
  assert(s.solve() == sat)
  print("passed")



