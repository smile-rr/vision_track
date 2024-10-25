# main.py
from video_processing import start_video_capture
from motion_detection import detect_motion, detect_pose_landmarks

def main():
    # 启动视频捕获并传入处理函数
    start_video_capture(detect_motion, detect_pose_landmarks)

if __name__ == "__main__":
    main()