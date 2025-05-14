# 🎧 Auto Beat Marker to EDL

**Auto Beat Marker** is a tool that helps you analyze the beat from an audio file and automatically generate an `.EDL` (Edit Decision List) file – commonly used in video editing software such as Adobe Premiere, DaVinci Resolve, etc.

## Required Library

```
librosa
tkinter
```

## How does it work?

- Chọn file nhạc (`.mp3`)
- Chọn thư mục lưu file `.edl`
- Phân tích nhịp tự động bằng Librosa
- Xuất file `.EDL` chứa danh sách các thời điểm beat

## 🚀 Setup
1. Clone project
```bash
git clone https://github.com/your-username/auto-beat-marker.git
cd auto-beat-marker
```
2. Install the necessary libraries
```bash
pip install -r requirements.txt
```
3. Run
Run file Python
```bash
python maker_auto.py
```
Or: Double click `run.bat`

