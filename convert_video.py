import cv2
import glob
import shutil
from pathlib import Path

def convert(search_dir="demo_recordings_full"):
    webms = glob.glob(f"{search_dir}/*.webm")
    if not webms:
        webms = glob.glob("demo_recordings/*.webm")
    if not webms:
        print("No webm recordings found.")
        return
    
    # Take newest recording
    webms.sort(key=lambda x: Path(x).stat().st_mtime)
    src = webms[-1]
    
    dst_mp4 = "Adaptive_Learning_AI_Demo_Full_5Min.mp4"
    dst_webm = "Adaptive_Learning_AI_Demo_Full_5Min.webm"
    
    # Save webm
    shutil.copy(src, dst_webm)
    shutil.copy(src, "Adaptive_Learning_AI_Demo.webm")
    print(f"Copied high-res demo to {dst_webm}")
    
    print(f"Converting {src} to MP4 format...")
    cap = cv2.VideoCapture(src)
    fps = cap.get(cv2.CAP_PROP_FPS) or 25
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(dst_mp4, fourcc, fps, (w, h))
    
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        count += 1
        if count % 500 == 0:
            print(f"Processed {count} frames ({count/fps:.1f} seconds)...")
        
    cap.release()
    out.release()
    
    # Also overwrite main mp4
    shutil.copy(dst_mp4, "Adaptive_Learning_AI_Demo.mp4")
    
    total_sec = count / fps
    print(f"Successfully converted {count} frames to {dst_mp4}!")
    print(f"Total video duration: {int(total_sec // 60)} min {int(total_sec % 60)} sec ({total_sec:.1f}s) @ {fps}fps, {w}x{h}!")

if __name__ == "__main__":
    convert()
