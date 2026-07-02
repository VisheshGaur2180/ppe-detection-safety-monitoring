import cv2
import os
import sys

# Fix imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from detection.model_loader import load_model
from violation.violation_logic import check_violation
from visualization.draw_boxes import draw_boxes
from config import MODEL_PATH, IMAGE_FOLDER, OUTPUT_FOLDER

def main():
    # Create output folder
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Load model
    model = load_model(MODEL_PATH)

    print("Model loaded successfully!")
    print("Model classes:", model.names)

    # Check if folder exists
    if not os.path.exists(IMAGE_FOLDER):
        print("❌ ERROR: Image folder not found:", IMAGE_FOLDER)
        return

    images = os.listdir(IMAGE_FOLDER)

    if len(images) == 0:
        print("❌ No images found in folder!")
        return

    for img_name in images:
        img_path = os.path.join(IMAGE_FOLDER, img_name)

        frame = cv2.imread(img_path)
        if frame is None:
            print(f"Skipping invalid image: {img_name}")
            continue

        results = model(frame)[0]

        detections = []

        for box in results.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            detections.append({
                "label": label,
                "conf": conf,
                "bbox": (x1, y1, x2, y2)
            })

        # Check violations
        violations = check_violation(detections)

        if violations:
            print(f"{img_name}: {violations}")

        # Draw boxes
        output_frame = draw_boxes(frame, detections, violations)

        # Save output
        output_path = os.path.join(OUTPUT_FOLDER, img_name)
        cv2.imwrite(output_path, output_frame)

        # Show result
        cv2.imshow("Result", output_frame)
        cv2.waitKey(0)

    cv2.destroyAllWindows()
    print("✅ Done!")

if __name__ == "__main__":
    main()