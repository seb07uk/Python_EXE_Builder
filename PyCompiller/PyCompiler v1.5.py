import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import subprocess
import threading
import os
import json
import sys

# ---------------------------------------------------------
#  ŚCIEŻKI polsoft.ITS™ London
# ---------------------------------------------------------
BASE_DIR = os.path.join(os.path.expanduser("~"), ".polsoft", "PyCompiler")
os.makedirs(BASE_DIR, exist_ok=True)

SETTINGS_FILE = os.path.join(BASE_DIR, "settings.json")
AUTO_VERSION_FILE = os.path.join(BASE_DIR, "auto_version.txt")

# ---------------------------------------------------------
#  USTAWIENIA
# ---------------------------------------------------------
settings = {
    "exe_name": "polsoft_app",
    "version": "1.0.0"
}

def load_settings():
    global settings
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                settings = json.load(f)
        except:
            pass

def save_settings():
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)

load_settings()

# ---------------------------------------------------------
#  GLOBALNE ZMIENNE
# ---------------------------------------------------------
py_file = ""
version_file = ""
icon_file = ""

# ---------------------------------------------------------
#  ANIMOWANE LOGO (GIF, BEZ PIL)
# ---------------------------------------------------------
class AnimatedGIF(tk.Label):
    def __init__(self, master, gif_path, delay=80):
        super().__init__(master, bg="#0d0d0d")
        self.delay = delay
        self.frames = []
        self.idx = 0

        try:
            img = tk.PhotoImage(file=gif_path, format="gif -index 0")
            self.frames.append(img)

            i = 1
            while True:
                try:
                    frame = tk.PhotoImage(file=gif_path, format=f"gif -index {i}")
                    self.frames.append(frame)
                    i += 1
                except tk.TclError:
                    break

            if len(self.frames) > 1:
                self.animate()
            else:
                self.config(image=self.frames[0])

        except Exception:
            self.frames = []

    def animate(self):
        if not self.frames:
            return
        frame = self.frames[self.idx]
        self.config(image=frame)
        self.idx = (self.idx + 1) % len(self.frames)
        self.after(self.delay, self.animate)
        
# ---------------------------------------------------------
#  GENEROWANIE version.txt
# ---------------------------------------------------------
def generate_version_file(exe_name, version):
    ver_tuple = version.replace(".", ",")
    return f"""# UTF-8
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=({ver_tuple},0),
    prodvers=({ver_tuple},0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo(
      [
        StringTable(
          '040904B0',
          [
            StringStruct('CompanyName', 'polsoft.ITS™ London'),
            StringStruct('FileDescription', 'polsoft.ITS™ Python Application'),
            StringStruct('FileVersion', '{version}'),
            StringStruct('InternalName', '{exe_name}'),
            StringStruct('OriginalFilename', '{exe_name}.exe'),
            StringStruct('ProductName', 'polsoft.ITS™ Tool'),
            StringStruct('ProductVersion', '{version}'),
            StringStruct('LegalCopyright', '©2026 Sebastian Januchowski')
          ]
        )
      ]
    ),
    VarFileInfo([VarStruct('Translation', [1033, 1200])])
  ]
)
"""

# ---------------------------------------------------------
#  FUNKCJE AKTUALIZACJI DIOD
# ---------------------------------------------------------
def update_py_led():
    if py_file:
        led_py.config(fg="#00ff00")  # Zielona
    else:
        led_py.config(fg="#ff0000")  # Czerwona

def update_ver_led():
    if version_file:
        led_ver.config(fg="#00ff00")  # Zielona
    else:
        led_ver.config(fg="#ffaa00")  # Żółta

def update_icon_led():
    if icon_file:
        led_ico.config(fg="#00ff00")  # Zielona
    else:
        led_ico.config(fg="#ffaa00")  # Żółta

# ---------------------------------------------------------
#  WYBÓR PLIKÓW
# ---------------------------------------------------------
def choose_py():
    global py_file
    file = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    if file:
        py_file = file
        update_py_led()

