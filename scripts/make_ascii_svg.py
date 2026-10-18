from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance
ROOT=Path(__file__).resolve().parents[1]; PHOTO=ROOT/'source-photo.jpg'; OUT=ROOT/'raunak-ascii.svg'
RAMP=' .`:-=+*cs#%@'; COLS,ROWS=82,48; CW,CH=8,13
im=Image.open(PHOTO).convert('L'); w,h=im.size; side=min(w,int(h*.95)); left=max(0,min(w-side,(w-side)//2)); top=max(0,int(h*.10))
im=ImageOps.fit(im.crop((left,top,left+side,min(h,top+side))),(COLS,ROWS),method=Image.Resampling.LANCZOS)
im=ImageEnhance.Contrast(ImageOps.autocontrast(im,cutoff=2)).enhance(1.35)
lines=[]
for y in range(ROWS):
 line=''.join(RAMP[min(len(RAMP)-1,int((255-im.getpixel((x,y)))/256*len(RAMP)))] for x in range(COLS)); lines.append(line.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;'))
out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{COLS*CW}" height="{ROWS*CH}" viewBox="0 0 {COLS*CW} {ROWS*CH}">','<rect width="100%" height="100%" fill="#0b0f14"/>','<style>text{font:12px monospace;fill:#c9d1d9}.row{animation:show .24s steps(1,end) both}@keyframes show{from{opacity:0}to{opacity:1}}</style>']
for y,line in enumerate(lines): out.append(f'<text class="row" x="1" y="{(y+1)*CH}" style="animation-delay:{y*.045:.3f}s">{line}</text>')
out.append('</svg>'); OUT.write_text('\n'.join(out)); print('Wrote',OUT)
