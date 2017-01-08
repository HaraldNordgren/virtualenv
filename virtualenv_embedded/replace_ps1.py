import re
import sys

m = re.search('(^[\n]*)(.*)', sys.argv[2], re.DOTALL)
sys.stdout.write("%s(%s) %s" % (m.group(1), sys.argv[1], m.group(2)))
