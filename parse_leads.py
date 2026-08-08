import re
with open('neuro-companies/non-us-neuro-leads.html') as f:
    html = f.read()
cards = re.split(r'<div class="card">', html)
print(f'Cards: {len(cards)}')
exhausted = ['INBRAIN Neuroelectronics','BrainQ','Neuroelectrics','Flow Neuroscience',
'GrayMatters Health','Hilo','Nobi','Omniscient Neurotechnology','ONWARD Medical',
'Bitbrain','Neurable','Neurovalens','MindMaze','SynPhNe','Intellect',
'Saluda Medical','Theranica','SetPoint Medical','BrainCo','Insightec',
'Zander Labs','Neurosoft Bioelectronics','Mobia','Cerebrel','Neurowyzr','NeuroDrive']
pending = ['Neurolief','ReVision Implant','Sychedelic','BrainQ / BRAIN.Q','Synchron',
'Coherence Neuro','Aurenar','Aleph Neuro','Lotus Neuro','CorTec','MintNeuro',
'Gestala','Hemispheric','Neuracle','Universal Brain','Neuronostics','Fluent']
for i, card in enumerate(cards[1:], 1):
    nm = re.search(r'<div class="company">(.*?)</div>', card)
    if not nm: continue
    name = nm.group(1).strip()
    if name in exhausted or name in pending: continue
    fb = re.search(r'class="funding-badge">(.*?)</div>', card)
    fl = re.search(r'flag">([^<]+)', card)
    em = re.search(r'href="mailto:([^"]+)"', card)
    ph = re.search(r'href="tel:([^"]+)"', card)
    li = re.search(r'href="(https://[^"]+linkedin[^"]+)"', card)
    wy = re.search(r'class="why[^>]*>.*?<strong>Why Jordan:</strong>(.*?)</div>', card, re.DOTALL)
    pr = re.search(r'class="product">(.*?)</div>', card)
    print(f'{i}. {fl.group(1) if fl else ""} {name}')
    print(f'   Badge: {fb.group(1) if fb else ""}')
    print(f'   Product: {pr.group(1) if pr else ""}')
    print(f'   Email: {em.group(1) if em else "none"}')
    print(f'   Phone: {ph.group(1) if ph else "none"}')
    print(f'   LI: {li.group(1)[:60] if li else "none"}...')
    print(f'   Why: {wy.group(1)[:120].strip() if wy else ""}')