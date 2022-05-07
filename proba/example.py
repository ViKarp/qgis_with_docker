import sys
print("ABCBCB")
from qgis.core import *

def print_points(path):
	app = QgsApplication([], True)
	app.setPrefixPath("/usr/share/qgis", True)
	app.initQgis()

	path_to_layer = path
	vlayer = QgsVectorLayer(path_to_layer, "Airports layer", "ogr")
	if not vlayer.isValid():
		print("Layer failed to load!")

	for feature in vlayer.getFeatures():
		if (feature.hasGeometry()):
			print(feature.geometry())

	app.exitQgis()
def print_nearest_points(path, x, y):
	app = QgsApplication([], True, None)
	app.setPrefixPath("/usr/share/qgis", True)
	app.initQgis()


	vlayer = QgsVectorLayer(path, "Airports layer", "ogr")
	if not vlayer.isValid():
		print("Layer failed to load!")

	key = QgsGeometry.fromPointXY(QgsPointXY(x, y))

	for feature in vlayer.getFeatures():
		if (feature.hasGeometry()):
			p = feature.geometry().nearestPoint(key).asPoint()
			print(str(p.x()) + ' ' + str(p.y()))

	app.exitQgis()
var1 = sys.argv[1]
if var1 == "print_points":
	print_points(sys.argv[2])
elif var1 == "print_nearest_points":
	print_nearest_points(sys.argv[2], float(sys.argv[3]), float(sys.argv[4]))