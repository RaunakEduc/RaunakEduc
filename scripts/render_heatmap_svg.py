import json
from datetime import date
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; payload=json.loads((ROOT/'data/contributions.json').read_text()); days=payload['days'][-371:]; palette=['#161b22','#0e4429','#006d32','#26a641','#39d353']; cell,gap=11,4; offset=(date.fromisoformat(days[0]['date']).weekday()+1)%7; w=53*(cell+gap)+68; h=7*(cell+gap)+64
o=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">','<rect width="100%" height="100%" rx="8" fill="#0d1117"/>','<style>.day{animation:in .4s ease-out both}@keyframes in{from{opacity:0;transform:translateY(-5px)}to{opacity:1;transform:translateY(0)}}</style>']
for i,d in enumerate(days):
 pos=i+offset; x=38+(pos//7)*(cell+gap); y=12+(pos%7)*(cell+gap); level=max(0,min(4,int(d.get('level',0)))); o.append(f'<rect class="day" x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" fill="{palette[level]}" style="animation-delay:{min(i*.001,.35):.3f}s"><title>{d["date"]}: level {level}</title></rect>')
o += [f'<text x="38" y="{h-16}" fill="#8b949e" font-family="sans-serif" font-size="12">{"Live public GitHub contributions" if "note" not in payload else "Preview grid — run fetch_contributions.py for live data"}</text>','</svg>']; (ROOT/'contrib-heatmap.svg').write_text('\n'.join(o)); print('Wrote contrib-heatmap.svg')
