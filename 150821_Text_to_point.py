"""
Author: Ángel Linares García.
Date: 150821
Description: This scripts takes 
selected text objects in Rhino and creates
3dpoints located at the height contained in 
the text object.
"""
##############################


import rhinoscriptsyntax as rs

numbers = rs.GetObjects("Select text containing topography data",512,False,True)

for n in numbers:
    
    height = rs.TextObjectText(n)
    a = height.replace(",",".")
    #print repr(a)
    #print float(height)
    pt = rs.TextObjectPoint(n)
    
    rs.AddPoint(pt.X,pt.Y,float(a))