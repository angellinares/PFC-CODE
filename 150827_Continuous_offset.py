"""
Author: Angel Linares Garcia.
Date: 150821
Description: This scripts takes one
selected curve and creates N offsets
at D distance.
"""
##############################

import rhinoscriptsyntax as rs

strCrv0 = rs.GetCurveObject("Select curve",True)
intTimes = rs.GetInteger("Number of repetitions")
dblDist = rs.GetReal("Distance between curves")
pt0 = rs.GetPoint("Selec offset side")
rs.EnableRedraw(False)

for i in range(intTimes):
    
    newCurve = rs.OffsetCurve(strCrv0[0],pt0,dblDist*(i+1))
    strCrv = newCurve
    
rs.EnableRedraw(True)
    