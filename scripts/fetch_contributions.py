import json,re
from datetime import date
from pathlib import Path
import requests
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]; user='RaunakEduc'
r=requests.get(f'https://github.com/users/{user}/contributions',headers={'User-Agent':'Mozilla/5.0'},timeout=30); r.raise_for_status(); soup=BeautifulSoup(r.text,'html.parser'); days=[]
for cell in soup.select('td[data-date]'):
 m=re.search(r'\d+',str(cell.get('data-level','0'))); days.append({'date':cell['data-date'],'level':max(0,min(4,int(m.group()) if m else 0))})
if not days: raise SystemExit('No contribution day cells found; GitHub may have changed its page markup.')
(ROOT/'data/contributions.json').write_text(json.dumps({'username':user,'days':days,'updated':date.today().isoformat()},indent=2)+'\n'); print(f'Saved {len(days)} days')
