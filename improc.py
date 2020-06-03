import cv2
import numpy as np

def run_main():
    cap = cv2.VideoCapture(0)
    four_cc = cv2.VideoWriter_fourcc(*'XVID')
    saved = cv2.VideoWriter('output.avi', four_cc, 30, (640, 480))
    while(cap.isOpened()):
        cv2.waitKey(1000/33)
        ret, frame = cap.read()
        if ret is True:
            # write the flipped frame
            saved.write(frame)
            cv2.imshow('frame', frame)
        if cv2.waitKey(1000/33) & 0xFF == ord('q'):
            break
# Release everything if job is finished
    cap.release()
    saved.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    run_main()