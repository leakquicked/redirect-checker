import argparse,json
from pathlib import Path
from urllib.parse import urlparse
def review(lines):
 items=[]
 for raw in lines:
  value=raw.strip()
  if not value:continue
  p=urlparse(value)
  items.append({"url":value,"scheme":p.scheme,"host":p.hostname,"has_credentials":bool(p.username or p.password),"https":p.scheme=="https"})
 hosts={x["host"] for x in items if x["host"]}
 return {"hops":items,"host_count":len(hosts),"hosts":sorted(hosts),"warnings":[x["url"] for x in items if not x["https"] or x["has_credentials"]]}
def main():
 a=argparse.ArgumentParser();a.add_argument("file");x=a.parse_args()
 print(json.dumps(review(Path(x.file).read_text(encoding="utf-8").splitlines()),indent=2))
if __name__=="__main__":main()
