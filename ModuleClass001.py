#150623 ALG
#Module Class implementation

#######################
##MODULES IMPORT
#######################

import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import Grasshopper as g
import copy

#######################
##CLASSES
#######################

class modClass():
    """Define a complementary use module
    based in general geometry data from the
    building core. 
    
    modClass(self, crvBase, width, height, nCuts, type, turn, coreN):
        
        crvBase: base curve used to build the module.
        width: module width from base curve.
        height: distance between base curve horizontal projection and module upper limit.
        nCuts: number of cuts used to build the module.
        type: module type.
        turn: turn in which the module is placed.
        coreN: core numberin turn with which the module is connected.
    
    """
    nextID = 0
    def __init__(self, crvBase, width, height, nCuts, type, turn, coreN):
        
        """Initializing instances variables
            
        """
        self.crvBase = crvBase
        self.width = width
        self.height = height
        self.nCuts = nCuts
        self.type = type
        self.turn = turn
        self.coreN = coreN
        
        #To be filled later with the information provided by the model.
        self.corePartner = None
        
        #Creates an unique ID forevery module in the current session.
        #Intorduction to computation and programing with Python. p97 
        self.ID = modClass.nextID
        modClass.nextID += 1
        
        #Creates automatically all module base geometry.
        self.modGeo
        
    def modGeo():
        
        self.createPlans()
        
    def createPlans():
            
            radius = self.crvBase.Radius
            offCrv = copy.copy(self.crvBase)
            offCrv.Radius = (radius+self.width)
            print "hola"
        
    def __str__(self):
        """ Function that substitudes str() 
        for module function """
        
        return  "-> Module " + str(self.ID) + "\n" + " || Type: " + str(self.type) + "\n" + " || Turn: " + str(self.turn) + "\n" + " || Core Partner: " + str(self.corePartner) + "\n" + " || ID: " + str(self.ID) + "\n\n" 


####################### 
##FUNCTIONS AND GLOBALS 
####################### 

a = modClass("Curve1", "10", "6", "6", "Apartment", "3", "4")
b = modClass("Curve3", "10", "6", "6", "Office", "2", "1")

print a, b