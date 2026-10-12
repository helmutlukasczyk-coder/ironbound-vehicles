from pathlib import Path
import json, math, re, xml.etree.ElementTree as E, subprocess
from collections import Counter
ROOT=Path(__file__).resolve().parent
stock=json.loads((ROOT/'stock-data.json').read_text())
VALUES={'AC/2':(403,1086400),'Bulldog':(605,1272800),'Condor':(653,1289000),'Demolisher':(981,2079000),'Hetzer':(574,664000),'J. Edgar':(544,729250),'LRM':(833,1872000),'Manticore':(993,2640800),'Pegasus':(640,865725),'Saladin':(596,911625),'Savannah':(215,91667),'Schrek':(935,3829500),'Scorpion':(306,327083),'SRM':(816,1932800),'Striker':(564,563315),'Vedette':(475,725750)}
ORDER=list(VALUES)
ROLES={'Brawler':'Brawler','Juggernaut':'Brawler','Scout':'Scout','Striker':'Skirmisher','Ambusher':'Brawler','Sniper':'Fire Support','Missile Boat':'Fire Support'}
WEAPONS={'Autocannon/2':('AC/2',2,[4,2,0,2,4],45),'Autocannon/5':('AC/5',5,[2,0,2,4,None],20),'Autocannon/20':('AC/20',20,[0,0,2,None,None],5),'Medium Laser':('Medium Laser',5,[0,0,2,None,None],0),'Large Laser':('Large Laser',8,[0,0,2,4,None],0),'PPC':('PPC',10,[2,0,2,4,None],0),'Machine Gun':('Machine Gun [AI]',2,[0,0,None,None,None],200)}
for rack in [2,4,6]:WEAPONS[f'SRM {rack}']=(f'SRM-{rack}',rack*2,[0,0,2,None,None],{2:50,4:25,6:15}[rack])
for rack in [10,20]:WEAPONS[f'LRM {rack}']=(f'LRM-{rack} [IF]',rack,[4,2,0,2,4],{10:12,20:6}[rack])
N='http://www.w3.org/2000/svg'; E.register_namespace('',N)
dark='#243540';muted='#61717c';accent='#a45426'
profiles=[]
for key in ORDER:
 d=next(v for v in stock if v['Name'].startswith(key));mass=int(float(d['tonnage']));move=int(d['cruiseMP']);armor=[max(1,math.floor(int(x)/4+.5)) for x in d['armor'].split()];turret=len(armor)==5;structure=max(1,math.floor(math.ceil(mass/10)/3+.5));tmm=next(i for i,lim in enumerate([2,4,6,9,17,999]) if move<=lim)
 ev,cv=VALUES[key]; groups=[]
 for loc in ['Front','Right','Left','Rear','Turret']:
  for weapon,count in Counter(d['equipment'][loc]).items():
   # Similar weapon types share a TIC where Override permits it.
   chunks=[]
   if weapon=='SRM 6' and count==10:chunks=[3,3,2,2]
   elif weapon=='LRM 20' and count==3:chunks=[2,1]
   elif weapon in ['PPC','Autocannon/20']:chunks=[1]*count
   else:chunks=[count]
   for n in chunks:
    label,tw,ranges,cap=WEAPONS[weapon];base=math.ceil(tw*n/3);mdice=0
    if weapon.startswith(('SRM','LRM')):
     rack=int(weapon.split()[1]);base=n*(max(1,rack//10) if weapon.startswith('LRM') else 1);mdice=n*math.ceil(rack/(10 if weapon.startswith('LRM') else 4))
    maxdamage=math.ceil(tw*n/3)
    assert (base<=5 and maxdamage<=14) or n==1
    groups.append(dict(weapon=weapon,count=n,label=(str(n)+'× ' if n>1 else '')+label,damage=f'{base}+M{mdice} ({maxdamage})' if mdice else str(base),base=base,max=maxdamage,mdice=mdice,location=loc,ranges=ranges))
 assert sum(g['count'] for g in groups)==sum(len(d['equipment'][l]) for l in ['Front','Left','Right','Rear','Turret'])
 bins=[]
 for item in d['equipment']['Body']:
  if 'Ammo' not in item:raise ValueError(item)
  typ='Machine Gun' if ('MG' in item or 'Machine Gun' in item) else 'Autocannon/'+re.search(r'AC/(\d+)',item).group(1) if 'AC/' in item else re.search(r'(LRM|SRM)-(\d+)',item).group(0).replace('-',' ')
  ids=[i+1 for i,g in enumerate(groups) if g['weapon']==typ];cap=100 if 'Half' in item else WEAPONS[typ][3]
  assert ids and cap>0
  bins.append(dict(weapon=typ,tics=ids,capacity=cap))
 slug={'AC/2':'AC2-Carrier','J. Edgar':'J-Edgar','LRM':'LRM-Carrier','SRM':'SRM-Carrier','Savannah':'Savannah-Master','Schrek':'Schrek-PPC-Carrier'}.get(key,key)
 filename=f'IRONBOUND-{slug}-'+('Mk-II' if key=='Demolisher' else 'Standard')+'.svg'
 p=dict(name=d['Name'],variant='Mk. II' if key=='Demolisher' else 'Standard',file=filename,mass=mass,year=int(d['year']),movement=d['motion_type'],ground=move,sprint=math.ceil(move*1.5),tmm=tmm,initiative=tmm,role=ROLES[d['role']],armor=armor,structure=structure,ev=ev,cv=cv,upkeep=mass*10,groups=groups,bins=bins,mul_id=d['mul id:'])
 profiles.append(p)
 r=E.Element('{'+N+'}svg',{'width':'277mm','height':'183mm','viewBox':'0 0 1000 660','role':'img','aria-labelledby':'title desc'})
 E.SubElement(r,'{'+N+'}title',{'id':'title'}).text='IRONBOUND — '+d['Name']+' — '+p['variant']
 E.SubElement(r,'{'+N+'}desc',{'id':'desc'}).text='Ground vehicle record. Override tactical conversion; IRONBOUND criticals and movement. EV uses standard BV2 G4/P5; crew paid separately.'
 g=E.SubElement(r,'{'+N+'}g',{'font-family':'DejaVu Sans, Arial, sans-serif'})
 def el(tag,**a):return E.SubElement(g,'{'+N+'}'+tag,{k.replace('_','-'):str(v) for k,v in a.items()})
 def tx(x,y,s,size=11,b=False,color=dark,anchor='start'):
  a=el('text',x=x,y=y,font_size=size,fill=color,text_anchor=anchor);a.text=str(s)
  if b:a.set('font-weight','bold')
  return a
 def rect(x,y,w,h,fill='#fff',stroke='none',rx=0):return el('rect',x=x,y=y,width=w,height=h,fill=fill,stroke=stroke,rx=rx)
 def line(x,y,x2,y2):el('path',d=f'M{x} {y}L{x2} {y2}',fill='none',stroke='#83919a')
 def check(x,y):rect(x,y,11,11,'#fff','#536572')
 def bar(x,y,w,s):rect(x,y,w,24,dark);tx(x+8,y+16,s,11,True,'#fff')
 def pips(cx,cy,n,cols=4,color=dark):
  for i in range(n):
   row=i//cols;k=min(cols,n-row*cols);col=i%cols
   el('circle',cx=cx+(col-(k-1)/2)*14,cy=cy+row*15,r=5.5,fill='#fff',stroke=color,stroke_width=1.7)
 rect(0,0,1000,660)
 tx(22,26,'IRONBOUND',14,True);tx(143,26,'UNIT RECORDS / GROUND VEHICLE',10,color=muted)
 title={'AC/2':'AC/2 CARRIER','J. Edgar':'J. EDGAR','LRM':'LRM CARRIER','SRM':'SRM CARRIER','Savannah':'SAVANNAH MASTER','Schrek':'SCHREK PPC CARRIER'}.get(key,key.upper())
 tx(22,59,title,28,True);tx(22,80,p['variant'].upper(),16,True,accent);tx(135,80,f'INNER SPHERE / {p["movement"].upper()} / INTRO {p["year"]}',10,color=muted)
 tx(613,29,'CREW',11,True,accent);line(657,31,864,31);tx(880,29,'ID:',10);line(901,31,975,31)
 tx(613,57,'Gunnery');line(666,59,698,59);tx(730,57,'Piloting');line(782,59,815,59)
 tx(613,81,'Injuries',10)
 for i in range(6):check(660+16*i,71)
 tx(776,81,'Acquired',10);line(829,83,975,83)
 tx(613,101,'Crew names:',10);line(690,103,975,103)
 bar(22,106,310,'UNIT DATA');bar(344,106,246,'MOTIVE DAMAGE')
 for y,k,v in [(145,'Mass',f'{mass} tons'),(168,'Ground / Sprint',f'{move} / {p["sprint"]} inches'),(191,'Base TMM / Initiative',f'{tmm} / {tmm}'),(214,'Movement type',p['movement']+' ('+{'Tracked':'t','Hover':'h','Wheeled':'w'}[p['movement']]+')'),(237,'Catalogue role',p['role'])]:tx(30,y,k,12);tx(200,y,v,12,True)
 tx(352,145,'Motive hits:',11)
 for i in range(math.ceil(move/2)):check(429+i*20,134)
 tx(352,167,'Each hit: Ground Move −2″; TMM −1.',10)
 tx(352,188,'Current Ground:',10);line(440,190,479,190);tx(489,188,'TMM:',10);line(524,190,577,190)
 check(352,204);tx(369,214,'Immobilized',10);check(470,204);tx(487,214,'Crew Stunned',10)
 tx(352,237,'Initiative remains at the printed base bracket.',9,color=muted)
 rect(22,251,565,18,dark);tx(34,263,'WEAPON TICS',12,True,'#fff')
 cols=[27,257,363,405,449,481,513,545,578]
 for x,s in zip(cols,['TIC / WEAPON','DAMAGE','ARC','LOC','PB','S','M','L','X']):tx(x,282,s,10,True,muted)
 for i in range(8):
  y=303+20*i;rect(22,y-14,565,20,'#e8e9e7' if i%2==0 else '#fff')
  if i>=len(groups):continue
  a=groups[i];vals=[f'{i+1}  '+a['label'],a['damage'],'360°' if a['location']=='Turret' else a['location'],{'Turret':'TU','Front':'FR','Right':'RS','Left':'LS','Rear':'RE'}[a['location']],*[f'+{n}' if n is not None else '—' for n in a['ranges']]]
  for x,s in zip(cols,vals):tx(x,y,s,9 if x in (257,363,405) else 11,x==27)
 tx(27,475,'AI: anti-infantry. IF: indirect fire. TU: turret; FR: front; BD: body.',9,color=muted)
 tx(29,498,'Weapon losses / TIC:',10)
 for i in range(len(groups)):check(164+i*51,488);tx(181+i*51,498,str(i+1),11,True)
 tx(22,512,'AMMUNITION / SHARED BINS' if bins else 'AMMUNITION: NONE',11,True)
 if bins:
  for x in [22,307]:
   tx(x,526,'TIC / AMMO (LOC)',9,True);tx(x+138,526,'SHOTS',9,True);tx(x+251.5,526,'Destroyed',9,anchor='middle')
  percol=math.ceil(len(bins)/2)
  for i,b in enumerate(bins):
   x=22+285*(i//percol);y=540+13*(i%percol);label=WEAPONS[b['weapon']][0].replace(' [AI]','').replace(' [IF]','').replace('Machine Gun','MG')
   tx(x,y,','.join(map(str,b['tics']))+' · '+label+' (BD)',10,True);tx(x+138,y,'______ / '+str(b['capacity']),10);check(x+246,y-10)
  tx(22,568,'Each row is one bin; shared by listed TICs. Spend 1 shot per weapon fired.',9)
 else:tx(22,540,'All weapon TICs use energy weapons; no ammunition bins.',10)
 tx(22,582,'Equipment: '+('Fusion' if d['engine_type']=='0' else 'ICE')+' engine; standard structure; standard armor; '+('turret.' if turret else 'no turret.'),9.5,color=muted)
 bar(613,120,362,'ARMOR AND STRUCTURE');tx(794,160,'Black: armor · Red: structure',10,anchor='middle')
 rect(708,183,172,277,'#d1d6d7',dark,10)
 if p['movement']=='Tracked':
  for x in [681,886]:
   rect(x,198,22,253,'#536572',dark,3)
   for y in range(207,446,13):line(x,y,x+22,y)
 elif p['movement']=='Wheeled':
  for x in [681,886]:
   for y in [206,298,390]:rect(x,y,22,54,'#536572',dark,5)
 else:
  for x in [681,886]:rect(x,194,22,260,'#aebbc0',dark,10)
 el('path',d='M716 194L872 194L851 270L737 270Z',fill='#b8c1c4',stroke=dark)
 el('path',d='M716 201L754 270L754 391L716 444Z',fill='#c4cbce',stroke=dark)
 el('path',d='M872 201L834 270L834 391L872 444Z',fill='#c4cbce',stroke=dark)
 el('path',d='M737 400L851 400L872 459L716 459Z',fill='#b8c1c4',stroke=dark)
 if turret:rect(786,249,16,74,'#536572',dark,3);rect(753,292,82,98,'#aebbc0',dark,14)
 pips(794,208,armor[0]);pips(759,255,structure,color='#b13737')
 pips(735,283,armor[2],2);pips(735,357,structure,2,color='#b13737')
 pips(853,283,armor[1],2);pips(853,357,structure,2,color='#b13737')
 if turret:pips(794,309,armor[4]);pips(794,356,structure,3,color='#b13737');tx(794,382,'Turret (5, 9)',9.5,True,anchor='middle')
 pips(794,412,armor[3]);pips(794,448,structure,3,color='#b13737')
 tx(794,178,'Front (6–8)',10,True,anchor='middle');tx(672,278,'Left Side',10,True,anchor='end');tx(672,293,'(10–11)' if turret else '(9–11)',10,anchor='end');tx(918,278,'Right Side',10,True);tx(918,293,'(3–4)' if turret else '(3–5)',10)
 tx(794,481,'Rear (6–8; rear attack)',10,True,anchor='middle')
 tx(613,508,'2 / 12: Floating Critical; reroll location.',10);tx(613,529,'Any location reduced to 0 Structure: destroyed.',10)
 tx(613,551,'Footprint:',10);line(672,553,708,553);tx(716,551,'×',10);line(730,553,768,553);tx(776,551,'inches (declare before deployment)',9)
 tx(613,572,'Critical effects:',10);line(699,574,975,574);line(613,591,975,591)
 rect(22,604,953,27,'#e8ebea')
 for x,s in [(29,'Destroyed'),(177,'Crew unconscious'),(382,'Abandoned')]:tx(x,622,s,10);check(x+len(s)*6+9,611)
 tx(613,622,'Injury checks: 3+ / 5+ / 7+ / 9+ / 11+ / Incap.',9)
 line(22,637,975,637);tx(22,652,f'EV {ev}',10,True);tx(115,652,f'CV {cv:,} C-bills',10,True);tx(365,652,f'Upkeep {mass*10}/day + crew 500/day',9,color=muted);tx(975,652,'EV reference: Gunnery 4 / Piloting 5',9,color=muted,anchor='end')
 f=ROOT/filename;f.write_text(E.tostring(r,encoding='unicode'));E.parse(f)
 assert len(r.findall('.//{'+N+'}circle'))==sum(armor)+structure*len(armor)
 subprocess.run(['inkscape',str(f),'--export-type=png',f'--export-filename={ROOT/"cards-preview"/(filename[:-4]+".png")}','--export-width=1500'],check=True,capture_output=True)
(ROOT/'profiles.json').write_text(json.dumps(profiles,indent=2)+'\n')
print(f'Generated and rendered {len(profiles)} cards; weapon counts, TIC limits, ammunition links and pip counts passed.')
