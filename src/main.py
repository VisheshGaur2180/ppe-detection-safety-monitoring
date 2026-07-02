import cv2
import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from detection.model_loader import load_model
from detection.detect import run_detection
from violation.violation_logic import check_violation
from summarization.frame_summary import generate_summary
from visualization.draw_boxes import draw_boxes
from config import MODEL_PATH, VIDEO_PATH, OUTPUT_PATH

def main():
    model = load_model(MODEL_PATH)

    cap = cv2.VideoCapture(VIDEO_PATH)

    width = int(cap.get(3))
    height = int(cap.get(4))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    out = cv2.VideoWriter(
        OUTPUT_PATH,
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps,
        (width, height)
    )

    frame_no = 0

    for frame, detections in run_detection(model, VIDEO_PATH):
        frame_no += 1

        violations = check_violation(detections)

        if violations:
            summary = generate_summary(frame_no, violations)
            print(summary)

        frame = draw_boxes(frame, detections, violations)

        out.write(frame)

        cv2.imshow("Output", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()