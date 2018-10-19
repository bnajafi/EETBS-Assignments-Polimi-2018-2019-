# -*- coding: utf-8 -*-
#A first way to import the functions from the other script and solve the problem is the following

import os
import sys
thisFileDirectory = os.path.dirname(sys.argv[0])
os.chdir(thisFileDirectory)
print os.getcwd()

T_IN = 22
T_OUT = -2
DT = (T_IN - T_OUT)
A = 50*(1-0.2)*2.5

R1 = {"name":"Outside Surface","type":"conv","material":"OutsideSurfaceWinter"}
R2 = {"name":"Wood Bevel Lapped Siding","type":"cond","material":"WoodLappedSiding","length":0.013}
R3 = {"name":"Fiber Board","type":"cond","material":"WoodFiberboard","length":0.013}
R4 = {"name":"Glass Fiber Insulation","type":"cond","material":"GlassFiberInsulation","length":0.09}
R5 = {"name":"Wood Stud","type":"cond","material":"WoodStud_90mm","length":0.09}
R6 = {"name":"Gypsum Wallboard","type":"cond","material":"Gypsum","length":0.013}
R7 = {"name":"Inside Surface","type":"conv","material":"InsideSurface"}
R_gap = {"name":"Air Gap","type":"gap","epsilon1":0.05,"epsilon2":0.9,"length":0.04}  
ListWithWood = [R1,R2,R3,R5,R6,R7,R_gap] 
ListWithInsulation = [R1,R2,R3,R4,R6,R7,R_gap] 

import WallFunctions_MFerrari as WallF
ResultDictWood = WallF.ResistanceOfLayersInSeries(ListWithWood) 
RtotWood = ResultDictWood["Rtot"]

ResultDictInsulation = WallF.ResistanceOfLayersInSeries(ListWithInsulation) 
RtotInsulation = ResultDictInsulation["Rtot"]

UWood = WallF.HeatTransferCoefficient(RtotWood)
UInsulation = WallF.HeatTransferCoefficient(RtotInsulation)
UWall = UWood*0.25 + UInsulation*0.75
RWall = 1/UWall

Q = UWall*A*DT

print ("The overall heat transfer coefficient of the wall is: " + str(UWall) + " W/(m^2°C)")
print ("The overall thermal resistance of the wall is " + str(RWall) + " (m^2°C)/W")
print ("The heat flux through the wall is " + str(Q) + " W")

#The alternative way to import the functions from the other script and solve the problem is the following

from WallFunctions_MFerrari import *
ResultDictWood2 = ResistanceOfLayersInSeries(ListWithWood) 
RtotWood2 = ResultDictWood2["Rtot"]

ResultDictInsulation2 = ResistanceOfLayersInSeries(ListWithInsulation) 
RtotInsulation2 = ResultDictInsulation2["Rtot"]

UWood2 = HeatTransferCoefficient(RtotWood2)
UInsulation2 = HeatTransferCoefficient(RtotInsulation2)
UWall2 = UWood2*0.25 + UInsulation2*0.75
RWall2 = 1/UWall2

Q2 = UWall2*A*DT

print ("The overall heat transfer coefficient of the wall is: " + str(UWall2) + " W/(m^2°C)")
print ("The overall thermal resistance of the wall is " + str(RWall2) + " (m^2°C)/W")
print ("The heat flux through the wall is " + str(Q2) + " W")