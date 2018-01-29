import sys, cv2, itertools, numpy as np 

args = sys.argv
argc = len(sys.argv)
if (argc != 2):
    print('Usage: python haikeiTouka.py filename')
    quit()

img = cv2.imread(args[1])
rows, cols = img.shape[0:2]
sheet = np.zeros((rows, cols, 4), np.uint8)
cv2.imshow('motoNoGazou', img)
for col in range(cols):
    for row in range(rows):
        sheet[row][col][0:3] = img[row, col][0:3]
        if sum(img[row, col]) <= 730:
            sheet[row][col][3] = 255
        
cv2.imshow('kakouGo', sheet)
cv2.imwrite('kakouGo.png', sheet)

cv2.waitKey(0)
cv2.destroyAllWindows()
