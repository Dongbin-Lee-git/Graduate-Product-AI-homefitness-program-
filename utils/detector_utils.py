import numpy as np
import sys
import tensorflow as tf
import os
import cv2
from utils import label_map_util

iou_cnt = 0
detection_graph = tf.Graph()
sys.path.append("..")
config = tf.compat.v1.ConfigProto()
# config.gpu_options.allow_growth = True
config.gpu_options.per_process_gpu_memory_fraction=0.27
# load label map
label_map = label_map_util.load_labelmap(os.path.join('hand_inference_graph', 'hand_label_map.pbtxt'))
categories = label_map_util.convert_label_map_to_categories(
    label_map, max_num_classes=1, use_display_name=True)
category_index = label_map_util.create_category_index(categories)
# Load a frozen infrerence graph into memory
def load_inference_graph():
    # load frozen tensorflow model into memory
    print("> ====== loading HAND frozen graph into memory")
    detection_graph = tf.compat.v1.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.compat.v1.GraphDef()
        with tf.io.gfile.GFile('hand_inference_graph/frozen_inference_graph.pb', 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')
        sess = tf.compat.v1.Session(graph=detection_graph, config=config)
    print(">  ====== Hand Inference graph loaded.")
    return detection_graph, sess


def intersection_over_union(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    x11, y11, x12, y12 = tf.split(boxA, 4, axis=0)
    x21, y21, x22, y22 = tf.split(boxB, 4, axis=0)

    xA = tf.maximum(x11, x21)
    yA = tf.maximum(y11, y21)
    xB = tf.minimum(x12, x22)
    yB = tf.minimum(y12, y22)

    interArea = tf.maximum((xB - xA + 1), 0) * tf.maximum((yB - yA + 1), 0)

    boxAArea = (x12 - x11 + 1) * (y12 - y11 + 1)
    boxBArea = (x22 - x21 + 1) * (y22 - y21 + 1)

    iou = interArea / (boxAArea + boxBArea - interArea)

    return iou

# draw the detected bounding boxes on the images
# You can modify this to also draw a label.
# def draw_box_on_image(num_hands_detect, score_thresh, scores, boxes, im_width, im_height, image_np, iou_k):
def draw_box_on_image(num_hands_detect, score_thresh, scores, boxes, im_width, im_height, image_np, iou_k):
    for i in range(num_hands_detect):
        if (scores[i] > score_thresh):
            (left, right, top, bottom) = (boxes[i][1] * im_width, boxes[i][3] * im_width,
                                          boxes[i][0] * im_height, boxes[i][2] * im_height)
            p1 = (int(left), int(top))
            p2 = (int(right), int(bottom))

            # #iou rectangle print
            cv2.rectangle(image_np, (2, 44), (30, 59), (77, 255, 9), 1, 1)
            cv2.rectangle(image_np, (2, 60), (30, 75), (77, 255, 9), 1, 1)
            cv2.rectangle(image_np, (2, 76), (30, 91), (77, 255, 9), 1, 1)
            cv2.rectangle(image_np, (2, 92), (30, 107), (77, 255, 9), 1, 1)
            cv2.rectangle(image_np, (2, 108), (30, 123), (77, 255, 9), 1, 1)
            cv2.rectangle(image_np, (122, 62), (152, 81), (77, 255, 9), 1, 1)
            cv2.rectangle(image_np, (153, 62), (182, 81), (77, 255, 9), 1, 1)
            #
            # # iou detection
            #
            iou_k[0] = intersection_over_union([2, 44, 30, 59], [int(left), int(top), int(right), int(bottom)])
            iou_k[1] = intersection_over_union([2, 60, 30, 75], [int(left), int(top), int(right), int(bottom)])
            iou_k[2] = intersection_over_union([2, 76, 30, 91], [int(left), int(top), int(right), int(bottom)])
            iou_k[3] = intersection_over_union([2, 92, 30, 107], [int(left), int(top), int(right), int(bottom)])
            iou_k[4] = intersection_over_union([2, 108, 30, 123], [int(left), int(top), int(right), int(bottom)])
            iou_k[5] = intersection_over_union([122, 62, 152, 81], [int(left), int(top), int(right), int(bottom)])
            iou_k[6] = intersection_over_union([153, 62, 182, 81], [int(left), int(top), int(right), int(bottom)])
            cv2.rectangle(image_np, p1, p2, (77, 255, 9), 1, 1)


# Show fps value on image.
def draw_fps_on_image(fps, image_np):
    cv2.putText(image_np, fps, (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (77, 255, 9), 2)


# Actual detection .. generate scores and bounding boxes given an image
def detect_objects(image_np, detection_graph, sess):
    # Definite input and output Tensors for detection_graph
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
    # Each box represents a part of the image where a particular object was detected.
    detection_boxes = detection_graph.get_tensor_by_name(
        'detection_boxes:0')
    # Each score represent how level of confidence for each of the objects.
    # Score is shown on the result image, together with the class label.
    detection_scores = detection_graph.get_tensor_by_name(
        'detection_scores:0')
    detection_classes = detection_graph.get_tensor_by_name(
        'detection_classes:0')
    num_detections = detection_graph.get_tensor_by_name(
        'num_detections:0')

    image_np_expanded = np.expand_dims(image_np, axis=0)

    (boxes, scores, classes, num) = sess.run(
        [detection_boxes, detection_scores,
         detection_classes, num_detections],
        feed_dict={image_tensor: image_np_expanded})
    return np.squeeze(boxes), np.squeeze(scores)