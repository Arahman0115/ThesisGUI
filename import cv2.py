import cv2
import argparse
import supervision as sv

from ultralytics import YOLO

def parse_arguments() -> argparse.Namespace:
    parser=argparse.ArgumentParser(description='YOLOV8 live')
    parser.add_argument(
        "--webcam-resolution",
          default=[1280, 720],
          nargs=2,
          type=int)
    args = parser.parse_args()
    return args

def main():
    args= parse_arguments()
    frame_width, frame_height = args.webcam_resolution

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,frame_height)


    model = YOLO("yolov8l.pt")

    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=2,
        text_scale=1
    )

    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera Test', frame)
        result = model(frame)[0]
        detections =sv.Detections.from_yolov8(result)
        frame = box_annotator.annotate(scene=frame, detections=detections)
        if (cv2.waitKey(30) == 27):
            break
if __name__ == '__main__':
    main()
def Rx_Genetic_Variant(self):
    # Create a new Toplevel window for the popup
    popup_window = tk.Toplevel(self.rx_Profile_patient)
    popup_window.title("Add Genetic Variant")
    popup_window.geometry("400x200")

    # Create entry widgets for genetic variant information
    gene_entry = Entry(popup_window, bg='white', fg='black')
    gene_entry.pack(pady=10)
    variant_entry = Entry(popup_window, bg='white', fg='black')
    variant_entry.pack(pady=10)
    disease_entry = Entry(popup_window, bg='white', fg='black')
    disease_entry.pack(pady=10)

    # Create a button to save the genetic variant information


def save_genetic_variant(self, gene, variant, disease):
    # Here, you can add code to save the genetic variant information to your database or perform other actions
    # For example, you might want to update the Treeview with the new information
    self.tree_genetic_variant.insert("", "end", values=(gene, variant, disease))
