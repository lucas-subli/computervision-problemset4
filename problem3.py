import numpy as np
import argparse
import cv2


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image to be scanned")
args = vars(ap.parse_args())


#Loading the image and making it a grey level one
image = cv2.imread(args["image"])
height, width = image.shape[:2]

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
tret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

#calculate the Loines by using the hough probabilistic algorithm
lines = cv2.HoughLinesP(image=thresh,rho=1,theta=np.pi/500, threshold=10, minLineLength=25, maxLineGap=10)

#Draw the lines
linesDrawing = np.ones((height,width,3))

#For each line in the resulting set
print(lines)
for line in lines:
	x1,y1,x2,y2 = line[0]
	print(str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2))
	cv2.line(linesDrawing,(x1,y1),(x2,y2),(0,255,0),2)



# find Harris corners
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)

# find centroids
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

# Now draw them
res = np.hstack((centroids,corners))
res = np.int0(res)
image[res[:,1],res[:,0]]=[0,0,255]
image[res[:,3],res[:,2]] = [0,255,0]



# show the images
cv2.imshow("Image", image)
cv2.imshow("Lines", linesDrawing)

cv2.waitKey(0)



#destroy all windows
cv2.destroyAllWindows()

