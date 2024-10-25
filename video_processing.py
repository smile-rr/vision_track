import cv2

def start_video_capture(process_frame_callback):
    # 打开摄像头
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("无法打开摄像头")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("无法读取摄像头帧")
                break

            # 处理当前帧
            process_frame_callback(frame)

            # 显示视频
            cv2.imshow('Real-time Video', frame)

            # 按 'q' 键退出
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