def choose_version():
    global version_file
    file = filedialog.askopenfilename(filetypes=[("TXT", "*.txt")])
    if file:
        version_file = file
        update_ver_led()

def choose_icon():
    global icon_file
    file = filedialog.askopenfilename(filetypes=[("Ikony", "*.ico")])
    if file:
        icon_file = file
        update_icon_led()

# ---------------------------------------------------------
#  FUNKCJE OTWIERANIA FOLDERÓW
# ---------------------------------------------------------
def open_project_folder():
    if not py_file:
        messagebox.showwarning("Brak danych", "Najpierw wybierz plik .py.")
        return

    project_folder = os.path.dirname(py_file)
    try:
        if sys.platform == "win32":
            os.startfile(project_folder)
        elif sys.platform == "darwin":
            subprocess.run(["open", project_folder])
        else:
            subprocess.run(["xdg-open", project_folder])
    except Exception as e:
        messagebox.showerror("Błąd", str(e))

def open_dist():
    if not py_file:
        messagebox.showwarning("Brak danych", "Najpierw wybierz plik .py i skompiluj projekt.")
        return

    dist_path = os.path.join(os.path.dirname(py_file), "dist")

    if not os.path.exists(dist_path):
        messagebox.showwarning("Brak folderu", "Folder 'dist' jeszcze nie istnieje.")
        return

    try:
        if sys.platform == "win32":
            os.startfile(dist_path)
        elif sys.platform == "darwin":
            subprocess.run(["open", dist_path])
        else:
            subprocess.run(["xdg-open", dist_path])
    except Exception as e:
        messagebox.showerror("Błąd", str(e))

# ---------------------------------------------------------
#  OKNO iNfO
# ---------------------------------------------------------
def show_info():
    info_win = tk.Toplevel(root)
    info_win.title("Informacje")
    info_win.geometry("420x300")
    info_win.resizable(False, False)
    info_win.configure(bg="#0d0d0d")

    header = tk.Label(
        info_win,
        text="polsoft.ITS™ London",
        font=("Segoe UI", 14, "bold"),
        fg="#00aaff",
        bg="#00111f",
        pady=10
    )
    header.pack(fill="x")

    frame_border = tk.Frame(info_win, bg="#00aaff", padx=2, pady=2)
    frame_border.pack(padx=20, pady=20, fill="both", expand=True)

    frame_inner = tk.Frame(frame_border, bg="#0d0d0d")
    frame_inner.pack(fill="both", expand=True)

    text = (
        "PyCompiler v1.5\n\n"
        "Sebastian Januchowski\n"
        "polsoft.its@fastservice.com\n"
        "https://github.com/seb07uk\n"
        "© 2026 polsoft.ITS™ London"
    )

    lbl = tk.Label(
        frame_inner,
        text=text,
        font=("Segoe UI", 11, "bold"),
        fg="#66e0ff",
        bg="#0d0d0d",
        justify="center"
    )
    lbl.pack(expand=True, fill="both", pady=10)

    bottom_line = tk.Frame(info_win, bg="#00aaff", height=3)
    bottom_line.pack(fill="x", side="bottom")

# ---------------------------------------------------------
#  CZYSZCZENIE LOGU
# ---------------------------------------------------------
def clear_log():
    txt_log.delete(1.0, tk.END)

