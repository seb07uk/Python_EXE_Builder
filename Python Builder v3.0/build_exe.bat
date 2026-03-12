@echo off
:: ╔══════════════════════════════════════════════════════════════════╗
:: ║            Python Builder v3.0 – Build Script                  ║
:: ║            polsoft.ITS™ Group  │  2025©                        ║
:: ╚══════════════════════════════════════════════════════════════════╝
title Python Builder – Build EXE

echo [Python Builder] Compiling to EXE...
echo.

pyinstaller --noconfirm python_builder.spec

if errorlevel 1 (
    echo.
    echo [ERROR] Compilation failed!
    pause
    exit /b 1
)

echo.
echo [OK] python_builder.exe created in dist\
pause
