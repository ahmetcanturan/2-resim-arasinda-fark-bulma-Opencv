import cv2
img=cv2.imread("input.png")
## İki farklı resim tek bir resimde olduğundan resmi 2 ye böldük
y_uzunlugu=img.shape[0]
yarisi=int(y_uzunlugu/2)
roi1=img[0:(yarisi-3),0:635] ### Resimlerde tam boyutsal eşitlik olmadığı için test ederek 3 piksel çıkarttık
roi2=img[yarisi+3:(852),0:635]
fark = cv2.absdiff(roi1, roi2)
fark_gray=cv2.cvtColor(fark,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(fark_gray, (15, 15), 0)
_,th=cv2.threshold(blur,27,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    (x, y, w, h) = cv2.boundingRect(cnt)
    cv2.rectangle(roi2, (x-5, y-5), (x + w+10, y + h+10), (0, 255, 0), 2)
    cv2.rectangle(roi1, (x - 5, y - 5), (x + w + 10, y + h + 10), (0, 255, 0), 2)
cv2.imshow("1.Resim",roi1)
cv2.imshow("2.Resim",roi2)
cv2.waitKey()
cv2.destroyAllWindows()