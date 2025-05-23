import os
os.environ["WHISPER_CACHE"] = os.path.join(os.path.dirname(__file__), "whisper")
import tkinter as tk
from tkinter import filedialog, messagebox
import whisper
import torch
import srt
import datetime
import webbrowser
import threading
from deep_translator import GoogleTranslator

def format_timestamp(seconds: float) -> str:
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hrs:02}:{mins:02}:{secs:02},{millis:03}"

def transcribe_file():
    path = file_path.get()
    model_name = model_var.get()
    output_lang = output_lang_var.get()
    use_gpu = torch.cuda.is_available()

    if not path:
        messagebox.showerror("错误", "请先选择一个音频文件")
        return

    log_text.set(f"📦 正在加载模型（使用 {'GPU' if use_gpu else 'CPU'}）...")
    root.update()
    model = whisper.load_model(model_name, device="cuda" if use_gpu else "cpu")
    log_text.set("✅ 模型加载成功，正在加载音频文件...")
    root.update()

    try:
        audio = whisper.load_audio(path)
    except Exception as e:
        messagebox.showerror("错误", f"音频读取失败：{e}")
        return

    log_text.set("✅ 音频加载成功，正在转为梅尔频谱...")
    root.update()
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    lang_suffix = {
        "乌克兰语（推荐）": "ukr",
        "英文（机器翻译）": "en",
        "中文字幕（翻译两次）": "zh"
    }[output_lang]

    lang_code = "uk" if output_lang != "中文字幕（翻译两次）" else "en"

    log_text.set("🧠 开始识别音频...")
    root.update()

    result = model.transcribe(path, language=lang_code, task="translate" if output_lang != "乌克兰语（推荐）" else "transcribe", verbose=False)

    srt_path = os.path.splitext(path)[0] + f"_translated_{lang_suffix}.srt"

    if output_lang == "中文字幕（翻译两次）":
        translator = GoogleTranslator(source="en", target="zh-CN")

    with open(srt_path, "w", encoding="utf-8") as f:
        for i, seg in enumerate(result['segments'], start=1):
            text = seg['text']
            start = format_timestamp(seg['start'])
            end = format_timestamp(seg['end'])

            if output_lang == "中文字幕（翻译两次）":
                text = translator.translate(text)

            f.write(f"{i}\n{start} --> {end}\n{text}\n\n")
            log_text.set(f"⏳ 第 {i} 段识别完成：{text[:30]}...")
            root.update()

    log_text.set(f"✅ 字幕生成成功：{srt_path}")
    messagebox.showinfo("完成", f"字幕文件已保存：\n{srt_path}")

def choose_file():
    path = filedialog.askopenfilename(filetypes=[("音频文件", "*.mp3 *.wav")])
    if path:
        file_path.set(path)

def open_gpu_guide():
    import sys
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    guide_path = resource_path("gpu_setup_guide.html")
    if not os.path.exists(guide_path):
        messagebox.showerror("错误", "找不到 gpu_setup_guide.html，请确保它与程序在同一目录。")
        return
    webbrowser.open(f"file://{guide_path}")

# ========== GUI 布局 ==========
root = tk.Tk()
root.title("Whisper 字幕助手（支持多语言输出）")

file_path = tk.StringVar()
model_var = tk.StringVar(value="medium")
output_lang_var = tk.StringVar(value="乌克兰语（推荐）")
log_text = tk.StringVar(value="准备就绪")

tk.Label(root, text="音频文件:").pack()
tk.Entry(root, textvariable=file_path, width=60).pack()
tk.Button(root, text="选择文件", command=choose_file).pack(pady=5)

tk.Label(root, text="Whisper 模型大小:").pack()
tk.OptionMenu(root, model_var, "tiny", "base", "small", "medium", "large").pack()

tk.Label(root, text="输出字幕语言:").pack()
tk.OptionMenu(root, output_lang_var,
              "乌克兰语（推荐）",
              "英文（机器翻译）",
              "中文字幕（翻译两次）").pack()

tk.Label(root, text="提示：翻译后的英文/中文字幕准确度较低，建议选择乌克兰语原文进行人工或 AI 翻译。",
         fg="red", wraplength=500, justify="center").pack(pady=5)

tk.Button(root, text="开始识别字幕", command=lambda: threading.Thread(target=transcribe_file).start()).pack(pady=10)
tk.Label(root, textvariable=log_text, fg="green", wraplength=500, justify="center").pack()

tk.Button(root, text="查看 GPU 安装说明", command=open_gpu_guide, bg="#e0e0e0").pack(pady=10)

root.mainloop()
