import librosa
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def sec_to_tc(seconds, fps=30):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    f = int((seconds % 1) * fps)
    return f"{h:02}:{m:02}:{s:02}:{f:02}"

def process_audio(audio_path, save_dir):
    if not os.path.exists(audio_path):
        messagebox.showerror("Lỗi", f"Không tìm thấy file: {audio_path}")
        return

    edl_output = os.path.join(save_dir, "markers.edl")

    log_text.set("📥 Đang load file...")
    root.update()

    y, sr = librosa.load(audio_path)

    log_text.set("🎵 Đang phân tích beat...")
    root.update()

    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beats, sr=sr)

    log_text.set(f"✅ Tìm thấy {len(beat_times)} beat\n📝 Đang tạo file EDL...")
    root.update()

    with open(edl_output, "w") as f:
        f.write("TITLE: BeatMarkers\nFCM: NON-DROP FRAME\n")
        for i, t in enumerate(beat_times):
            tc = sec_to_tc(t)
            f.write(f"{i+1:03}  AX       V     C        {tc} {tc} {tc} {tc}\n")
            f.write(f"* FROM BEAT {i+1}\n")

    log_text.set(f"✅ Đã tạo xong file: {edl_output}")
    messagebox.showinfo("Hoàn tất", f"Đã lưu file:\n{edl_output}")

def choose_audio():
    path = filedialog.askopenfilename(
        filetypes=[("Audio Files", "*.mp3 *.wav *.ogg *.flac"), ("All files", "*.*")]
    )
    if path:
        audio_path_var.set(path)

def choose_output_folder():
    folder = filedialog.askdirectory()
    if folder:
        output_dir_var.set(folder)

def run_processing():
    audio_path = audio_path_var.get()
    save_dir = output_dir_var.get()
    if not audio_path or not save_dir:
        messagebox.showwarning("Thiếu thông tin", "Vui lòng chọn cả file âm thanh và thư mục lưu.")
        return
    process_audio(audio_path, save_dir)

# GUI setup
root = tk.Tk()
root.title("🎧 Auto Beat Marker to EDL")
root.geometry("500x300")
root.resizable(False, False)

audio_path_var = tk.StringVar()
output_dir_var = tk.StringVar()
log_text = tk.StringVar()

# Audio file selection
tk.Label(root, text="🎵 Chọn file âm thanh:").pack(anchor="w", padx=10, pady=5)
tk.Entry(root, textvariable=audio_path_var, width=60).pack(padx=10)
tk.Button(root, text="Chọn file...", command=choose_audio).pack(pady=5)

# Output folder selection
tk.Label(root, text="📁 Thư mục lưu file .EDL:").pack(anchor="w", padx=10, pady=5)
tk.Entry(root, textvariable=output_dir_var, width=60).pack(padx=10)
tk.Button(root, text="Chọn thư mục...", command=choose_output_folder).pack(pady=5)

# Process button
tk.Button(root, text="🚀 Bắt đầu xử lý", command=run_processing, bg="green", fg="white").pack(pady=10)

# Log display
ttk.Label(root, textvariable=log_text, foreground="blue", wraplength=460).pack(pady=5)

root.mainloop()
