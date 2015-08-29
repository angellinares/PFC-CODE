import ModuleClass003 as md
import Rhino.Geometry as rg

reload(md)

mods = []
a = []
cen = []
dict = {}
info = []

for i in range(len(c)):
    mod = md.modClass(c[i],w,h,nCuts,Info[i]["Type"],Info[i]["Turn"],Info[i]["Core"])
    a.append(mod.modGeo())
    cen.append(mod.planCentroid)
    mods.append(mod)

"""
Building core partner information and binding it 
to modules.
"""
for m1 in mods:
    
    for m2 in mods:
        
        if (m1 != m2) and m1.coreN == m2.coreN:
            m1.corePartner = m2.ID
            m2.corePartner = m1.ID
            break


#printing module info
for m in mods:
    print m     
            
area = rg.AreaMassProperties.Compute(a[0])
dict["Area"] = area.Area
info.append(dict)       