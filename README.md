# 🔱 Whisper 字幕助手 GUI（支持中文/英文/乌克兰语）

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

## 1. 安装依赖

### 💻 安装Python

确保你已安装 Python 3.10 或以上版本：推荐使用 [Python 官网](https://www.python.org/downloads/) 或 [Anaconda](https://www.anaconda.com/)

### ✅ 一键安装全部依赖（推荐）

Python安装完成后，点击win+R，打开cmd，输入下方代码，将自动完成所需全部依赖的安装

```bash
pip install openai-whisper torch srt deep-translator
```

安装完成后不要点击.py运行！继续往下看

---

## 2. 安装ffmpeg（必须）

Whisper 依赖 `ffmpeg` 来加载音频文件，如果你未安装或配置错误，将导致程序无法运行

---

### ✅ 第一步：下载 Windows 版 ffmpeg

1. 打开官网下载地址：  
   https://www.gyan.dev/ffmpeg/builds/
2. 滚动到 "Release builds"
3. 建议下载名字如下的版本：  
   `ffmpeg-release-essentials.zip`（约88Mb）

---

### ✅ 第二步：解压 ffmpeg 并整理目录结构

1. **右键压缩包 → 解压到新文件夹（不能直接双击浏览）**
2. 解压后文件夹应如下所示：  
C:\ffmpeg  
└── bin  
└── ffmpeg.exe  
└── ffplay.exe  
└── ffprobe.exe  

✅ 必须确保你打开 `C:\ffmpeg` 目录后，直接能看到 `bin` 文件夹，而不是 `ffmpeg-x.x/bin` 这类嵌套结构！

---

### ✅ 第三步：添加 ffmpeg 到系统环境变量

1. 复制路径：
   `C:\ffmpeg\bin`
2. 按 Win + R，搜索：**SystemPropertiesAdvanced** → 打开
3. 点击【环境变量】按钮
4. 在“系统变量”下找到 `Path`，点击【编辑】
5. 点击【新建】，粘贴刚才的路径
6. 依次点击【确定】保存

---

### ✅ 第四步：验证是否安装成功

1. 重新打开 CMD
2. 输入：
```bash
ffmpeg -version
```
✅ 如果能看到版本号说明配置成功，例如：ffmpeg version 6.0 ...

---

### ❌ 常见错误排查

| 错误行为                        | 正确做法                         |
|-------------------------------|----------------------------------|
| ❌ 添加的是 `C:\ffmpeg`       | ✅ 应该是 `C:\ffmpeg\bin`       |
| ❌ 文件夹是 `ffmpeg/ffmpeg/bin` | ✅ 应该是 `ffmpeg/bin`（不要有嵌套）|
| ❌ 没有真正解压 zip            | ✅ 必须右键解压                  |
| ❌ 配置完没重启命令行          | ✅ 添加完环境变量后重启 CMD 才生效 |

---

## 3. 启用显卡以加速处理进程

默认转文本将使用CPU进行，该进程可能会十分缓慢，如果你的电脑使用英伟达系列显卡，则可以通过显卡处理以加速转文字过程

### 📄 [点击查看 GPU 安装网页（适用于 NVIDIA 显卡用户）](https://csfs64.github.io/CSFS_subtitle-tool/)

点击上方连接并按照提示操作即可

---

## 4. 下载转文字工具

### ⬇️ 在GitHub首页点击Code，点击Zip格式下载，解压至任意你希望的文件夹


---

## 5. 运行转文字工具（不要双击.py打开！！）

### 🖱️ 在你解压完成后的文件夹中，按住Shift，同时鼠标右键并选择在此运行PowerShell，随后在PowerShell中输入

```bash
python gui_whisper.py
```

初次进入可能需要等待一段时间，然后你将看到操作界面展开
