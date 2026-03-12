========================================================================
  Python Builder v3.0
  Python --> EXE Compiler GUI
  polsoft.ITS(TM) Group
========================================================================

  Author    : Sebastian Januchowski
  Company   : polsoft.ITS(TM) Group
  Email     : polsoft.its@fastservice.com
  GitHub    : https://github.com/seb07uk
  Copyright : 2025(c) polsoft.ITS(TM). All rights reserved.

------------------------------------------------------------------------
DESCRIPTION
------------------------------------------------------------------------
Python Builder v3.0 is a professional graphical tool for compiling
Python scripts (.py) and packages into standalone Windows executables
(.exe). Built on PyInstaller, it wraps the entire build workflow in a
dark-themed, bilingual (EN/PL) GUI -- no command line required.

------------------------------------------------------------------------
SYSTEM REQUIREMENTS
------------------------------------------------------------------------
  - OS      : Windows 10 / 11 (64-bit recommended)
  - Python  : 3.10 or newer
  - pip packages (auto-detected / auto-installed):
      * pyinstaller >= 6.x
      * Pillow (icon support)
      * tkinter (bundled with Python)

------------------------------------------------------------------------
QUICK START
------------------------------------------------------------------------
  1. Install dependencies:
       pip install pyinstaller pillow

  2. Run the application:
       python python_builder.py

  3. In the GUI:
       a) Click [File] and select your .py script
       b) (Optional) Set icon, output folder, metadata, password
       c) Choose options: --onefile, --console, UAC Admin
       d) Click [BUILD EXE] to compile

------------------------------------------------------------------------
FEATURES
------------------------------------------------------------------------
  [+] Single-file EXE  : --onefile mode, one self-contained binary
  [+] Portable mode    : Folder + .bat launcher, no install needed
  [+] Custom icon      : Embed .ico into the compiled binary
  [+] EXE Metadata     : App Name, Company, Version, Copyright
  [+] Password lock    : SHA-256 hashed compilation password
  [+] UAC elevation    : Request Administrator privileges on launch
  [+] Console toggle   : Show/hide terminal window at runtime
  [+] Live build log   : Color-coded real-time compilation output
  [+] EN / PL UI       : Full bilingual interface
  [+] Auto PyInstaller : Detects & installs PyInstaller if missing

------------------------------------------------------------------------
BUILD OPTIONS
------------------------------------------------------------------------
  --onefile      Pack everything into a single EXE (default: ON)
  --console      Keep terminal window visible (default: OFF)
  UAC Admin      Request elevated privileges (default: OFF)

------------------------------------------------------------------------
BUILD ACTIONS
------------------------------------------------------------------------
  [PORTABLE]    Creates portable folder + .bat launcher
  [BUILD EXE]   Compiles to single .exe via PyInstaller
  [OPEN OUTPUT] Opens the output directory in Explorer

------------------------------------------------------------------------
FILE STRUCTURE
------------------------------------------------------------------------
  python_builder.py    Main application (single-file, self-contained)
  py-2-exe.ico         Application icon
  README.txt           This file

------------------------------------------------------------------------
LICENSE
------------------------------------------------------------------------
  (c) 2025 polsoft.ITS(TM) Group -- Sebastian Januchowski
  All rights reserved.
  Unauthorized redistribution, copying or modification is prohibited.
  Contact: polsoft.its@fastservice.com

========================================================================
