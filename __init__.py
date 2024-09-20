import argparse

from get_data import get_data
from dmd_model import fit
from test_dmd import test

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-g', '--get', action='store_true')  # on/off flag
  parser.add_argument('-t','--ticker')
  parser.add_argument('-f','--fit', action='store_true')
  parser.add_argument('-d','--dmd',action='store_true')
  args = parser.parse_args()
  print(args)
  
  if(args.get and args.ticker):
    print("getting data for:",args.ticker)
    get_data(args.ticker)
  if(args.fit and args.ticker):
    fit(args.ticker)
  if(args.dmd and args.ticker):
    test(args.ticker)
    

if (__name__ == "__main__"):
    main()