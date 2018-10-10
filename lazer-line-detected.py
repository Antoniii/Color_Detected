import cv2
import numpy as np 

img = cv2.imread('photo.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.png', gray)
edges = cv2.Canny(gray, 100, 200)
cv2.imwrite('edges.png', edges)
minLineLenght = 50
maxLineGap = 20
lines = cv2.HoughLinesP(edges, 0.05, np.pi/5000, 10, minLineLenght, maxLineGap)
print(len(lines))

for i in range(len(lines)):
	x1, y1, x2, y2 = lines[i][0]
	cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 2)

cv2.imwrite('houghlines5.png', img)