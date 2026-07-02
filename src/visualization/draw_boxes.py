import cv2

def draw_boxes(frame, detections, violations):
    for det in detections:
        x1, y1, x2, y2 = det["bbox"]
        label = det["label"]

        color = (0, 255, 0)

        if "Helmet Missing" in violations:
            color = (0, 0, 255)

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    return frame