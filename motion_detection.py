# motion_detection.py
import cv2
import numpy as np
from datetime import datetime
import mediapipe as mp


def detect_motion(frame):

    # 将图像转换为灰度
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 进行高斯模糊处理
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 假设我们有一个背景图像
    background = np.zeros_like(blurred)  # 这里可以替换为实际的背景图像

    # 计算当前帧与背景帧的差异
    frame_delta = cv2.absdiff(background, blurred)

    # 应用阈值，生成二值图像
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]

    # 找到轮廓
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 检查轮廓并假设检测到人物和动作
    detected_person = None
    detected_action = None

    for contour in contours:
        if cv2.contourArea(contour) > 500:  # 过滤小轮廓
            # 假设检测到一个人
            detected_person = "Person A"  # 模拟检测到的人物
            detected_action = "Moving"  # 模拟动作
            break  # 一旦检测到一个人物就退出循环

    # 获取当前时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 打印识别结果
    if detected_person and detected_action:
        print(f"时间: {current_time}, 人物: {detected_person}, 动作: {detected_action}")


def detect_pose_landmarks(frame):
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()

    # 将帧从 BGR 转换为 RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 使用 MediaPipe 进行动作识别
    results = pose.process(frame_rgb)

    if results.pose_landmarks:
        # 绘制人体姿态
        mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
