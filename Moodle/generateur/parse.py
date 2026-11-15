import json,sys,xml.etree.ElementTree as ET
d=json.load(open(sys.argv[1],encoding='utf8'))
root=ET.fromstring(d['data']['xml'])
def inl(el):
    out=[]
    for c in el:
        if c.tag=='text':
            b=c.find('bold')
            if b is not None: out.append(('b',''.join(b.itertext())))
            else: out.append(('t',''.join(c.itertext())))
        elif c.tag=='date': out.append(('t',c.get('value')))
        elif c.tag=='mention': out.append(('t',c.get('name') or ''))
        else: out.append(('t',''.join(c.itertext())))
    return out
blocks=[]
for el in root:
    if el.tag=='paragraph':
        h=el.get('heading')
        blocks.append({'type':'h'+h if h else 'p','inl':inl(el)})
    elif el.tag=='table':
        rows=[]
        for r in el.findall('row'):
            cells=[]
            for c in r.findall('cell'):
                cells.append({'h':c.get('header')=='true','inl':sum([inl(p) for p in c.findall('paragraph')],[])})
            rows.append(cells)
        blocks.append({'type':'table','rows':rows})
    elif el.tag=='embed':
        blocks.append({'type':'embed','ref':el.get('ref'),'caption':el.get('caption')})
    else:
        blocks.append({'type':el.tag,'raw':''.join(el.itertext())})
json.dump(blocks,open(sys.argv[2],'w',encoding='utf8'),ensure_ascii=False,indent=0)
for b in blocks:
    if b['type'].startswith('h') or b['type'] in('embed',) or b['type'] not in('p','table'):
        print(b['type'], (''.join(t for _,t in b.get('inl',[])) if 'inl' in b else b.get('ref') or b.get('raw'))[:90])
