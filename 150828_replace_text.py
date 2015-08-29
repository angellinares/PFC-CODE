"""
Author: Angel Linares Garcia.
Date: 150821
Description: This scripts takes one
selected curve and creates N offsets
at D distance.
"""
##############################

import rhinoscriptsyntax as rs

text = rs.GetObjects("Select text",512,False,True)
strTarget = rs.GetString("Text to search")
strReplace = rs.GetString("Text to use")
print text


for t in text:
    if rs.IsText(t):
        str0 = rs.TextObjectText(t)
        strNew = str0.replace(strTarget,strReplace)
        rs.TextObjectText(t,strNew)