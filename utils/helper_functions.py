# 这里可以放置一些常用的函数，比如处理视频帧的函数
def convert_to_grayscale(frame):
    """将图像转换为灰度图"""
    import cv2
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
