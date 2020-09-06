# pip install opencv-python

import  cv2

class MobileCamera:
    def getVideo(self, camera):
        self.camera=camera
        cap= cv2.VideoCapture(self.camera)

        while True:
            ret, frame= cap.read()

            cv2.imshow("Mobile Cam", frame)

            if cv2.waitKey(1) == ord('q'):  
                break

        cap.release()

        cv2.destroyAllWindows()

cam= MobileCamera()

cam.getVideo("https://192.168.43.235:8080/video")

input()