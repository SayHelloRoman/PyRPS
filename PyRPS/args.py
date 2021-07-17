import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-time', help='Specify how many seconds will be tested', default=5, type=int)
parser.add_argument('-url', help='Specify address', type=str)
args = parser.parse_args()

time = args.time
url  = args.url