# coding: utf-8
# authors: Yiwen Liu, Jiemin Zhou, Jin Ma

# import arcgis module
import arcpy as ap
import os

# define the functions
# function "calRelief":
# get the terrian relief
# "demData" - the data of DEM; "reliefSize" - the window's size for FocalStatistics
def calRelief(demData, reliefSize):
    # set the rectangle for FocalStatistics
    neighborhood = ap.sa.NbrRectangle(reliefSize, reliefSize, "CELL")

    # do Maximum and Minimum FocalStatistics
    minDEM = ap.sa.FocalStatistics(demData, neighborhood, "MINIMUM", "")
    maxDEM = ap.sa.FocalStatistics(demData, neighborhood, "MAXIMUM", "")

    # get the relief raster
    diffDEM = abs(minDEM - maxDEM)

    # reclassify the dem raster by certain range
    remapRange = ap.sa.RemapRange([[-1000, 1000,1],[1000,3500,2],[3500,5000,3],[5000,10000,4]])
    demLevel = ap.sa.Reclassify(demData, "Value", remapRange, "NODATA")

    # reclassify the relief raster by certain range
    remapRange1 = ap.sa.RemapRange([[0, 30,1],[30,200,2],[200,500,3],[500,1000,4], [1000,2500,5], [2500, 10000, 6]])
    fluctuation = ap.sa.Reclassify(diffDEM, "Value", remapRange1, "NODATA")

    # get the Basic landform type by dem level and terrain relief
    result = demLevel * 10 + fluctuation

    # save the result as "relief"
    result.save("relief")


# function "calRiver"
# extract the raster river from DEM
# "demData" - the data of DEM
def calRiver(demData):
    # fill the dem, then get the flow direction and accumulation
    fillDEM = ap.sa.Fill(demData)
    flowDir = ap.sa.FlowDirection(fillDEM, "FORCE", "")
    flowAcc = ap.sa.FlowAccumulation(flowDir, "", "INTEGER")

    # classify the raster as a binary image by a certain value
    riverTemp = ap.sa.Con(flowAcc >= 3000, 1, 0)
    river = ap.sa.Reclassify(riverTemp, "Value", "0 NODATA;1 1", "NODATA")

    # save the result as "river"
    river.save("river")

# fucntion "toPdf"
# print the result as a pdf by using a example aprx
# "aprxPath" - the file path of parx file; "pdfPath" - the file path of pdf file
def toPdf(aprxPath, pdfPath, mapExtent):
    # get the aprx file
    aprx = ap.mp.ArcGISProject(aprxPath)
    
    # get the map list and layout list
    mapList = aprx.listMaps()[0]
    lyt = aprx.listLayouts()[0]

    # add "relief" and "river" to map
    mapList.addDataFromPath(wp + r"\relief")
    mapList.addDataFromPath(wp + r"\river")

    # set map extent
    mf = lyt.listElements("MAPFRAME_ELEMENT")[0]
    mf.camera.setExtent(mapExtent)

    # export to pdf
    lyt.exportToPDF(pdfPath, resolution=300)


# the main program

# get the paramenters from the tool box
# the DEM data
demData = ap.GetParameterAsText(0)
# the size for Focal Statisitics
reliefSize = int(ap.GetParameterAsText(1))
# the file path of the example aprx file
aprxPath = ap.GetParameterAsText(2)
# the file path of the output pdf file
pdfPath = aprx = ap.GetParameterAsText(3)

print("Start the preparation")
# get the workspace
wp = ap.env.workspace
ap.env.overwriteOutput = True

# describe the DEM data
desc = ap.Describe(demData)

print("do the calculation")
# do the calculation
calRelief(demData, reliefSize)
calRiver(demData)

print("export to the pdf file")
# print to pdf
toPdf(aprxPath, pdfPath, desc.extent)

# open the pdf
os.startfile(pdfPath)



