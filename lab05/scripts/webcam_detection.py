"""Lab 5: live LSF letter recognition from the webcam. Press Q (or ESC) to exit.

Shows ONE letter (the most probable one) and a box around the hand:
- the letter comes from the classification model (--model, trained on whole frames);
- the box comes from the detection model (--det-model, trained on the CVAT boxes).
If the detection model is missing or finds no hand, the letter is shown alone in the corner.

Run from the repository root using the course virtual environment.
Example: python lab05/scripts/webcam_detection.py --source 0
Fallback: python lab05/scripts/webcam_detection.py --source lab05/data/sample_video.mp4
"""
from __future__ import annotations
import argparse
from pathlib import Path
import cv2
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parents[2]
GREEN = (0, 200, 0)


def draw_label(img, text: str, x: int, y: int, scale: float = 1.4) -> None:
    """Draw white text on a green background, with (x, y) as the bottom-left corner of the background."""
    (w, h), base = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, scale, 3)
    y = max(y, h + base + 8)
    cv2.rectangle(img, (x, y - h - base - 8), (x + w + 12, y), GREEN, -1)
    cv2.putText(img, text, (x + 6, y - base - 4), cv2.FONT_HERSHEY_SIMPLEX, scale, (255, 255, 255), 3, cv2.LINE_AA)


def main() -> int:
    parser = argparse.ArgumentParser(description='Live LSF letter recognition (one letter + hand box)')
    parser.add_argument('--source', default='0', help='Camera index (0) or local video file')
    parser.add_argument('--model', default=str(ROOT / 'runs/classify/train-9/weights/best.pt'),
                        help='Classification weights: gives the letter')
    parser.add_argument('--det-model', default=str(ROOT / 'runs/detect/train/weights/best.pt'),
                        help="Detection weights: gives the hand box ('' to disable)")
    parser.add_argument('--conf', type=float, default=0.25, help='Minimum confidence of the hand box')
    parser.add_argument('--imgsz', type=int, default=320, help='Classification input size (trained at 320)')
    parser.add_argument('--det-imgsz', type=int, default=640, help='Detection input size (trained at 640)')
    args = parser.parse_args()
    if not 0 <= args.conf <= 1:
        parser.error('--conf must be between 0 and 1')
    source = int(args.source) if args.source.isdigit() else args.source
    if isinstance(source, str) and not Path(source).exists():
        parser.error(f'Video not found: {source}')

    cls_model = YOLO(args.model)
    det_model = None
    if args.det_model and Path(args.det_model).exists():
        det_model = YOLO(args.det_model)
    else:
        print('No detection model found: the letter will be shown without a hand box.')

    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        print('Could not open camera/video. Try --source 1 or a sample video path.')
        return 1
    try:
        print('Press q or ESC in the video window to stop.')
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            probs = cls_model.predict(frame, imgsz=args.imgsz, device='cpu', verbose=False)[0].probs
            confidence = probs.top1conf.item()

            if confidence < 0.20:
                label = "Non detected"
            else:
                label = f'{cls_model.names[probs.top1]}  {confidence:.0%}'

            box = None
            if det_model is not None:
                boxes = det_model.predict(frame, conf=args.conf, imgsz=args.det_imgsz, device='cpu', verbose=False)[0].boxes
                if len(boxes):
                    box = boxes.xyxy[boxes.conf.argmax()].int().tolist()  # keep only the most confident hand

            annotated = frame.copy()
            if box:
                x1, y1, x2, y2 = box
                cv2.rectangle(annotated, (x1, y1), (x2, y2), GREEN, 3)
                draw_label(annotated, label, x1, y1)
            else:
                draw_label(annotated, label, 10, 10)

            try:
                cv2.imshow('Lab 5 | LSF letter (q to quit)', annotated)
                if cv2.waitKey(1) & 0xFF in (ord('q'), 27):
                    break
            except cv2.error as ex:
                print('OpenCV cannot open a video window in this environment:', ex)
                print('Run from the local desktop, not a headless terminal.')
                return 2
    finally:
        cap.release()
        cv2.destroyAllWindows()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
