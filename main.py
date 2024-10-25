from video_processing import start_video_capture
from motion_detection import detect_motion

def main():
    print("启动摄像头捕获并进行动作识别...")
    start_video_capture(detect_motion)

if __name__ == "__main__":
    main()
