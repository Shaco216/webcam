import cv2
def capture_webcam():
    cap = cv2.VideoCapture(0) #0=webcam
    while(True):
        ret, frame = cap.read()
        cv2.imshow('frame', frame)#er nimmt die ressource 'frame'; als code wird auch frame übergeben -> filterfrei
        k = cv2.waitKey(1)
        if k == 27:#wenn man ab hier auskommatiert bzw. mit escape aufnahme beenden
            break

    cap.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    capture_webcam()