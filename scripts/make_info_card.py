import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; d=json.loads((ROOT/'scripts/profile.json').read_text())
def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
rows=[('name',d.get('name','Raunak')),('role',d.get('title','')),('location',d.get('location','')),('now',d.get('now','')),('stack',d.get('stack','')),('highlights',d.get('highlights',''))]
o=['<svg xmlns="http://www.w3.org/2000/svg" width="490" height="310" viewBox="0 0 490 310">','<rect width="490" height="310" rx="10" fill="#0b0f14" stroke="#30363d"/>','<rect width="490" height="38" rx="10" fill="#161b22"/>','<circle cx="20" cy="19" r="5" fill="#ff5f56"/><circle cx="39" cy="19" r="5" fill="#ffbd2e"/><circle cx="58" cy="19" r="5" fill="#27c93f"/>','<text x="245" y="24" text-anchor="middle" fill="#8b949e" font-family="monospace" font-size="13">raunak@github — profile</text>']
for i,(k,v) in enumerate(rows):
 y=76+i*37; o += [f'<text x="24" y="{y}" fill="#7ee787" font-family="monospace" font-size="14">{esc(k)}</text>',f'<text x="122" y="{y}" fill="#c9d1d9" font-family="monospace" font-size="13">{esc(v)[:43]}</text>']
o.append('</svg>'); (ROOT/'info-card.svg').write_text('\n'.join(o)); print('Wrote info-card.svg')
