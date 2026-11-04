"""Lab 5: capture webcam photos for CVAT. SPACE = save frame, Q = quit.
Saves to lab05/captures/ by default. Do not upload identifiable people without consent.
Run: python lab05/scripts/webcam_capture.py --source 0
"""
from __future__ import annotations
import argparse
from datetime import datetime
from pathlib import Path
import cv2


def main() -> int:
    parser = argparse.ArgumentParser(description='Save webcam frames with the space bar')
    parser.add_argument('--source',default='0',help='Camera index or video file path')
    parser.add_argument('--output',default='lab05/captures',help='Folder for new images')
    args=parser.parse_args()
    output=Path(args.output)
    source=int(args.source) if args.source.isdigit() else args.source
    cap=cv2.VideoCapture(source)
    if not cap.isOpened():
        print('Could not open input. Try --source 1 or a video file.')
        return 1
    count=0
    print('SPACE to save a photo; Q or ESC to quit. Capture varied backgrounds and angles.')
    try:
        while True:
            ok,frame=cap.read()
            if not ok:
                break
            display=frame.copy()
            cv2.putText(display, 'SPACE: save | Q: quit', (15,30),
                        cv2.FONT_HERSHEY_SIMPLEX,0.65,(255,255,255),2)
            try:
                cv2.imshow('Lab 5 | Webcam capture',display)
                key=cv2.waitKey(1)&0xFF
            except cv2.error as ex:
                print('Could not open camera preview:',ex)
                return 2
            if key==ord(' ') :
                output.mkdir(parents=True,exist_ok=True)
                filename=output/f'frame_{datetime.now().strftime("%Y%m%d_%H%M%S_%f")}.jpg'
                # Save original frame WITHOUT on-screen text overlay.
                cv2.imwrite(str(filename),frame)
                count+=1
                print('Saved',filename)
            elif key in (ord('q'),27):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
    print(f'{count} image(s) saved')
    return 0


if __name__=='__main__':
    raise SystemExit(main())
