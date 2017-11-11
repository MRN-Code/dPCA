import json;
import argparse
from os import listdir
from os.path import isfile, join
import sys
import numpy as np


parser = argparse.ArgumentParser(description='help read in my data from my local machine!')
parser.add_argument('--run', type=str,  help='grab coinstac args')
args = parser.parse_args()
args.run = json.loads(args.run)

username = args.run['username']

# inspect what args were passed
# runInputs = json.dumps(args.run, sort_keys=True, indent=4, separators=(',', ': '))
# sys.stderr.write(runInputs + "\n")

if 'remoteResult' in args.run and \
    'data' in args.run['remoteResult'] and \
    username in args.run['remoteResult']['data']:
    sys.exit(0); # no-op!  we already contributed our data

passedDir = args.run['userData']['dirs'][0]
sys.stderr.write("reading files from dir: " + passedDir)

files = [f for f in listdir(passedDir) if isfile(join(passedDir, f))]

# allFileData = {}

for f in files:
    
    X = np.load(join(passedDir,f))
    d, n = X.shape
    K = 8
    C = (1.0 / n) * np.dot(X, X.T)
    U, S, V = np.linalg.svd(C)
    Uk = U[:, :K]
    Sk = np.diag(S)[:K, :K]
    P = np.dot(Uk, np.sqrt(Sk))
    en = np.trace(np.dot(Uk.T, np.dot(C, Uk)))

computationOutput = json.dumps({'P': P.tolist(), 'en': en, 'C': C.tolist()}, sort_keys=True, indent=4, separators=(',', ': '))
#computationOutput = json.dumps({'en': en}, sort_keys=True, indent=4, separators=(',', ': '))

# preview output data
# sys.stderr.write(computationOutput + "\n")

# send results
sys.stdout.write(computationOutput)

