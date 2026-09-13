"""Exhaustive sum/product-free subset classification in F_31^*. Standard library only."""
from pathlib import Path
import hashlib, itertools, json, re, time

started=time.monotonic()
prime=31
edge_set=set()
for x in range(1,prime):
    for y in range(1,prime):
        for z in ((x+y)%prime,(x*y)%prime):
            if z:
                edge_set.add(sum(1<<(t-1) for t in {x,y,z}))
edges=sorted(edge_set,key=int.bit_count)
minimal=[]
for e in edges:
    if not any(e&f==f for f in minimal):minimal.append(e)
incident={1<<i:[e for e in minimal if e&(1<<i)] for i in range(30)}
forbidden_singletons=sum(e for e in minimal if e.bit_count()==1)
best=0;maximizers=set();nodes=0
def visit(chosen,available):
    global best,nodes,maximizers
    nodes+=1
    size=chosen.bit_count()
    if size+available.bit_count()<best:return
    if not available:
        if size>best:best=size;maximizers=set()
        if size==best:maximizers.add(chosen)
        return
    vertices=[1<<i for i in range(30) if available&(1<<i)]
    v=max(vertices,key=lambda v:sum(((e&~chosen)&~available)==0 for e in incident[v]))
    rest=available^v;included=chosen|v;allowed=rest;valid=True
    for e in incident[v]:
        missing=e&~included
        if not missing:valid=False;break
        if missing.bit_count()==1:allowed&=~missing
    if valid:visit(included,allowed)
    visit(chosen,rest)
visit(0,((1<<30)-1)&~forbidden_singletons)
sets=sorted([i+1 for i in range(30) if m&(1<<i)] for m in maximizers)
theorem=(Path(__file__).parent/'THEOREM.md').read_text(encoding='utf-8')
printed=sorted([int(x) for x in s.split(',')] for s in re.findall(r'^\{([\d,]+)\}$',theorem,re.M))
assert best==8 and len(sets)==9 and sets==printed

result={'prime':prime,'maximum':best,'extremal_count':len(sets),'valid_size_9_count':0,'extremizers':sets,'search_nodes':nodes,'minimal_forbidden_edges':len(minimal),'method':'Exhaustive include/exclude enumeration with monotone forbidden-edge propagation and cardinality pruning.','elapsed_seconds':round(time.monotonic()-started,6)}
print(json.dumps(result,indent=2))
