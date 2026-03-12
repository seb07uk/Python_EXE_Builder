<p align="center">
  <img src="logo.png" width="96" alt="Python Builder Logo" />
</p>

<h1 align="center">Python Builder v3.0</h1>
<p align="center"><strong>Kompilator Python → EXE z interfejsem graficznym · polsoft.ITS™ Group</strong></p>

<p align="center">
  <img src="https://img.shields.io/badge/wersja-3.0-00f0ff?style=flat-square" />
  <img src="https://img.shields.io/badge/platforma-Windows-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/python-3.10%2B-yellow?style=flat-square" />
  <img src="https://img.shields.io/badge/licencja-własnościowa-a855f7?style=flat-square" />
</p>

---

## 📸 Zrzut ekranu

![Python Builder v3.0 – Okno główne](screenshot.png)

---

## 📋 Opis

**Python Builder v3.0** to profesjonalne narzędzie graficzne do kompilacji skryptów Pythona (`.py`) i pakietów do samodzielnych plików wykonywalnych Windows (`.exe`). Opiera się na silniku **PyInstaller** i udostępnia cały proces kompilacji przez intuicyjny interfejs z ciemnym motywem — bez konieczności korzystania z wiersza poleceń.

> **Produkt:** Python Builder v3.0 – EXE  
> **Autor:** Sebastian Januchowski  
> **Firma:** polsoft.ITS™ Group  
> **Kontakt:** polsoft.its@fastservice.com  
> **GitHub:** https://github.com/seb07uk  
> **Prawa autorskie:** 2025© polsoft.ITS™. Wszelkie prawa zastrzeżone.

---

## ✨ Funkcje

| Funkcja | Opis |
|---|---|
| **Pojedynczy plik EXE** | Tryb `--onefile` — kompiluje wszystko do jednego pliku `.exe` |
| **Tryb portable** | Tworzy katalog portable z launcherem `.bat` — bez instalacji |
| **Własna ikona** | Osadzenie własnej ikony `.ico` w skompilowanym pliku |
| **Metadane EXE** | Ustawienie nazwy aplikacji, firmy, wersji, opisu, praw autorskich |
| **Ochrona hasłem** | Kompilacja zabezpieczona hasłem (hash SHA-256) |
| **Uprawnienia UAC** | Opcjonalne żądanie uprawnień Administratora |
| **Przełącznik konsoli** | Pokaż lub ukryj okno terminala w czasie działania |
| **Log kompilacji** | Kolorowy log streamowany na żywo podczas kompilacji |
| **EN / PL interfejs** | Interfejs dostępny w języku angielskim i polskim |
| **Auto-instalacja PyInstaller** | Wykrywa brakujący PyInstaller i oferuje jego instalację |

---

## 🖥️ Wymagania systemowe

- **System:** Windows 10 / 11 (zalecany 64-bit)
- **Python:** 3.10 lub nowszy
- **Zależności (automatycznie wykrywane):**
  - `pyinstaller` ≥ 6.x
  - `Pillow` (obsługa ikon)
  - `tkinter` (dołączony do Pythona)

---

## 🚀 Szybki start

### Uruchomienie ze źródeł
```bash
pip install pyinstaller pillow
python python_builder.py
```

### Kompilacja do EXE (self-hosting)
```bash
pyinstaller --onefile --windowed --icon=py-2-exe.ico python_builder.py
```

---

## 🗂️ Przewodnik po interfejsie

### Pasek narzędzi
| Przycisk | Akcja |
|---|---|
| 📄 File | Wybierz pojedynczy plik źródłowy `.py` |
| 📁 Folder | Wybierz katalog pakietu Python |
| 🖼 Icon | Wybierz plik ikony `.ico` |
| 📂 Output | Ustaw katalog wyjściowy |
| 🏷 Metadata | Edytuj metadane wersji / firmy EXE |
| 🔒 Password | Włącz/wyłącz hasło kompilacji |

### Panel opcji
- **--onefile** — pakuje wszystko do jednego pliku wykonywalnego
- **--console** — zachowuje widoczne okno terminala (przydatne dla narzędzi CLI)
- **UAC Administrator** — żąda podwyższonych uprawnień przy starcie

### Akcje kompilacji
- **📦 PORTABLE** — tworzy przenośny katalog + launcher `.bat`
- **⚡ BUILD EXE** — kompiluje do jednego pliku `.exe` przez PyInstaller
- **📂 OPEN OUTPUT** — otwiera katalog wyjściowy w Eksploratorze

---

## 🔒 Ochrona hasłem

Po włączeniu hash SHA-256 hasła jest osadzany jako stała w skompilowanym pliku binarnym. Hasło jest wymagane za każdym razem, gdy uruchamiana jest nowa kompilacja — chroni proces kompilacji przed nieautoryzowanym użyciem.

---

## 🌐 Internacjonalizacja

Interfejs obsługuje **angielski** i **polski** (przycisk przełącznika `EN` / `PL` w prawym górnym rogu). Wszystkie etykiety, okna dialogowe i komunikaty dziennika są w pełni przetłumaczone.

---

## 📁 Struktura projektu

```
python_builder.py      ← Główna aplikacja (jeden plik)
py-2-exe.ico           ← Ikona aplikacji
README.md              ← Ten plik
```

---

## 📜 Licencja

© 2025 polsoft.ITS™ Group — Sebastian Januchowski  
Wszelkie prawa zastrzeżone. Nieautoryzowana redystrybucja jest zabroniona.  
Kontakt: polsoft.its@fastservice.com
