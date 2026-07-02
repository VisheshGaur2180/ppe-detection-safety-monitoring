import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "best.pt")

IMAGE_FOLDER = os.path.join(BASE_DIR, "data", "images")
VIDEO_FOLDER = os.path.join(BASE_DIR, "data", "videos")
VIDEO_PATH = os.path.join(VIDEO_FOLDER, "input.mp4")

OUTPUT_BASE = os.path.join(BASE_DIR, "outputs")

OUTPUT_IMAGES = os.path.join(OUTPUT_BASE, "processed_images")
OUTPUT_VIDEOS = os.path.join(OUTPUT_BASE, "processed_videos")
OUTPUT_REPORTS = os.path.join(OUTPUT_BASE, "reports")
OUTPUT_LOGS = os.path.join(OUTPUT_BASE, "logs")

OUTPUT_VIDEO_PATH = os.path.join(OUTPUT_VIDEOS, "output.mp4")
LOG_JSON = os.path.join(OUTPUT_LOGS, "violation_log.json")
REPORT_CSV = os.path.join(OUTPUT_REPORTS, "report.csv")

WEB_UPLOADS = os.path.join(BASE_DIR, "website", "static", "uploads")
WEB_RESULTS = os.path.join(BASE_DIR, "website", "static", "results")

CONF_THRESHOLD = 0.5

def create_folders():
    folders = [
        IMAGE_FOLDER,
        VIDEO_FOLDER,
        OUTPUT_IMAGES,
        OUTPUT_VIDEOS,
        OUTPUT_REPORTS,
        OUTPUT_LOGS,
        WEB_UPLOADS,
        WEB_RESULTS
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)


create_folders()
FRAME_SKIP = 5
SAVE_INTERVAL = 25