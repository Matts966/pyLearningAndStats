import sys, cv2, itertools, numpy as np 
from numpy.random import *

args = sys.argv
argc = len(sys.argv)
if (argc != 2):
    print('Usage: python vss.py filename')
    quit()

w = 255
b = 0
h = 163
permn = 24

perm = [(int(i[0]), int(i[1]), int(i[2]), int(i[3])) for i in itertools.permutations('0123')]
vssb = [[b,b,w,w],
        [w,w,b,b]]
vssp = [ [0, 0], [0, 1] ]

img = cv2.imread(args[1], 0)
rows, cols = img.shape
sheet0 = np.zeros((rows*2, cols*2), np.uint8)
sheet1 = np.zeros((rows*2, cols*2), np.uint8)
sheet2 = np.zeros((rows*2, cols*2), np.uint8)
imageMat = np.zeros((rows*2, cols*2, 4), np.uint8)
imageMat2 = np.zeros((rows*2, cols*2, 4), np.uint8)

img2 = cv2.imread(args[1])
cv2.imshow('img2', img2)
imageMat3 = np.zeros((rows, cols, 4), np.uint8)

for col in range(0, cols):
    for row in range(0, rows):
        imageMat3[row][col][0] = img2[row, col][0]
        imageMat3[row][col][1] = img2[row, col][1]
        imageMat3[row][col][2] = img2[row, col][2]
        if sum(img2[row, col]) <= 730:
            imageMat3[row][col][3] = 255
        patt = 0 if img[row, col] > h else 1
        rand = randint(permn)
        sheet0[row*2,   col*2  ] = vssb[vssp[patt][0]][perm[rand][0]]
        sheet0[row*2,   col*2+1] = vssb[vssp[patt][0]][perm[rand][1]]
        sheet0[row*2+1, col*2  ] = vssb[vssp[patt][0]][perm[rand][2]]
        sheet0[row*2+1, col*2+1] = vssb[vssp[patt][0]][perm[rand][3]]
        sheet1[row*2,   col*2  ] = vssb[vssp[patt][1]][perm[rand][0]]
        sheet1[row*2,   col*2+1] = vssb[vssp[patt][1]][perm[rand][1]]
        sheet1[row*2+1, col*2  ] = vssb[vssp[patt][1]][perm[rand][2]]
        sheet1[row*2+1, col*2+1] = vssb[vssp[patt][1]][perm[rand][3]]
        sheet2[row*2,   col*2  ] = min(vssb[vssp[patt][1]][perm[rand][0]], vssb[vssp[patt][0]][perm[rand][0]])
        sheet2[row*2,   col*2+1] = min(vssb[vssp[patt][1]][perm[rand][1]], vssb[vssp[patt][0]][perm[rand][1]])
        sheet2[row*2+1, col*2  ] = min(vssb[vssp[patt][1]][perm[rand][2]], vssb[vssp[patt][0]][perm[rand][2]])
        sheet2[row*2+1, col*2+1] = min(vssb[vssp[patt][1]][perm[rand][3]], vssb[vssp[patt][0]][perm[rand][3]])


        pat0 = vssb[vssp[patt][0]]
        pat1 = vssb[vssp[patt][1]]
        imageMat[row*2,   col*2  ] = [pat0[perm[rand][0]]] * 3 + [255-pat0[perm[rand][0]]]       
        imageMat[row*2,   col*2+1] = [pat0[perm[rand][1]]] * 3 + [255-pat0[perm[rand][1]]] 
        imageMat[row*2+1, col*2  ] = [pat0[perm[rand][2]]] * 3 + [255-pat0[perm[rand][2]]]
        imageMat[row*2+1, col*2+1] = [pat0[perm[rand][3]]] * 3 + [255-pat0[perm[rand][3]]]
        imageMat2[row*2,   col*2  ] = [pat1[perm[rand][0]]] * 3 + [255-pat1[perm[rand][0]]]
        imageMat2[row*2,   col*2+1] = [pat1[perm[rand][1]]] * 3 + [255-pat1[perm[rand][1]]]
        imageMat2[row*2+1, col*2  ] = [pat1[perm[rand][2]]] * 3 + [255-pat1[perm[rand][2]]]
        imageMat2[row*2+1, col*2+1] = [pat1[perm[rand][3]]] * 3 + [255-pat1[perm[rand][3]]]

cv2.imshow('alpha', imageMat)
cv2.imshow('alpha2', imageMat2)
cv2.imwrite('alpha.png', imageMat)
cv2.imwrite('alpha2.png', imageMat2)

cv2.imshow('img2skel', imageMat3)
cv2.imwrite('img2skel.png', imageMat3)


cv2.imshow('sheet0', sheet0)
cv2.imshow('sheet1', sheet1)
cv2.imshow('sheet2', sheet2)
cv2.imwrite('sheet0.png', sheet0)
cv2.imwrite('sheet1.png', sheet1)
cv2.imwrite('sheet2.png', sheet2)
cv2.waitKey(0)
cv2.destroyAllWindows()
