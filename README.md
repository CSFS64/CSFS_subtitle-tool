# 🎧 Whisper 字幕助手 GUI（支持中文/英文/乌克兰语）

基于 OpenAI Whisper 的图形界面字幕识别工具，支持将 MP3/WAV 音频文件识别为字幕（SRT），并支持输出为乌克兰语、英文或中文字幕

---

## ✨ 功能特点

- 支持以下音频格式：`mp3`, `wav`
- 输出语言支持：
  - ✅ 乌克兰语（推荐）
  - ✅ 英文（自动翻译）
  - ✅ 中文（自动翻译两次）
- 实时显示识别进度
- 自动检测是否启用 GPU 加速
- 输出标准 `.srt` 字幕文件

---

## 📦 安装依赖

确保你已安装 Python 3.10 或以上版本：推荐使用 [Python 官网](https://www.python.org/downloads/) 或 [Anaconda](https://www.anaconda.com/)。

### ✅ 一键安装全部依赖（推荐）

```bash
pip install openai-whisper torch srt deep-translator
