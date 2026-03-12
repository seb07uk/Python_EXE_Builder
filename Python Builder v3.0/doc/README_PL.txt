========================================================================
  Python Builder v3.0
  Kompilator Python --> EXE z interfejsem graficznym
  polsoft.ITS(TM) Group
========================================================================

  Autor      : Sebastian Januchowski
  Firma      : polsoft.ITS(TM) Group
  E-mail     : polsoft.its@fastservice.com
  GitHub     : https://github.com/seb07uk
  Prawa aut. : 2025(c) polsoft.ITS(TM). Wszelkie prawa zastrzezone.

------------------------------------------------------------------------
OPIS
------------------------------------------------------------------------
Python Builder v3.0 to profesjonalne narzedzie graficzne do kompilacji
skryptow Pythona (.py) i pakietow do samodzielnych plikow wykonywalnych
Windows (.exe). Oparty na PyInstaller, oferuje caly proces kompilacji
w ciemnym, dwujezycznym (EN/PL) interfejsie -- bez uzycia terminala.

------------------------------------------------------------------------
WYMAGANIA SYSTEMOWE
------------------------------------------------------------------------
  - System  : Windows 10 / 11 (zalecany 64-bit)
  - Python  : 3.10 lub nowszy
  - Pakiety pip (auto-wykrywane / auto-instalowane):
      * pyinstaller >= 6.x
      * Pillow (obsluga ikon)
      * tkinter (dolaczony do Pythona)

------------------------------------------------------------------------
SZYBKI START
------------------------------------------------------------------------
  1. Zainstaluj zaleznosci:
       pip install pyinstaller pillow

  2. Uruchom aplikacje:
       python python_builder.py

  3. W interfejsie graficznym:
       a) Kliknij [File] i wybierz plik .py
       b) (Opcjonalnie) Ustaw ikone, katalog wyjsciowy, metadane, haslo
       c) Wybierz opcje: --onefile, --console, UAC Admin
       d) Kliknij [BUILD EXE] aby skompilowac

------------------------------------------------------------------------
FUNKCJE
------------------------------------------------------------------------
  [+] Pojedynczy EXE   : Tryb --onefile, jeden samodzielny plik
  [+] Tryb portable    : Katalog + launcher .bat, bez instalacji
  [+] Wlasna ikona     : Osadzenie .ico w skompilowanym pliku
  [+] Metadane EXE     : Nazwa, Firma, Wersja, Prawa autorskie
  [+] Blokada haslem   : Haslo kompilacji (hash SHA-256)
  [+] Uprawnienia UAC  : Zadanie uprawnien Administratora przy starcie
  [+] Przelacznik kons.: Pokaz/ukryj okno terminala
  [+] Log na zywo      : Kolorowy output kompilacji w czasie rzeczyw.
  [+] Interfejs EN/PL  : Pelny dwujezyczny interfejs
  [+] Auto PyInstaller : Wykrywa i instaluje PyInstaller jezeli brak

------------------------------------------------------------------------
OPCJE KOMPILACJI
------------------------------------------------------------------------
  --onefile      Pakuje wszystko do jednego EXE (domyslnie: WL)
  --console      Zachowuje widoczne okno terminala (domyslnie: WYL)
  UAC Admin      Zadanie podwyzszonych uprawnien (domyslnie: WYL)

------------------------------------------------------------------------
AKCJE KOMPILACJI
------------------------------------------------------------------------
  [PORTABLE]    Tworzy przenosny katalog + launcher .bat
  [BUILD EXE]   Kompiluje do .exe przez PyInstaller
  [OPEN OUTPUT] Otwiera katalog wyjsciowy w Eksploratorze

------------------------------------------------------------------------
STRUKTURA PLIKOW
------------------------------------------------------------------------
  python_builder.py    Glowna aplikacja (pojedynczy plik)
  py-2-exe.ico         Ikona aplikacji
  README.txt           Ten plik

------------------------------------------------------------------------
LICENCJA
------------------------------------------------------------------------
  (c) 2025 polsoft.ITS(TM) Group -- Sebastian Januchowski
  Wszelkie prawa zastrzezone.
  Nieautoryzowana redystrybucja, kopiowanie lub modyfikacja jest
  zabroniona.
  Kontakt: polsoft.its@fastservice.com

========================================================================