# ---------------------------------------------------------
#  KOMPILACJA W WĄTKU
# ---------------------------------------------------------
def run_pyinstaller():
    progress_bar.start(10)
    btn_build.config(state="disabled")

    # Używamy 'pyinstaller' z PATH
    cmd = ["pyinstaller", "--onefile"]
    
    # Obsługa checkboxa konsoli
    if not console_var.get():
        cmd.append("--noconsole")
    
    cmd.extend([
        f"--name={settings['exe_name']}",
        f"--version-file={version_file}",
    ])

    if icon_file:
        cmd.append(f"--icon={icon_file}")

    cmd.append(py_file)

    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            cwd=os.path.dirname(py_file)
        )

        for line in process.stdout:
            txt_log.insert(tk.END, line)
            txt_log.see(tk.END)

        process.wait()

        progress_bar.stop()
        btn_build.config(state="normal")

        if process.returncode == 0:
            messagebox.showinfo("polsoft.ITS™ London", "Kompilacja zakończona! Sprawdź folder 'dist'.")
        else:
            messagebox.showerror("Błąd", "PyInstaller zwrócił błąd. Sprawdź log powyżej.")

    except FileNotFoundError:
        progress_bar.stop()
        btn_build.config(state="normal")
        messagebox.showerror(
            "Błąd", 
            "PyInstaller nie został znaleziony!\n\n"
            "Zainstaluj go komendą:\npip install pyinstaller"
        )
    except Exception as e:
        progress_bar.stop()
        btn_build.config(state="normal")
        messagebox.showerror("Błąd", str(e))

# ---------------------------------------------------------
#  START KOMPILACJI
# ---------------------------------------------------------
def build_exe():
    global version_file, settings

    exe_name = entry_exe.get().strip()
    
    # Pobieranie wersji z 4 pól
    ver1 = entry_ver1.get().strip()
    ver2 = entry_ver2.get().strip()
    ver3 = entry_ver3.get().strip()
    ver4 = entry_ver4.get().strip()
    
    version = f"{ver1}.{ver2}.{ver3}.{ver4}"

    if not exe_name:
        messagebox.showwarning("Błąd", "Podaj nazwę EXE.")
        return

    # Walidacja formatu wersji
    if not all([ver1, ver2, ver3, ver4]):
        messagebox.showwarning("Błąd", "Podaj wszystkie 4 cyfry wersji.")
        return
    
    if not all(part.isdigit() for part in [ver1, ver2, ver3, ver4]):
        messagebox.showwarning("Błąd", "Wersja musi zawierać tylko cyfry.")
        return

    settings["exe_name"] = exe_name
    settings["version"] = version
    save_settings()

    if not version_file:
        version_file = AUTO_VERSION_FILE
        with open(AUTO_VERSION_FILE, "w", encoding="utf-8") as f:
            f.write(generate_version_file(exe_name, version))

    if not py_file:
        messagebox.showwarning("Brak danych", "Musisz wybrać plik .py.")
        return

    threading.Thread(target=run_pyinstaller, daemon=True).start()

# ---------------------------------------------------------
#  GUI – polsoft.ITS™ London STYLE
# ---------------------------------------------------------
root = tk.Tk()
root.title("polsoft.ITS™ London – PY → EXE Builder")
root.geometry("700x480")
root.resizable(False, False)
root.configure(bg="#0d0d0d")

style = ttk.Style()
style.theme_use("default")
style.configure(
    "Polsoft.Horizontal.TProgressbar",
    troughcolor="#00111f",
    background="#00aaff",
    bordercolor="#00111f",
    lightcolor="#00aaff",
    darkcolor="#0077aa"
)

header = tk.Label(
    root,
    text="polsoft.ITS™ London\nPY → EXE Builder",
    font=("Segoe UI", 20, "bold"),
    fg="#00aaff",
    bg="#0d0d0d"
)
header.pack(pady=10)

# Logo - tylko jeśli plik istnieje
logo_path = "polsoft_logo.gif"
if os.path.exists(logo_path):
    logo = AnimatedGIF(root, logo_path)
    if logo.frames:
        logo.pack(pady=5)

# Pola EXE + wersja z przyciskami czyszczenia
frm_exe = tk.Frame(root, bg="#0d0d0d")
frm_exe.pack(pady=3)

tk.Label(frm_exe, text="Nazwa EXE:", fg="#00aaff", bg="#0d0d0d").pack(side="left", padx=5)

entry_exe = tk.Entry(frm_exe, width=30, bg="#001f33", fg="#00aaff", insertbackground="#00aaff")
entry_exe.pack(side="left")
entry_exe.insert(0, settings["exe_name"])

