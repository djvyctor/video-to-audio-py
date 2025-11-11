import os
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from .downloader import download_video

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube → MP3")
        self.geometry("600x280")
        self.resizable(False, False)
        self.configure(bg='#1e1e1e')
        self.url_var = tk.StringVar()
        self.dir_var = tk.StringVar(value=os.path.join(os.path.expanduser("~"), "Downloads"))
        self.status_var = tk.StringVar(value="")
        self.progress_var = tk.DoubleVar(value=0)
        self._setup_style()
        self._build()

    def _setup_style(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Dark.TFrame', background='#1e1e1e')
        style.configure('Dark.TLabel', background='#1e1e1e', foreground='#ffffff', font=('Segoe UI', 10))
        style.configure('Dark.TEntry', fieldbackground='#2d2d2d', foreground='#ffffff', borderwidth=0)
        style.configure('Dark.TButton', background='#0078d4', foreground='#ffffff', borderwidth=0, focuscolor='none', font=('Segoe UI', 10))
        style.map('Dark.TButton', background=[('active', '#005a9e')])
        style.configure('Dark.Horizontal.TProgressbar', background='#0078d4', troughcolor='#2d2d2d', borderwidth=0, thickness=20)

    def _build(self):
        pad = {'padx': 20, 'pady': 8}
        ttk.Label(self, text="URL do YouTube", style='Dark.TLabel').pack(anchor='w', **pad)
        ttk.Entry(self, textvariable=self.url_var, style='Dark.TEntry', width=70).pack(fill='x', **pad)
        
        ttk.Label(self, text="Pasta de saída", style='Dark.TLabel').pack(anchor='w', **pad)
        dir_frame = ttk.Frame(self, style='Dark.TFrame')
        dir_frame.pack(fill='x', **pad)
        ttk.Entry(dir_frame, textvariable=self.dir_var, style='Dark.TEntry', width=50).pack(side='left', fill='x', expand=True, padx=(0, 10))
        ttk.Button(dir_frame, text="Procurar", style='Dark.TButton', command=self._choose_dir).pack(side='right')
        
        self.progress_bar = ttk.Progressbar(self, variable=self.progress_var, maximum=100, style='Dark.Horizontal.TProgressbar')
        self.progress_bar.pack(fill='x', **pad)
        
        self.convert_btn = ttk.Button(self, text="Converter", style='Dark.TButton', command=self._start)
        self.convert_btn.pack(anchor='w', **pad)
        
        ttk.Label(self, textvariable=self.status_var, style='Dark.TLabel', foreground='#00ff00').pack(anchor='w', **pad)

    def _choose_dir(self):
        d = filedialog.askdirectory(initialdir=self.dir_var.get() or os.getcwd())
        if d:
            self.dir_var.set(d)

    def _update_progress(self, percent):
        self.progress_var.set(percent)

    def _start(self):
        url = self.url_var.get().strip()
        outdir = self.dir_var.get().strip()
        if not url or not outdir:
            messagebox.showerror("Erro", "Informe a URL e a pasta de saída.")
            return
        self.status_var.set("Baixando...")
        self.progress_var.set(0)
        self.convert_btn.config(state="disabled")
        threading.Thread(target=self._worker, args=(url, outdir), daemon=True).start()

    def _worker(self, url, outdir):
        try:
            path = download_video(url, outdir, progress_callback=lambda p: self.after(0, self._update_progress, p))
            self.after(0, self._done_ok, path)
        except Exception as err:
            self.after(0, self._done_err, str(err))

    def _done_ok(self, path):
        self.progress_var.set(100)
        self.status_var.set(f"Concluído: {os.path.basename(path)}")
        self.convert_btn.config(state="normal")
        messagebox.showinfo("Concluído", f"Arquivo salvo em:\n{path}")

    def _done_err(self, msg):
        self.progress_var.set(0)
        self.status_var.set("")
        self.convert_btn.config(state="normal")
        messagebox.showerror("Erro", msg)