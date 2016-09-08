# importing qgis core modules
from qgis.core import *

# qgis init parameters
QgsApplication.setPrefixPath("/usr", True)
qgs = QgsApplication([], True)
qgs.initQgis()

# access one layer
layer = QgsVectorLayer("data/gis.osm.transport_a_free_1.shp", "transport", "ogr")

# information about fields
for field in layer.pendingFields():
    print field.name(), field.typeName()

# close qgis parms
qgs.exitQgis()
