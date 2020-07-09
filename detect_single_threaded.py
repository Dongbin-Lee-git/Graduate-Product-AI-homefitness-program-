from utils import detector_utils as detector_utils
import cv2
# import datetime
import numpy as np
from UI import *
iou_cnt = np.zeros(7)

def iou_active(iou, w):
    global iou_cnt
    print(iou_cnt)
    iou_cnt = np.where(iou > 0.4, iou_cnt + 1, iou_cnt)
    result = np.where(iou_cnt >= 30)
    if len(result[0]) is not 0:
        iou_cnt.fill(0)
        w.select_button(result[0][0])

def hand_track(q):
    app = QApplication(sys.argv)
    window = MainWindow()
    detection_graph, sess = detector_utils.load_inference_graph()

    cv2.namedWindow('Single-Threaded Detection', flags=cv2.WINDOW_NORMAL)
    while True:
        iou = np.zeros(7)
        image_np = q.get()
        if image_np is not None:
            try:
                image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
            except:
                print("Error converting to RGB")
            boxes, scores = detector_utils.detect_objects(image_np,
                                                          detection_graph, sess)
            detector_utils.draw_box_on_image(2, 0.2,
                                             scores, boxes, 192, 216,
                                             image_np, iou)
            iou_active(iou, window)
            print(iou)
            iou.fill(0)
            cv2.imshow('Single-Threaded Detection',
                        cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR))
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
    app.exec_()