btn_clear_exe = tk.Button(
    frm_exe, text="🗑", width=2, command=lambda: entry_exe.delete(0, tk.END),
    bg="#001f33", fg="#ff6666", activebackground="#330000",
    activeforeground="#ff9999", relief="flat", font=("Segoe UI", 9, "bold")
)
btn_clear_exe.pack(side="left", padx=3)

frm_ver = tk.Frame(root, bg="#0d0d0d")
frm_ver.pack(pady=3)

tk.Label(frm_ver, text="Wersja:", fg="#00aaff", bg="#0d0d0d").pack(side="left", padx=22)

# 4 osobne pola do wersji
entry_ver1 = tk.Entry(frm_ver, width=3, bg="#001f33", fg="#00aaff", insertbackground="#00aaff", justify="center")
entry_ver1.pack(side="left", padx=2)
entry_ver1.insert(0, settings["version"].split(".")[0] if "." in settings["version"] else "1")

tk.Label(frm_ver, text=".", fg="#00aaff", bg="#0d0d0d", font=("Segoe UI", 12, "bold")).pack(side="left")

entry_ver2 = tk.Entry(frm_ver, width=3, bg="#001f33", fg="#00aaff", insertbackground="#00aaff", justify="center")
entry_ver2.pack(side="left", padx=2)
entry_ver2.insert(0, settings["version"].split(".")[1] if len(settings["version"].split(".")) > 1 else "0")

tk.Label(frm_ver, text=".", fg="#00aaff", bg="#0d0d0d", font=("Segoe UI", 12, "bold")).pack(side="left")

entry_ver3 = tk.Entry(frm_ver, width=3, bg="#001f33", fg="#00aaff", insertbackground="#00aaff", justify="center")
entry_ver3.pack(side="left", padx=2)
entry_ver3.insert(0, settings["version"].split(".")[2] if len(settings["version"].split(".")) > 2 else "0")

tk.Label(frm_ver, text=".", fg="#00aaff", bg="#0d0d0d", font=("Segoe UI", 12, "bold")).pack(side="left")

entry_ver4 = tk.Entry(frm_ver, width=3, bg="#001f33", fg="#00aaff", insertbackground="#00aaff", justify="center")
entry_ver4.pack(side="left", padx=2)
entry_ver4.insert(0, settings["version"].split(".")[3] if len(settings["version"].split(".")) > 3 else "0")

# Auto-skip do następnego pola po wpisaniu jednej cyfry
def auto_skip(event, next_entry):
    current_widget = event.widget
    if len(current_widget.get()) >= 1:
        # Usuń starą zawartość i zostaw tylko ostatnio wpisaną cyfrę
        text = current_widget.get()
        current_widget.delete(0, tk.END)
        current_widget.insert(0, text[-1])  # Wstaw tylko ostatni znak
        next_entry.focus()
        next_entry.icursor(tk.END)

entry_ver1.bind('<KeyRelease>', lambda e: auto_skip(e, entry_ver2))
entry_ver2.bind('<KeyRelease>', lambda e: auto_skip(e, entry_ver3))
entry_ver3.bind('<KeyRelease>', lambda e: auto_skip(e, entry_ver4))
entry_ver4.bind('<KeyRelease>', lambda e: auto_skip(e, entry_ver1))

def clear_version():
    entry_ver1.delete(0, tk.END)
    entry_ver2.delete(0, tk.END)
    entry_ver3.delete(0, tk.END)
    entry_ver4.delete(0, tk.END)
    entry_ver1.focus()

btn_clear_ver = tk.Button(
    frm_ver, text="🗑", width=2, command=clear_version,
    bg="#001f33", fg="#ff6666", activebackground="#330000",
    activeforeground="#ff9999", relief="flat", font=("Segoe UI", 9, "bold")
)
btn_clear_ver.pack(side="left", padx=3)

