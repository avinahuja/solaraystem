import cv2
img = cv2.imread('solar-system.jpg')

cv2.putText(img,
            'SUN',
            (20,400),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,255,0))

cv2.putText(img,
            'MERCURY',
            (110,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,255,0))

cv2.putText(img,
            'VENUS',
            (190,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,255,0))

cv2.putText(img,
            'EARTH',
            (285,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,255,0))

cv2.putText(img,
            'MARS',
            (385,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,255,0))

cv2.putText(img,
            'JUPITER',
            (520,225),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,255,0))

cv2.putText(img,
            'SATURN',
            (770,225),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,255,0))

cv2.putText(img,
            'URANUS',
            (965,225),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,255,0))

cv2.putText(img,
            'NEPTUNE',
            (1100,225),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,255,0))

cv2.imshow('THINGY', img)
cv2.waitKey(5000)