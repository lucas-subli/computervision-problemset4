# USAGE
# python problem2.py --image image/image1.jpg

# import the necessary packages
import numpy as np
import argparse
import cv2


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image to be scanned")
ap.add_argument("-sr", "--spatialRadius", required = True,
	help = "Spacial Radius", type=float)
ap.add_argument("-cr", "--colorRadius", required = True,
	help = "Color Radius", type=float)
ap.add_argument("-L", "--maxLevel", required = True,
	help = "Levels in the image pyramid", type=int)
args = vars(ap.parse_args())


#Loading the image and making it a grey level one
image = cv2.imread(args["image"])
sr = args["spatialRadius"]
cr = args["colorRadius"]
maxLvl = args["maxLevel"]

output = cv2.pyrMeanShiftFiltering(image, sr, cr, maxLevel = maxLvl)
output = cv2.pyrMeanShiftFiltering(output, sr, cr, maxLevel = maxLvl)
output = cv2.pyrMeanShiftFiltering(output, sr, cr, maxLevel = maxLvl)
output = cv2.pyrMeanShiftFiltering(output, sr, cr, maxLevel = maxLvl)
output = cv2.pyrMeanShiftFiltering(output, sr, cr, maxLevel = maxLvl)


cv2.imshow("Output", np.hstack((image, output)))
cv2.waitKey(0)

cv2.destroyAllWindows()