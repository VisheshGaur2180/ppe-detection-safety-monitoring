import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, "src"))
sys.path.append(os.path.join(BASE_DIR, "website"))

import argparse

def run_images():
    print("[INFO] Running image testing...")
    from src.test_images import main as test_images
    test_images()

def run_video():
    print("[INFO] Running video processing...")
    from src.test_video import main as test_video
    test_video()

def run_full_pipeline():
    print("[INFO] Running full pipeline...")
    from src.main import main
    main()

def run_website():
    print("[INFO] Starting Flask server...")
    from website.app import app
    app.run(debug=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PPE Project Runner")

    parser.add_argument(
        "--mode",
        type=str,
        required=True,
        choices=["images", "video", "full", "web"],
        help="Mode to run the project"
    )

    args = parser.parse_args()

    if args.mode == "images":
        run_images()

    elif args.mode == "video":
        run_video()

    elif args.mode == "full":
        run_full_pipeline()

    elif args.mode == "web":
        run_website()