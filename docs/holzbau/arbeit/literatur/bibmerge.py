import re,glob,csv,unicodedata,collections
def norm(t):
    t=unicodedata.normalize('NFKD',t.lower()); return re.sub(r'[^a-z0-9]','',t)[:80]
def parse(txt):
    i=0;out=[]
    while True:
        j=txt.find('@',i)
        if j<0: break
        m=re.match(r'@(\w+)\s*\{',txt[j:])
        if not m: i=j+1; continue
        k=j+m.end(); depth=1; p=k
        while depth and p<len(txt):
            if txt[p]=='{': depth+=1
            elif txt[p]=='}': depth-=1
            p+=1
        body=txt[k:p-1]; key,_,rest=body.partition(',')
        out.append((m.group(1),key.strip(),rest)); i=p
    return out
def fld(body,n):
    m=re.search(r'(?:^|,)\s*'+n+r'\s*=\s*',body,re.I)
    if not m: return ''
    s=body[m.end():]
    if s.startswith('{'):
        d=0
        for q,ch in enumerate(s):
            if ch=='{': d+=1
            elif ch=='}':
                d-=1
                if d==0: v=s[1:q]; break
        else: v=s
    elif s.startswith('"'): v=s[1:s.find('"',1)]
    else: v=re.match(r'[^,\n]*',s).group(0)
    return re.sub(r'[{}]','',re.sub(r'\s+',' ',v)).strip()
def main():
    entries=[]
    for f in sorted(glob.glob('lit-*.bib')):
        for typ,key,body in parse(open(f,encoding='utf-8').read()):
            if typ.lower() in('comment','preamble','string'): continue
            entries.append(dict(key=key,typ=typ,datei=f,autor=(fld(body,'author') or fld(body,'organization') or fld(body,'institution'))[:150],jahr=fld(body,'year'),titel=fld(body,'title'),doi=fld(body,'doi').lower(),url=fld(body,'url'),note=fld(body,'note')[:250]))
    print('Einträge',len(entries))
    seen={};master=[];dups=[]
    for e in entries:
        ids=([('doi',e['doi'])] if e['doi'] else [])+[('t',norm(e['titel']))]
        hit=next((seen[i] for i in ids if i in seen and i[1]),None)
        if hit is not None: dups.append((e['key'],master[hit]['key'])); master[hit]['dateien']+=';'+e['datei']; master[hit].setdefault('alias',[]).append(e['key']); continue
        e['dateien']=e['datei']; idx=len(master); master.append(e)
        for i in ids:
            if i[1]: seen[i]=idx
    print('eindeutig',len(master),'Duplikate',len(dups)); [print(' dup',d) for d in dups]
    kc=collections.Counter(e['key'] for e in master); print('Key-Kollisionen',[k for k,c in kc.items() if c>1])
    with open('quellen-master.csv','w',newline='',encoding='utf-8') as fh:
        w=csv.DictWriter(fh,fieldnames=['id','key','alias','typ','autor','jahr','titel','doi','url','dateien','note'],extrasaction='ignore'); w.writeheader()
        for i,e in enumerate(master,1): e['id']=f'Q{i:03d}'; e['alias']=';'.join(e.get('alias',[])); w.writerow(e)


if __name__ == '__main__':
    main()
