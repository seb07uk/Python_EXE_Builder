╔══════════════════════════════════════════════════════════════════╗
║         Python Builder v3.0 – Python → EXE Compiler GUI        ║
║                                                                  ║
║  Project Manager : Sebastian Januchowski                        ║
║  Company         : polsoft.ITS™ Group                           ║
║  Email           : polsoft.its@fastservice.com                  ║
║  GitHub          : https://github.com/seb07uk                   ║
║  Copyright       : 2025© polsoft.ITS™. All rights reserved.    ║
╚══════════════════════════════════════════════════════════════════╝

== HOW TO RUN ==
  python python_builder.py

== HOW TO COMPILE TO EXE ==
  Option 1 (recommended):
    build_exe.bat

  Option 2 (manual):
    pyinstaller --noconfirm python_builder.spec

== IMPORTANT – FIX: EXE compiling EXE ==
  When Python Builder is compiled to EXE with PyInstaller (--windowed),
  sys.executable points to python_builder.exe itself, NOT to python.exe.
  This version includes _get_python_exe() which automatically detects
  the real Python interpreter via PATH, Windows Registry, and common
  install directories.  If none is found, a file dialog opens so you
  can locate python.exe manually.

== REQUIREMENTS ==
  pip install pyinstaller pillow

