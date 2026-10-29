exec(open('/tmp/claude-0/s/gen5.py').read().split('# A: white')[0])
import sys,math;sys.path.insert(0,'/tmp/claude-0/s')
import fonts_sheet as FS
b64=base64.b64encode(open('/tmp/claude-0/s/art_inci.png','rb').read()).decode()
NAVY,SAF,CREAM='#042455','#FAAD07','#F6EEE0'
def wordmark(cx,base,size,idp,wght=800,track=2):
    f=FS.load('MontserratItalic',{'wght':wght});gs=f.getGlyphSet();cm=f.getBestCmap();sc=size/1000
    cap=700*sc;xh=f['OS/2'].sxHeight*sc;slant=math.tan(math.radians(11.3))
    x=0;paths=[];dot=None
    for ch in 'biboşluk':
        c='ı' if ch=='i' else ch
        g=cm[ord(c)];pen=SVGPathPen(gs);gs[g].draw(TransformPen(pen,(sc,0,0,-sc,x,0)));paths.append(pen.getCommands())
        if ch=='i':
            adv=gs[g].width*sc;r=size*0.1;dy=xh+size*0.09+r
            dot=(x+adv/2+slant*(dy-xh/2), -dy, r)
        x+=gs[g].width*sc+track
    W=x-track;ox=cx-W/2
    wy=-xh*0.42
    wave=f'M{-20} {wy} q15 -9 30 0 t30 0 '*1
    seg=''.join(f'q{12} {-5 if i%2==0 else 5} 24 0 ' for i in range(0,int(W/24)+4))
    wp=f'M-20 {wy:.1f} '+seg
    return f'''<defs><mask id="wm{idp}" maskUnits="userSpaceOnUse" x="-40" y="{-size}" width="{W+80:.0f}" height="{size*1.5:.0f}"><rect x="-40" y="{-size}" width="{W+80:.0f}" height="{size*1.5:.0f}" fill="#fff"/><path d="{wp}" fill="none" stroke="#000" stroke-width="{size*0.04:.1f}"/></mask></defs>
<g transform="translate({ox:.1f} {base})"><path d="{''.join(paths)}" fill="{NAVY}" mask="url(#wm{idp})"/><circle cx="{dot[0]:.1f}" cy="{dot[1]:.1f}" r="{dot[2]:.1f}" fill="{SAF}"/></g>'''
def frame(x,y,w,h,art_w,idp,stroke,inner,sun=None,text=None,sw=5,rx=6):
    ah=art_w*AH/AW;ax=x+w/2-art_w/2;ay=y+h-ah-8
    rect=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/>'
    cx=x+w/2
    sea_y=y+h-70
    sea=f'M{x} {sea_y} q{w/8} -12 {w/4} 0 t{w/4} 0 t{w/4} 0 t{w/4} 0 V{y+h} H{x}Z'
    s=''
    if sun:
        sy,sr=sun
        s=f'<circle cx="{cx}" cy="{sy}" r="{sr}" fill="{SAF}"/>'
    t=wordmark(cx,*text,idp) if text else ''
    return f'''<defs><linearGradient id="sky{idp}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#CBE8E6"/><stop offset=".7" stop-color="#DCEFEE"/><stop offset="1" stop-color="#CFE7E6"/></linearGradient><clipPath id="fc{idp}">{rect}</clipPath></defs>
<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="#D6ECEA"/>
<g clip-path="url(#fc{idp})">{s}{t}<image href="data:image/png;base64,{b64}" x="{ax:.1f}" y="{ay:.1f}" width="{art_w}" height="{ah:.1f}"/></g>
<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="none" stroke="{stroke}" stroke-width="{sw}"/>'''
for name,bg,stroke in [('logo-ana','#FFFFFF',NAVY),('logo-ana-koyu','#031A3D',CREAM)]:
    g=frame(40,40,900,660,862,name[-4:],stroke,SAF,sun=(112,28),text=(236,96))
    svg(980,740,bg,g,name)
g=frame(112,196,800,632,800,'ic',CREAM,SAF,sun=(320,42),rx=6,sw=6)
svg(1024,1024,'#031A3D','<rect width="1024" height="1024" fill="#031A3D"/>'+g,'uygulama-ikonu')
svg(1024,1024,'#FFFFFF','<defs><clipPath id="rr"><rect width="1024" height="1024" rx="228"/></clipPath></defs><g clip-path="url(#rr)"><rect width="1024" height="1024" fill="#031A3D"/>'+g.replace('id="sky','id="skyR').replace('url(#skyic','url(#skyRic')+'</g>','uygulama-ikonu-yuvarlak')
