
import rpg

print rpg.version()

N = 2000
poly = rpg.rpg(N)

print "generated random polygon with",N,"vertices"

print "The vertices are:"
n=0
for p in poly:
    print n," ",p
    n=n+1
