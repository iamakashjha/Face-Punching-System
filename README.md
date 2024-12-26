# Zidio Face Punching System

## Overview
The **Zidio Face Punching System** is a cutting-edge facial recognition-based employee attendance system that ensures seamless, contactless, and secure attendance tracking. Designed to streamline workforce management, this system integrates real-time attendance logging with advanced data analytics to provide insightful productivity trends and performance metrics.

## Features

### 1. Facial Recognition Check-in/Out
- Employees can clock in and out using facial recognition for a smooth, contactless experience.

### 2. Real-time Attendance Logging
- Automatically logs employee check-in and check-out times, with live updates to a centralized database.

### 3. Attendance Reports
- Generates customizable daily, weekly, and monthly attendance reports summarizing:
  - Work hours
  - Late arrivals
  - Early departures

### 4. Face Spoof Detection
- Enhanced security algorithms to detect and prevent spoofing attempts using photos or videos.

### 5. Shift & Overtime Tracking
- Tracks shifts and calculates overtime accurately for payroll processing.

### 6. Data Analysis & Insights
- Provides analytics on:
  - Average hours worked
  - Absenteeism trends
  - Late arrivals
- Visual insights using graphs, heatmaps, and charts.

## Installation

### Prerequisites
- Python 3.10
- Required Python libraries (install via `requirements.txt`)
- OpenCV for real-time video processing
- sklearn for machine learning

### Steps to Install
1. Clone this repository:
   ```bash
   git clone https://github.com/iamakashjha/Face-Punching-System
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure the following files are present:
   - `data/haarcascade_frontalface_default.xml` for face detection
   - `background.png` for the user interface

## Usage

### 1. Collect Face Data
Run the `add_faces.py` script to collect and save face data for employees:
```bash
python face_data_collection.py
```
- Follow the prompts to add new employees.

### 2. Test the System
Run the `test.py` script to test real-time recognition and attendance logging:
```bash
python face_recognition_attendance.py
```
- Press `o` to mark attendance.
- Press `q` to quit the application.

### 3. View Attendance Reports
- run app.py file to view the report in browser.
- Attendance data is saved in the `Attendance` folder as CSV files.
- Reports are named in the format `Attendance_<date>.csv`.

## Folder Structure
```
├── data
│   ├── haarcascade_frontalface_default.xml
│   ├── names.pkl
│   ├── faces_data.pkl
├── Attendance
│   ├── Attendance_<date>.csv
├── add_faces.py
├── test.py
├── app.py
├── background.png
├── requirements.txt
└── README.md
```

## Future Enhancements
- **Mobile App Integration**: Develop a companion app for mobile devices to view reports and manage data.
- **Cloud Sync**: Integrate cloud services for centralized data storage and access.
- **Multi-language Support**: Add support for multiple languages.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Acknowledgments
- OpenCV for providing a robust library for computer vision tasks.
- sklearn for machine learning utilities.
- pyttsx3 for text-to-speech functionality.


## Contact

- For questions or support, please reach out to me:

- Email: iamakashjha@icloud.com

- GitHub: https://github.com/iamakashjha/
