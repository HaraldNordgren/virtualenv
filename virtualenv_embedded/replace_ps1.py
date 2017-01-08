import re
import sys


env_dir = "(%s)" % sys.argv[1]
old_ps1 = sys.argv[2]

m = re.search('(^[\n]+)(.*)', old_ps1, re.DOTALL)

if m:
    new_ps1 = "%s%s %s" % (m.group(1), env_dir, m.group(2))
else:
    new_ps1 = "%s %s" % (env_dir, old_ps1)

sys.stdout.write(new_ps1)
