#150606 ALG
#Creates cores, ramp and support layout.

import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import Grasshopper as g

#######################
##FUNCTIONS AND GLOBALS
#######################

#pExt = []
#pInt = []
auxIntPts = []
auxExtPts = []
#extArcs = []
#intArcs = []

#Declare an universal DataTree
dSlope = g.DataTree[object]()
pSect = g.DataTree[object]()
pSupExt = g.DataTree[object]()
#lnSupIxt = g.DataTree[object]()
pExt = g.DataTree[rg.Point3d]()
pInt = g.DataTree[rg.Point3d]()
extArcs = g.DataTree[object]()
intArcs = g.DataTree[object]()
cPedAux = g.DataTree[object]()
pPed = g.DataTree[rg.Point3d]()
cParkAux = g.DataTree[object]()
pPark = g.DataTree[rg.Point3d]()
arcPed = g.DataTree[object]()
arcPark = g.DataTree[object]()

testRad = pedOff+parkOff+laneWidth
R2 = R1 - testRad


if R1 < testRad:
    R1 = testRad
    R2 = 0.01
    print "Coerced R1"

##############
##############

def createSupPt (origin, nCores,nFloors,rad1,rad2,hP,ang):
    
    for i in range((nCores*nFloors)+1):
        ptO = rs.PointAdd(origin, (0,0,hP*i/nCores))
        
        pt1 = rs.Polar(ptO,(360*i/nCores),rad1)
        pt1AuxA = rs.Polar(ptO,(360*i/nCores)+ang,rad1)
        pt1AuxB = rs.Polar(ptO,(360*i/nCores)-ang,rad1)
        
        pt2 = rs.Polar(ptO,(360*i/nCores),rad2)
        pt2AuxA = rs.Polar(ptO,(360*i/nCores)+ang,rad2)
        pt2AuxB = rs.Polar(ptO,(360*i/nCores)-ang,rad2)
        
        #pExt.append(pt1)
        pExt.Add(pt1,g.Kernel.Data.GH_Path(i//nCores))
        auxExtPts.extend([pt1AuxA,pt1AuxB])
        arc1 = rs.AddArc3Pt(pt1AuxA,pt1AuxB,pt1)
        #arc drawing pedestrian path in core area
        arcPed.Add(rs.OffsetCurve(arc1,origin,pedOff)[0],g.Kernel.Data.GH_Path(i//nCores))
        arcPark.Add(rs.OffsetCurve(arc1,origin,pedOff+parkOff)[0],g.Kernel.Data.GH_Path(i//nCores))
        
        #extArcs.append(arc1)
        extArcs.Add(arc1,g.Kernel.Data.GH_Path(i//nCores))
        
        #pInt.append(pt2)
        pInt.Add(pt2,g.Kernel.Data.GH_Path(i//nCores))
        auxIntPts.extend([pt2AuxA,pt2AuxB])
        arc2 = rs.AddArc3Pt(pt2AuxA,pt2AuxB,pt2)
        #intArcs.append(arc2)
        intArcs.Add(arc2,g.Kernel.Data.GH_Path(i//nCores))
        
        pSupExt.AddRange([pt1AuxA,pt1AuxB,pt2AuxA,pt2AuxB],g.Kernel.Data.GH_Path(i//nCores))

        
def createHelix (origin, nCores, nFloors, rad, ped, park, ptH, hP, subD, ang, counter):
    
    helixPed = []
    helixPark = []
    helixPts = []
    curves = g.DataTree[object]()
    pHelix = g.DataTree[rg.Point3d]()
    
    angRamp = 360/nCores
    
    for j in range(nCores*nFloors):
        for i in range(subD+1):
            #Variable data
            tetha = (((angRamp-(2*ang))/subD)*i)+ang+(angRamp*j)
            zVect = (hP*i/(nCores*(subD)))+(hP*j/nCores)
            #print "zVect: " + str(zVect) + " , " + "J: " + str(j) + " , " + "I: " + str(i)
            
            pt0 = rs.PointAdd(origin,(0,0,zVect))
            
            pt = rs.Polar(pt0,tetha,rad)
            ptPed = rs.Polar(pt0,tetha,rad-pedOff) #Pedestrian points
            ptPark = rs.Polar(pt0,tetha,rad-pedOff-parkOff) #Carpark points
            
            helixPts.append(pt)
            helixPed.append(ptPed)
            helixPark.append(ptPark)
        
        if j < 1:
            slope = slopeCalc(helixPts[0],helixPts[1])
            #print slope
            
        curves.Add(rs.AddInterpCurve(helixPts),g.Kernel.Data.GH_Path(j//nCores))
        if ptH:
            pHelix.AddRange(helixPts,g.Kernel.Data.GH_Path(counter,j)) #Points to calculate ramp srf
        
        if ped:
            cPedAux.Add(rs.AddInterpCurve(helixPed),g.Kernel.Data.GH_Path(counter,j//nCores))
            pPed.AddRange(helixPed,g.Kernel.Data.GH_Path(counter,j)) #Points to calculate ramp srf
        if park:
            cParkAux.Add(rs.AddInterpCurve(helixPark),g.Kernel.Data.GH_Path(counter,j//nCores))
            pPark.AddRange(helixPark,g.Kernel.Data.GH_Path(counter,j)) #Points to calculate park srf
            
        #Passing points calculated to an ordered Output
        pSect.AddRange(helixPts,g.Kernel.Data.GH_Path(counter,j)) #Points to calculate ramp srf
        #Reset the point list
        helixPts = []
        helixPed = []
        helixPark = []
        
        
    return (curves,slope,cPedAux,cParkAux,pHelix)
    

def slopeCalc(p1,p2):
    
    pt1 = rs.coerce3dpoint(p1)
    pt2 = rs.coerce3dpoint(p2)
    
    h = pt2.Z-pt1.Z
    pt2.Z = pt1.Z
 
    dist = pt1.DistanceTo(pt2)
    #print dist
    slope = h*100/dist
    
    return slope


def graphOutput():
    return
    
    
    
#######################
##EXECUTION
#######################

createSupPt (O,NC,NF,R1,R2,h,aCore)
#pCrvExt = createHelix (O,NC,NF,R1,h,Sub) #Non-flat-core version
#pCrvInt = createHelix (O,NC,NF,R2,h,Sub)

#createHelix returns a list (first item = crv, second = slope)
hExt = createHelix (O,NC,NF,R1,True,True,False,h,Sub,aCore,0)
hInt = createHelix (O,NC,NF,R2,False,False,True,h,Sub,aCore,1)
cExt = hExt[0]
cInt = hInt[0]
cPed = hExt[2]
cPark = hExt[3]
pCrvInt = hInt[4]
dSlope.AddRange(("Ext.Slope: " + str("%.2f" % hExt[1])+"%",("Int.Slope: "+ str("%.2f" % hInt[1])+ "%")))


#pExt = supExtPts
#pInt = supIntPts
pAuxExt = auxExtPts
pAuxInt = auxIntPts

