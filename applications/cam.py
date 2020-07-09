import cv2
import visualizations as vis
from applications.model_wrapper import ModelWrapper
#from multiprocessing import Process, Queue
#from detect_single_threaded import hand_track
# import time
import configs.draw_config as draw_config
import psutil
import applications.taskbar_control as tc

# from utils import detector_utils as detector_utils
# import datetime
# import numpy as np
# import os


def dictpop(dt : dict):
    for k in ['neck','Rchick','Rtemple','Lchick','Ltemple','nose','Reye','Rear','Leye','Lear']:
        dt.pop(k, None)


def process_frame(self, img):
    skeletons = self.model_wrapper.process_image(img)
    skeleton_drawer = vis.SkeletonDrawer(img, draw_config)
    for skeleton in skeletons:
        dictpop(skeleton.keypoints)
        dictpop(skeleton.joints)
        print("-----------------------------------")
        skeleton.draw_skeleton(skeleton_drawer.joint_draw, skeleton_drawer.kpt_draw)
    return img


if __name__ == "__main__":
    model_path = "../trained_models/model11_test-15Sun1219-2101"
    model_wrapper = ModelWrapper(model_path)

    fps_time = 0

    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    # q = Queue(3)
    # p = Process(target=hand_track, args=(q,))
    # p.start()

    tc.hide_taskbar()

    print("Press ESC to exit")

    cv2.namedWindow("cam-test", flags=cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("cam-test", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.moveWindow("cam-test", 0, 0)
    cv2.resizeWindow("cam-test", 960, 1080)

    while True:
        s, cam_img_bgr = cam.read()
        cam_img_bgr = cv2.flip(cam_img_bgr, 1)
        # q.put(cv2.resize(cam_img_bgr, dsize=(384, 216)))

        cam_img_bgr = cam_img_bgr[0:1080, 480:1440]
        img_rgb = cv2.cvtColor(cam_img_bgr, cv2.COLOR_BGR2RGB)
        skeletons = model_wrapper.process_image(img_rgb)
        skeleton_drawer = vis.SkeletonDrawer(img_rgb, draw_config)
        for skeleton in skeletons:
            dictpop(skeleton.keypoints)
            dictpop(skeleton.joints)
            print("-----------------------------------")
            skeleton.draw_skeleton(skeleton_drawer.joint_draw, skeleton_drawer.kpt_draw)
        #
        processed_img_rgb = img_rgb
        processed_img_bgr = cv2.cvtColor(processed_img_rgb, cv2.COLOR_RGB2BGR)
        # # cv2.putText(processed_img_bgr,
        # #             "FPS: %f" % (1.0 / (time.time() - fps_time)),
        # #             (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
        # #             (0, 255, 0), 2)
        cv2.imshow("cam-test", processed_img_bgr)
        # fps_time = time.time()
        if cv2.waitKey(1) == 27:  # Esc key to stop
            tc.unhide_taskbar()
            for proc in psutil.process_iter():
                if proc.name() == "trainer_unity.exe":
                    proc.kill()
            break
    cv2.destroyAllWindows()
    p.join()