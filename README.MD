# VisionTrack

## Overview
VisionTrack is a Python-based project that focuses on real-time video processing and motion detection using OpenCV and MediaPipe. This project aims to capture video from a webcam, process the video frames, and perform motion recognition.

## Features
- Real-time video capture from the webcam
- Motion detection using MediaPipe for pose estimation
- Visualization of detected poses on the video feed
- Modular architecture for easy extension and maintenance

## Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Setup
1. Clone the repository:
   ```bash
   git clone git@github.com:smile-rr/vision_track.git
   cd vision_track
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the project, execute the following command in the terminal:
```bash
python main.py
```

Press the 'q' key to exit the video capture.

## Directory Structure
```
vision_track/
│
├── main.py                  # Main entry point for the application
├── video_processing.py       # Video processing logic
├── motion_detection.py       # Motion detection logic
├── requirements.txt          # Required libraries
└── utils/
    └── helper_functions.py   # Helper functions for various tasks
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
- [OpenCV](https://opencv.org/) for computer vision capabilities
- [MediaPipe](https://mediapipe.dev/) for efficient pose detection

## Contact
For inquiries, please reach out to [your-email@example.com].
