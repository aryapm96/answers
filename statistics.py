import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str, required=True)
parser.add_argument('--country', type=str, required=True, help='Country to perform operation for')
parser.add_argument('--o{avg,min,max}', type=int,help='Operation to perform on dates.(Default avg)')
parser.add_argument('--from', type=date,help='Starting year (inclusive)')
parser.add_argument('--to', type=date,help='Ending year (inclusive)')
args = parser.parse_args()

if args.country:
    print(args.country,args.min,args.max,args.avg,args.from,args.to)
