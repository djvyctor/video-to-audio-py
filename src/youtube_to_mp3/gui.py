import os
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from .downloader import download_video

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube → MP3")
        self.geometry("540x200")
        self.resizable(False, False)
        self.url_var = tk.StringVar()
        self.dir_var = tk.StringVar(value=os.path.join(os.path.expanduser("~"), "Downloads"))
        self.status_var = tk.StringVar(value="")
        self._build()

    def _build(self):
        pad = {'padx': 10, 'pady': 6}
        ttk.Label(self, text="URL do YouTube").grid(row=0, column=0, sticky="w", **pad)
        ttk.Entry(self, textvariable=self.url_var, width=62).grid(row=1, column=0, columnspan=2, sticky="we", **pad)
        ttk.Label(self, text="Pasta de saída").grid(row=2, column=0, sticky="w", **pad)
        ttk.Entry(self, textvariable=self.dir_var, width=50).grid(row=3, column=0, sticky="we", **pad)
        ttk.Button(self, text="Procurar", command=self._choose_dir).grid(row=3, column=1, sticky="e", **pad)
        self.convert_btn = ttk.Button(self, text="Converter", command=self._start)
        self.convert_btn.grid(row=4, column=0, sticky="w", **pad)
        ttk.Label(self, textvariable=self.status_var, foreground="#555").grid(row=5, column=0, columnspan=2, sticky="w", **pad)

    def _choose_dir(self):
        d = filedialog.askdirectory(initialdir=self.dir_var.get() or os.getcwd())
        if d:
            self.dir_var.set(d)

    def _start(self):
        url = self.url_var.get().strip()
        outdir = self.dir_var.get().strip()
        if not url or not outdir:
            messagebox.showerror("Erro", "Informe a URL e a pasta de saída.")
            return
        self.status_var.set("Baixando e convertendo...")
        self.convert_btn.config(state="disabled")
        threading.Thread(target=self._worker, args=(url, outdir), daemon=True).start()

    def _worker(self, url, outdir):
        try:
            path = download_video(url, outdir)
            self.after(0, lambda: self._done_ok(path))
        except Exception as e:
            self.after(0, lambda: self._done_err(str(e)))

    def _done_ok(self, path):
        self.status_var.set(f"Concluído: {os.path.basename(path)}")
        self.convert_btn.config(state="normal")
        messagebox.showinfo("Concluído", f"Arquivo salvo em:\n{path}")

    def _done_err(self, msg):
        self.status_var.set("")
        self.convert_btn.config(state="normal")
        messagebox.showerror("Erro", msg)