# ---------------------------------------------------------
#  STATUS DIODY - PLIK.PY / VERSION / IKONA
# ---------------------------------------------------------
frm_status = tk.Frame(root, bg="#0d0d0d")
frm_status.pack(pady=8)

# PLIK .PY
tk.Label(frm_status, text="Plik.py", fg="#00aaff", bg="#0d0d0d", font=("Segoe UI", 10, "bold")).pack(side="left", padx=5)
led_py = tk.Label(frm_status, text="●", fg="#ff0000", bg="#0d0d0d", font=("Segoe UI", 12))
led_py.pack(side="left", padx=3)

# SEPARATOR
tk.Label(frm_status, text="│", fg="#004466", bg="#0d0d0d", font=("Segoe UI", 14)).pack(side="left", padx=10)

# VERSION
tk.Label(frm_status, text="Ver", fg="#00aaff", bg="#0d0d0d", font=("Segoe UI", 10, "bold")).pack(side="left", padx=5)
led_ver = tk.Label(frm_status, text="●", fg="#ffaa00", bg="#0d0d0d", font=("Segoe UI", 12))
led_ver.pack(side="left", padx=3)

# SEPARATOR
tk.Label(frm_status, text="│", fg="#004466", bg="#0d0d0d", font=("Segoe UI", 14)).pack(side="left", padx=10)

# IKONA
tk.Label(frm_status, text="Ikona", fg="#00aaff", bg="#0d0d0d", font=("Segoe UI", 10, "bold")).pack(side="left", padx=5)
led_ico = tk.Label(frm_status, text="●", fg="#ffaa00", bg="#0d0d0d", font=("Segoe UI", 12))
led_ico.pack(side="left", padx=3)

# Inicjalizacja diod
update_py_led()
update_ver_led()
update_icon_led()

# Etykiety - USUNIĘTE
# lbl_py = tk.Label(root, text="Plik .py: (nie wybrano)", fg="#cccccc", bg="#0d0d0d")
# lbl_py.pack(pady=3)
# lbl_ver = tk.Label(root, text="version.txt: (nie wybrano)", fg="#cccccc", bg="#0d0d0d")
# lbl_ver.pack(pady=3)
# lbl_ico = tk.Label(root, text="Ikona (opcjonalnie): (nie wybrano)", fg="#cccccc", bg="#0d0d0d")
# lbl_ico.pack(pady=3)

# ---------------------------------------------------------
#  CHECKBOX: TRYB KONSOLI
# ---------------------------------------------------------
console_var = tk.BooleanVar(value=False)

chk_console = tk.Checkbutton(
    root,
    text="Włącz konsolę (PyInstaller --console)",
    variable=console_var,
    bg="#0d0d0d",
    fg="#00aaff",
    activebackground="#0d0d0d",
    activeforeground="#66d9ff",
    selectcolor="#001f33",
    font=("Segoe UI", 10, "bold")
)
chk_console.pack(pady=5)

# ---------------------------------------------------------
#  PRZYCISKI – LEWA / PRAWA KOLUMNA (4+4)
# ---------------------------------------------------------
frm_buttons = tk.Frame(root, bg="#0d0d0d")
frm_buttons.pack(pady=10)

frm_left = tk.Frame(frm_buttons, bg="#0d0d0d")
frm_left.pack(side="left", padx=20)

frm_right = tk.Frame(frm_buttons, bg="#0d0d0d")
frm_right.pack(side="right", padx=20)

# LEWA KOLUMNA
btn1 = tk.Button(
    frm_left, text="1. Wybierz plik (.py)", width=30, command=choose_py,
    bg="#001f33", fg="#00aaff", activebackground="#00334d",
    activeforeground="#66d9ff", relief="flat", font=("Segoe UI", 10, "bold")
)
btn1.pack(pady=5)

btn2 = tk.Button(
    frm_left, text="2. Wstaw version.txt", width=30, command=choose_version,
    bg="#001f33", fg="#00aaff", activebackground="#00334d",
    activeforeground="#66d9ff", relief="flat", font=("Segoe UI", 10, "bold")
)
btn2.pack(pady=5)

