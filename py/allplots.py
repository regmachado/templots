import os, glob

for name in sorted(glob.glob('???.py')):
    cmd = 'python3 %s' % name
    print(cmd)
    os.system(cmd)
