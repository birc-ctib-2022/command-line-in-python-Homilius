import sys

x = sys.stdin.read() if len(sys.argv) < 2 else sys.argv[1]
x = x.strip()

def split_args(args):
    flags, rest = [], []
    for arg in args:
        if arg.startswith('-'):
            flags.append(arg)
        else:
            rest.append(arg)
    return flags, rest

flags, args = split_args(sys.argv[1:])

if '-s' in flags:
	print(''.join(args))

if '-n' in flags:
	print(' '.join(args), end ='')

if len(flags) < 1:
	print(' '.join(args))
