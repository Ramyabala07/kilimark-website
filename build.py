import re
s=open('index.src.html').read()
defs=re.search(r'<svg width="0" height="0"[^>]*>\s*<defs>(.*?)</defs>\s*</svg>\s*', s, re.S)
syms={m.group(1):(m.group(2),m.group(3)) for m in re.finditer(r'<symbol id="([^"]+)" viewBox="([^"]+)">(.*?)</symbol>', defs.group(1), re.S)}
s=s.replace(defs.group(0),'')
def rep(m):
    attrs, sid = m.group(1), m.group(2)
    vb, body = syms[sid]
    return f'<svg{attrs} viewBox="{vb}" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
s, n = re.subn(r'<svg([^>]*)><use href="#([^"]+)"/></svg>', rep, s)
assert '<use ' not in s
# artifact.html: page fragment for the Claude artifact (it adds the document wrapper itself)
open('artifact.html','w').write(s)
# index.html: complete page for GitHub Pages and local preview
open('index.html','w').write('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>Kilimark rice, milled in Madurai</title></head><body>\n'+s+'\n</body></html>')
print('icons inlined:', n)
