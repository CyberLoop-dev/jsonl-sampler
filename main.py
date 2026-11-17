import argparse,json,random
def sample(lines,n,seed=0):
 if n<0: raise ValueError("count must be non-negative")
 r=random.Random(seed);out=[]
 for i,line in enumerate(lines):
  if not line.strip():continue
  json.loads(line)
  if len(out)<n:out.append(line.rstrip())
  elif n:
   j=r.randrange(i+1)
   if j<n:out[j]=line.rstrip()
 return out
def main():
 p=argparse.ArgumentParser();p.add_argument("input");p.add_argument("output");p.add_argument("-n",type=int,default=100);p.add_argument("--seed",type=int,default=0);a=p.parse_args()
 with open(a.input,encoding="utf8") as f:rows=sample(f,a.n,a.seed)
 open(a.output,"w",encoding="utf8").write("\\n".join(rows)+("\\n" if rows else ""));print("Wrote",len(rows))
if __name__=="__main__":main()