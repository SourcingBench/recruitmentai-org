from PIL import Image, ImageDraw, ImageFont
import os
os.makedirs('public', exist_ok=True)
def font(sz, bold=True):
    for p in (["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf","/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"] if bold else ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf","/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"]):
        if os.path.exists(p): return ImageFont.truetype(p, sz)
    return ImageFont.load_default()
INK='#16181d'; IND='#4338ca'; MINT='#0f9d7a'
im=Image.new('RGB',(1200,630),'#ffffff'); d=ImageDraw.Draw(im)
for i in range(1200):
    t=i/1200; r=int(0x43+(0x0f-0x43)*t); g=int(0x38+(0x9d-0x38)*t); b=int(0xca+(0x7a-0xca)*t); d.line([(i,0),(i,14)],fill=(r,g,b))
d.rounded_rectangle((80,80,132,132),radius=14,fill=IND)
d.text((150,84),'RecruitmentAI.org',font=font(38),fill=INK)
d.text((80,210),'What is recruitment AI?',font=font(70),fill=INK)
d.text((80,310),'The plain-English handbook on AI in recruiting:',font=font(30,False),fill='#444a57')
d.text((80,355),'how it works, the seven types, the rules, how to evaluate it.',font=font(30,False),fill='#444a57')
d.text((80,500),'9 chapters · 14 vendors · 32-term glossary · independent',font=font(24,False),fill=MINT)
im.save('public/og.png')
for sz,name in [(512,'icon-512.png'),(192,'icon-192.png'),(180,'apple-touch-icon.png'),(96,'favicon-96.png')]:
    ic=Image.new('RGB',(sz,sz),IND); dd=ImageDraw.Draw(ic); dd.text((sz/2,sz/2+sz*0.03),'rAI',font=font(int(sz*0.4)),fill='#ffffff',anchor='mm'); ic.save('public/'+name)
Image.open('public/favicon-96.png').resize((48,48)).save('public/favicon.ico',sizes=[(48,48)])
open('public/favicon.svg','w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4338ca"/><stop offset="1" stop-color="#0f9d7a"/></linearGradient></defs><rect width="64" height="64" rx="14" fill="url(#g)"/><text x="32" y="43" font-family="system-ui,sans-serif" font-weight="800" font-size="30" text-anchor="middle" fill="#fff">AI</text></svg>')
print('assets ok')
