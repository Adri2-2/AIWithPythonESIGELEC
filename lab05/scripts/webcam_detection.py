"""Lab 5: live YOLO webcam/video detection. Press Q (or ESC) to exit.
Run from the repository root or lab05 directory using the course virtual environment.
Example: python lab05/scripts/webcam_detection.py --source 0 --conf 0.35
Fallback: python lab05/scripts/webcam_detection.py --source lab05/data/sample_video.mp4
"""
from __future__ import annotations
import argparse
from pathlib import Path
import cv2
from ultralytics import YOLO


def main() -> int:
    parser = argparse.ArgumentParser(description='Live object detection with YOLO11n')
    parser.add_argument('--source', default='0', help='Camera index (0) or local video file')
    parser.add_argument('--model', default='yolo11n.pt', help='Local weights path or model name')
    parser.add_argument('--conf', type=float, default=0.25)
    parser.add_argument('--imgsz', type=int, default=416)
    args = parser.parse_args()
    if not 0 <= args.conf <= 1:
        parser.error('--conf must be between 0 and 1')
    source = int(args.source) if args.source.isdigit() else args.source
    if isinstance(source, str) and not Path(source).exists():
        parser.error(f'Video not found: {source}')
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        print('Could not open camera/video. Try --source 1 or a sample video path.')
        return 1
    try:
        model = YOLO(args.model)  # First use may download pretrained weights.
        print('Press q or ESC in the video window to stop.')
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            result = model.predict(frame, conf=args.conf, imgsz=args.imgsz, device='cpu', verbose=False)[0]
            annotated = result.plot()
            try:
                cv2.imshow('Lab 5 | YOLO detection (q to quit)', annotated)
                if cv2.waitKey(1) & 0xFF in (ord('q'),27):
                    break
            except cv2.error as ex:
                print('OpenCV cannot open a video window in this environment:',ex)
                print('Run from the local desktop, not a headless terminal.')
                return 2
    finally:
        cap.release()
        cv2.destroyAllWindows()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
