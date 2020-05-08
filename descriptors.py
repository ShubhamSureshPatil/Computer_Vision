import cv2
import numpy as np

def surf_feature(img):
	"""
	Extract surf features
	"""
	# Set the Hessian Threshold
	surf = cv2.xfeatures2d.SIFT_create()

	# Find keypoint and descriptors
	kp, des = surf.detectAndCompute(img,None)

	print(len(des))


def main():
	img = cv2.imread('img1.jpg',1)
	cv2.imshow('Image_CMU', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	surf_feature(img)

if __name__ == '__main__':
	main()