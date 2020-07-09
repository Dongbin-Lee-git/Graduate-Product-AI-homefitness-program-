from multiprocessing import Process, Queue
import cv2
import visualizations as vis
from applications.model_wrapper import ModelWrapper
import configs.draw_config as draw_config
import os
#import psutil
from detect_single_threaded import hand_track
import applications.taskbar_control as tc


def dictpop(dt : dict):
    for k in ['neck', 'Rchick', 'Rtemple', 'Lchick', 'Ltemple', 'nose', 'Reye', 'Rear', 'Leye', 'Lear']:
        dt.pop(k, None)


if __name__ == '__main__':
    #Load = Process(target=Loading_start)
   #Load.start()
    model_path = "trained_models/model11_test-15Sun1219-2101"
    model_wrapper = ModelWrapper(model_path)
    tc.hide_taskbar()
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    q = Queue(2)
    p = Process(target=hand_track, args=(q,))
    p.start()
    cv2.namedWindow("one", flags=cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("one", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.moveWindow("one", 0, 0)
    cv2.resizeWindow("one", 960, 1080)
    # os.startfile(os.path.join(os.path.dirname(__file__), 'trainer_unity/tr_unity.bat'))

    while(True):
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cam_img_bgr = frame[0:1080, 480:1440]
        q.put(cv2.resize(cam_img_bgr, dsize=(192, 216)))
        img_rgb = cv2.cvtColor(cam_img_bgr, cv2.COLOR_BGR2RGB)
        skeletons = model_wrapper.process_image(img_rgb)
        skeleton_drawer = vis.SkeletonDrawer(img_rgb, draw_config)
        key = cv2.waitKey(1)
        if key == ord('j'):
            skeleton_drawer.change_color('Llowerarm')
            skeleton_drawer.change_color('LupperArm')
            skeleton_drawer.change_color('Rlowerarm')
            skeleton_drawer.change_color('RupperArm')
        # if key == ord('k'):
        #     skeleton_drawer.change_color('Lupperleg')
        #     skeleton_drawer.change_color('Llowerleg')
        #     skeleton_drawer.change_color('Rupperleg')
        #     skeleton_drawer.change_color('Rlowerleg')

        for skeleton in skeletons:
            dictpop(skeleton.keypoints)
            dictpop(skeleton.joints)
            print("-----------------------------------")
            skeleton.draw_skeleton(skeleton_drawer.joint_draw, skeleton_drawer.kpt_draw)
        processed_img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
        cv2.imshow("one", processed_img_bgr)
        print('one = ', os.getpid())
        if key == 27:
            tc.unhide_taskbar()
            # for proc in psutil.process_iter():
            #     if proc.name() == "tr_unity.exe":
            #         proc.kill()
            #     if proc.name() == "Single-Threaded Detection":
            #         proc.kill()
            break
    # p.join()
    cap.release()
    cv2.destroyAllWindows()