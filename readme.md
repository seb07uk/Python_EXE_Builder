<p align="center">
 <img width="962" height="772" alt="image" src="https://github.com/user-attachments/assets/6e0b7b00-c965-4ee7-b151-a1e4455bfc80" />

</p>

<h1 align="center">Python Builder v3.0</h1>
<p align="center"><strong>Python → EXE Compiler GUI · polsoft.ITS™ Group</strong></p>

<p align="center">
  <img src="https://img.shields.io/badge/version-3.0-00f0ff?style=flat-square" />
  <img src="https://img.shields.io/badge/platform-Windows-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/python-3.10%2B-yellow?style=flat-square" />
  <img src="https://img.shields.io/badge/license-proprietary-a855f7?style=flat-square" />
</p>

---

## 📸 Screenshot

![Python Builder v3.0 – Main Window](screenshot.png)

---

## 📋 Overview

**Python Builder v3.0** is a professional graphical tool for compiling Python scripts (`.py`) and packages into standalone Windows executables (`.exe`). Built on top of **PyInstaller**, it wraps the entire compilation workflow in an intuitive dark-themed GUI — no command line required.

> **Product:** Python Builder v3.0 – EXE  
> **Author:** Sebastian Januchowski  
> **Company:** polsoft.ITS™ Group  
> **Contact:** polsoft.its@fastservice.com  
> **GitHub:** https://github.com/seb07uk  
> **Copyright:** 2025© polsoft.ITS™. All rights reserved.

---

## ✨ Features

| Feature | Description |
|---|---|
| **Single-file EXE** | `--onefile` mode — compiles everything into one portable `.exe` |
| **Portable mode** | Creates a portable folder with launcher `.bat` — no installation needed |
| **Custom icon** | Embed your own `.ico` icon into the compiled binary |
| **EXE Metadata** | Set App Name, Company, Version, Description, Copyright |
| **Password protection** | Password-locked compilation (SHA-256 hashed) |
| **UAC elevation** | Optionally request Administrator privileges on launch |
| **Console toggle** | Show or hide the terminal window at runtime |
| **Real-time build log** | Color-coded log streamed live during compilation |
| **EN / PL UI** | Interface available in English and Polish |
| **Auto-install PyInstaller** | Detects missing PyInstaller and offers to install it |

---

## 🖥️ System Requirements

- **OS:** Windows 10 / 11 (64-bit recommended)
- **Python:** 3.10 or newer
- **Dependencies (auto-detected):**
  - `pyinstaller` ≥ 6.x
  - `Pillow` (for icon handling)
  - `tkinter` (bundled with Python)

---

## 🚀 Quick Start

### Run from source
```bash
pip install pyinstaller pillow
python python_builder.py
```

### Compile to EXE (self-hosting)
```bash
pyinstaller --onefile --windowed --icon=py-2-exe.ico python_builder.py
```

---

## 🗂️ Interface Guide

### Toolbar
| Button | Action |
|---|---|
| 📄 File | Pick a single `.py` source file |
| 📁 Folder | Pick a Python package directory |
| 🖼 Icon | Choose a `.ico` icon file |
| 📂 Output | Set the output directory |
| 🏷 Metadata | Edit EXE version/company metadata |
| 🔒 Password | Enable/disable compilation password |

### Options panel
- **--onefile** — pack everything into a single executable
- **--console** — keep the terminal window visible (useful for CLI tools)
- **UAC Administrator** — request elevated privileges on startup

### Build actions
- **📦 PORTABLE** — builds a portable directory + `.bat` launcher
- **⚡ BUILD EXE** — compiles to a single-file `.exe` via PyInstaller
- **📂 OPEN OUTPUT** — opens the output folder in Explorer

---

## 🔒 Password Protection

When enabled, a SHA-256 hash of the password is embedded as a constant in the compiled binary. The password is required every time a new build is triggered — protecting your compilation workflow from unauthorized use.

---

## 🌐 Internationalization

The interface supports **English** and **Polish** (`EN` / `PL` toggle button in the top-right corner). All labels, dialogs, and log messages are fully translated.

---

## 📁 Project Structure

```
python_builder.py      ← Main application (single-file)
py-2-exe.ico           ← Application icon
README.md              ← This file
```

---

## 📜 License

© 2025 polsoft.ITS™ Group — Sebastian Januchowski  
All rights reserved. Unauthorized redistribution is prohibited.  
Contact: polsoft.its@fastservice.com
