import cv2
from multiprocessing import Process, Queue
from detect_single_threaded import hand_track


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    q = Queue(3)
    p = Process(target=hand_track, args=(q,))
    p.start()
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        q.put(cv2.resize(frame, dsize=(384, 216)))
        cv2.imshow("one", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()