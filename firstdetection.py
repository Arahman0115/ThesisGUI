import cv2
import argparse
import supervision as sv
from ultralytics import YOLO
import numpy as np

ZONE_POLYGON = np.array([
    [0,0],
    [1280 // 2,0],
    [1250 // 2, 720],
    [0,720]
])

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='YOLOV8 live')
    parser.add_argument(
        "--webcam-resolution",
        default=[1280, 720],
        nargs=2,
        type=int
    )
    return parser.parse_args()

def initialize_camera(frame_width, frame_height):
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
    return cap

def main():
    args = parse_arguments()
    frame_width, frame_height = args.webcam_resolution

    cap = initialize_camera(frame_width, frame_height)
    model = YOLO("yolov8l.pt")

    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=2,
        text_scale=1
    )

    zone = sv.PolygonZone(polygon=ZONE_POLYGON, frame_resolution_wh=tuple(args.webcam_resolution))
    zone_annotator = sv.PolygonZoneAnnotator(
        zone=zone,
        color=sv.Color.red(),
        thickness=2,
        text_thickness=4,
        text_scale=2,

      )



    while True:
        ret, frame = cap.read()
        result = model(frame, agnostic_nms=True)[0]
        detections = sv.Detections.from_ultralytics(result)
        detections = detections[detections.class_id != 0]


        confidences = detections.confidence
        class_ids = detections.class_id

        labels = [
            f"{model.model.names[class_id]} {confidence:.2f}"
            for confidence, class_id in zip(confidences,class_ids)
        ]


        annotated_frame = box_annotator.annotate(
            scene=frame,
            detections=detections,
            labels=labels
        )

        zone.trigger(detections=detections)
        frame = zone_annotator.annotate(scene=frame)

        cv2.imshow('yolov8', annotated_frame)

        if cv2.waitKey(30) == 27:  # Exit on 'ESC' key
            break

if __name__ == '__main__':
    main()
