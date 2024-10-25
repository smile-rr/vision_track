# video_processing.py
import cv2

def start_video_capture(detect_motion_callback, detect_pose_landmarks_callback):
    cap = cv2.VideoCapture(0)  # 使用内置摄像头

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 调用回调函数处理帧
        detect_pose_landmarks_callback(frame)
        detect_motion_callback(frame)

        # 显示视频流
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按下 'q' 键退出
            break

    cap.release()
    cv2.destroyAllWindows()