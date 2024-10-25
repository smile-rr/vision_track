import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()


def detect_motion(frame):
    # 将帧从 BGR 转换为 RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 使用 MediaPipe 进行动作识别
    results = pose.process(frame_rgb)

    if results.pose_landmarks:
        # 绘制人体姿态
        mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