btn3 = tk.Button(
    frm_left, text="3. Wybierz ikonę (.ico)", width=30, command=choose_icon,
    bg="#001f33", fg="#00aaff", activebackground="#00334d",
    activeforeground="#66d9ff", relief="flat", font=("Segoe UI", 10, "bold")
)
btn3.pack(pady=5)

btn_build = tk.Button(
    frm_left, text="4. Kompiluj do EXE", width=30, command=build_exe,
    bg="#001f33", fg="#00aaff", activebackground="#00334d",
    activeforeground="#66d9ff", relief="flat", font=("Segoe UI", 10, "bold")
)
btn_build.pack(pady=5)

# PRAWA KOLUMNA
btn_open_project = tk.Button(
    frm_right, text="5. Otwórz folder projektu", width=30, command=open_project_folder,
    bg="#001f33", fg="#00aaff", activebackground="#00334d",
    activeforeground="#66d9ff", relief="flat", font=("Segoe UI", 10, "bold")
)
btn_open_project.pack(pady=5)

btn_open_dist = tk.Button(
    frm_right, text="6. Otwórz folder 'dist'", width=30, command=open_dist,
    bg="#001f33", fg="#00aaff", activebackground="#00334d",
    activeforeground="#66d9ff", relief="flat", font=("Segoe UI", 10, "bold")
)
btn_open_dist.pack(pady=5)

btn_clear_log = tk.Button(
    frm_right, text="7. Wyczyść log", width=30, command=clear_log,
    bg="#001f33", fg="#00aaff", activebackground="#00334d",
    activeforeground="#66d9ff", relief="flat", font=("Segoe UI", 10, "bold")
)
btn_clear_log.pack(pady=5)

btn_info = tk.Button(
    frm_right, text="8. iNfO", width=30, command=show_info,
    bg="#001f33", fg="#00aaff", activebackground="#00334d",
    activeforeground="#66d9ff", relief="flat", font=("Segoe UI", 10, "bold")
)
btn_info.pack(pady=5)

# PRZYCISK WYJŚCIE - WYŚRODKOWANY POD KOLUMNAMI
btn_exit = tk.Button(
    root, text="9. Wyjdź", width=30, command=root.destroy,
    bg="#001f33", fg="#00aaff", activebackground="#00334d",
    activeforeground="#66d9ff", relief="flat", font=("Segoe UI", 10, "bold")
)
btn_exit.pack(pady=10)

progress_bar = ttk.Progressbar(
    root, mode="indeterminate", length=500, style="Polsoft.Horizontal.TProgressbar"
)

# PRZYCISK UKRYWANIA/POKAZYWANIA LOGU
log_visible = False  # UKRYTY NA STARCIE

def toggle_log():
    global log_visible
    if log_visible:
        txt_log.pack_forget()
        progress_bar.pack_forget()
        btn_toggle_log.config(text="▼▼▼ Pokaż Output ▼▼▼")
        log_visible = False
        root.geometry("700x480")  # Zmniejsz okno
    else:
        progress_bar.pack(pady=10)
        txt_log.pack(pady=10)
        btn_toggle_log.config(text="▲▲▲ Ukryj Output ▲▲▲")
        log_visible = True
        root.geometry("700x680")  # Przywróć oryginalny rozmiar

btn_toggle_log = tk.Button(
    root, text="▼▼▼ Pokaż Output ▼▼▼", command=toggle_log,
    bg="#001f33", fg="#00aaff", activebackground="#00334d",
    activeforeground="#66d9ff", relief="flat", font=("Segoe UI", 9, "bold"),
    width=60
)
btn_toggle_log.pack(pady=5)

txt_log = tk.Text(
    root, height=10, width=85,
    bg="#0d0d0d", fg="#66e0ff", insertbackground="#66e0ff"
)
# txt_log.pack(pady=10) - ZAKOMENTOWANE, bo ukryte na starcie

root.mainloop()