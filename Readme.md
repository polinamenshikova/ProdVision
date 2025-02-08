# Object Tracking Without Dataset Training

## Overview

This project provides an efficient method for object tracking and counting in a production line without the need for dataset training. By leveraging computer vision techniques, this approach saves time and computational resources while maintaining accuracy.

## Features

- Utilizes **OpenCV** for image processing
- Tracks objects using bounding boxes
- Eliminates the need for dataset training
- Efficient for real-time applications

## Technologies Used

- **Python** for scripting and automation
- **OpenCV** for image analysis and object tracking
- **NumPy** for numerical operations

## How It Works

The script processes a video feed to detect and track objects as they move through a defined area. Each detected object is assigned a unique ID and counted upon passing a threshold line. The method relies on frame-based detection and tracking, allowing it to function without a pre-trained dataset.

## Video Demonstration

Watch the demo: [YouTube Link](https://youtu.be/FIpdoaEOKW4)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/object-tracking.git
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the script:
   ```sh
   python contur_zero_.py
   ```

## License

This project is open-source under the MIT License.

MIT
