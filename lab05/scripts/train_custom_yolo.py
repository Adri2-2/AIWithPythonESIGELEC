"""OPTIONAL project template: fine-tune YOLO on your OWN annotated dataset.
Needs a real dataset with sufficient images. CPU training can take a long time.
Example: python lab05/scripts/train_custom_yolo.py --data path/to/data.yaml --epochs 10
Do not treat the tiny illustrative toy dataset as a meaningful training benchmark.
"""
import argparse
from pathlib import Path
from ultralytics import YOLO


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--data',required=True,help='Path to YOUR exported data.yaml')
    parser.add_argument('--epochs',type=int,default=10)
    parser.add_argument('--imgsz',type=int,default=416)
    parser.add_argument('--model',default='yolo11n.pt')
    args=parser.parse_args()
    if not Path(args.data).is_file():
        parser.error('Could not find data.yaml: '+args.data)
    model=YOLO(args.model)
    model.train(data=args.data,epochs=args.epochs,imgsz=args.imgsz,device='cpu',batch=4)

if __name__=='__main__':
    main()
