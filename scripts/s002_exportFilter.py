# importing qgis core modules
from qgis.core import *

# qgis init parameters
QgsApplication.setPrefixPath("/usr", True)
qgs = QgsApplication([], True)
qgs.initQgis()

# define file
inputFile = "data/gis.osm.transport_a_free_1.shp"
outputFile = "out/output_ferryTerminals.shp"

# access transport layer
layer = QgsVectorLayer(inputFile, "transport", "ogr")

# init filter
exp = "fclass = 'ferry_terminal'"
ferryFeaturesSubselection = layer.getFeatures(QgsFeatureRequest().setFilterExpression(exp))

# apply filter
layer.setSelectedFeatures([feature.id() for feature in ferryFeaturesSubselection])
print "Filter applied."

# copy selected filter to a new file
QgsVectorFileWriter.writeAsVectorFormat(layer, outputFile, "utf-8", None, "ESRI Shapefile", True) # onlySelected = True
print "Output file created."

# close qgis parms
qgs.exitQgis()
