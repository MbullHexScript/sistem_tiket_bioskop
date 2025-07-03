import tkinter as tk
from tkinter import ttk, messagebox
from collections import deque
import datetime

class PemesananTiketGUI:
    def __init__(self):
        self.antrian = deque()
        self.setup_main_window()
        self.setup_styles()
        self.create_widgets()

    def setup_main_window(self):
        self.root = tk.Tk()
        self.root.title("Sistem Pemesanan Tiket Bioskop - Mbull CinemaX")
        self.root.geometry("1200x800")
        self.root.configure(bg='#1a1a2e')
        self.root.resizable(True, True)

        # posisi screen windows
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (1200 // 2)
        y = (self.root.winfo_screenheight() // 2) - (800 // 2)
        self.root.geometry(f"1200x800+{x}+{y}")

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')

        # warna custom
        colors = {
            'primary': '#16213e',
            'secondary': '#0f3460',
            'accent': '#e94560',
            'text': '#ffffff',
            'bg': '#1a1a2e',
            'card': '#16213e'
        }

        # Configure styles
        style.configure('Title.TLabel',
                       background=colors['bg'],
                       foreground=colors['text'],
                       font=('Helvetica', 24, 'bold'))

        style.configure('Subtitle.TLabel',
                       background=colors['bg'],
                       foreground=colors['text'],
                       font=('Helvetica', 14))

        style.configure('Card.TFrame',
                       background=colors['card'],
                       relief='flat',
                       borderwidth=1)

        style.configure('Custom.TButton',
                       background=colors['accent'],
                       foreground='white',
                       font=('Helvetica', 11, 'bold'),
                       focuscolor='none',
                       borderwidth=0,
                       relief='flat')

        style.map('Custom.TButton',
                 background=[('active', '#d63447'),
                           ('pressed', '#c62d42')])

        style.configure('Secondary.TButton',
                       background=colors['secondary'],
                       foreground='white',
                       font=('Helvetica', 10),
                       focuscolor='none',
                       borderwidth=0,
                       relief='flat')

        style.map('Secondary.TButton',
                 background=[('active', '#1e4976'),
                           ('pressed', '#0d2544')])

    def create_widgets(self):
        # Main container
        main_frame = tk.Frame(self.root, bg='#1a1a2e')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Header
        self.create_header(main_frame)

        # Content area
        content_frame = tk.Frame(main_frame, bg='#1a1a2e')
        content_frame.pack(fill='both', expand=True, pady=(20, 0))

        # Left panel - Booking form
        self.create_booking_panel(content_frame)

        # Right panel - Queue display
        self.create_queue_panel(content_frame)

        # Bottom panel - Controls
        self.create_control_panel(main_frame)

    def create_header(self, parent):
        header_frame = tk.Frame(parent, bg='#1a1a2e', height=100)
        header_frame.pack(fill='x', pady=(0, 20))
        header_frame.pack_propagate(False)

        # Title
        title_label = ttk.Label(header_frame, text="🎬 SISTEM PEMESANAN BIOSKOP",
                               style='Title.TLabel')
        title_label.pack(side='top', pady=(10, 5))

        # Subtitle
        subtitle_label = ttk.Label(header_frame, text="Nonton film di MbullCinemaX",
                                  style='Subtitle.TLabel')
        subtitle_label.pack(side='top')

        # Separator
        separator = ttk.Separator(header_frame, orient='horizontal')
        separator.pack(fill='x', pady=(15, 0))

    def create_booking_panel(self, parent):
        # Left panel container
        left_panel = ttk.Frame(parent, style='Card.TFrame', padding=20)
        left_panel.pack(side='left', fill='both', expand=True, padx=(0, 10))

        # Panel title
        panel_title = tk.Label(left_panel, text="📝 PEMESANAN BARU",
                              bg='#16213e', fg='#ffffff',
                              font=('Helvetica', 16, 'bold'))
        panel_title.pack(anchor='w', pady=(0, 20))

        # Form fields
        self.create_form_fields(left_panel)

    def create_form_fields(self, parent):
        # Customer name
        name_frame = tk.Frame(parent, bg='#16213e')
        name_frame.pack(fill='x', pady=(0, 15))

        name_label = tk.Label(name_frame, text="Nama Pelanggan:",
                             bg='#16213e', fg='#ffffff',
                             font=('Helvetica', 12, 'bold'))
        name_label.pack(anchor='w', pady=(0, 5))

        self.nama_entry = tk.Entry(name_frame, font=('Helvetica', 11),
                                  bg='#ffffff', fg='#333333',
                                  relief='flat', bd=5)
        self.nama_entry.pack(fill='x', ipady=8)

        # Movie selection
        movie_frame = tk.Frame(parent, bg='#16213e')
        movie_frame.pack(fill='x', pady=(0, 15))

        movie_label = tk.Label(movie_frame, text="Pilih Film:",
                              bg='#16213e', fg='#ffffff',
                              font=('Helvetica', 12, 'bold'))
        movie_label.pack(anchor='w', pady=(0, 5))

        self.movie_var = tk.StringVar()
        movie_combo = ttk.Combobox(movie_frame, textvariable=self.movie_var,
                                  font=('Helvetica', 11),
                                  values=['Avatar: The Way of Water', 'Top Gun: Maverick',
                                         'Black Panther: Wakanda Forever', 'Spider-Man: No Way Home',
                                         'The Batman', 'Doctor Strange 2', 'Jurassic World: Dominion'],
                                  state='readonly')
        movie_combo.pack(fill='x', ipady=8)
        movie_combo.set('Pilih film...')

        # Ticket quantity
        qty_frame = tk.Frame(parent, bg='#16213e')
        qty_frame.pack(fill='x', pady=(0, 15))

        qty_label = tk.Label(qty_frame, text="Jumlah Tiket:",
                            bg='#16213e', fg='#ffffff',
                            font=('Helvetica', 12, 'bold'))
        qty_label.pack(anchor='w', pady=(0, 5))

        qty_control_frame = tk.Frame(qty_frame, bg='#16213e')
        qty_control_frame.pack(fill='x')

        self.qty_var = tk.IntVar(value=1)
        qty_spinbox = tk.Spinbox(qty_control_frame, from_=1, to=10,
                                textvariable=self.qty_var,
                                font=('Helvetica', 11),
                                bg='#ffffff', fg='#333333',
                                relief='flat', bd=5, width=10)
        qty_spinbox.pack(side='left', ipady=8)

        # Price display
        self.price_label = tk.Label(qty_control_frame, text="Harga: Rp 0",
                                   bg='#16213e', fg='#e94560',
                                   font=('Helvetica', 12, 'bold'))
        self.price_label.pack(side='right', padx=(10, 0))

        # Update price when quantity changes
        self.qty_var.trace('w', self.update_price)

        # Add booking button
        add_btn = ttk.Button(parent, text="🎫 TAMBAH KE ANTRIAN",
                            command=self.tambah_pemesanan,
                            style='Custom.TButton')
        add_btn.pack(fill='x', pady=(30, 0), ipady=10)

    def create_queue_panel(self, parent):
        # Right panel container
        right_panel = ttk.Frame(parent, style='Card.TFrame', padding=20)
        right_panel.pack(side='right', fill='both', expand=True, padx=(10, 0))

        # Panel title with queue count
        title_frame = tk.Frame(right_panel, bg='#16213e')
        title_frame.pack(fill='x', pady=(0, 20))

        queue_title = tk.Label(title_frame, text="📋 ANTRIAN PEMESANAN",
                              bg='#16213e', fg='#ffffff',
                              font=('Helvetica', 16, 'bold'))
        queue_title.pack(side='left')

        self.queue_count_label = tk.Label(title_frame, text="(0 item)",
                                         bg='#16213e', fg='#e94560',
                                         font=('Helvetica', 12, 'bold'))
        self.queue_count_label.pack(side='right')

        # Queue listbox with scrollbar
        list_frame = tk.Frame(right_panel, bg='#16213e')
        list_frame.pack(fill='both', expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(list_frame, bg='#16213e')
        scrollbar.pack(side='right', fill='y')

        # Listbox
        self.queue_listbox = tk.Listbox(list_frame,
                                       yscrollcommand=scrollbar.set,
                                       bg='#0f3460', fg='#ffffff',
                                       font=('Consolas', 10),
                                       selectbackground='#e94560',
                                       relief='flat', bd=0,
                                       highlightthickness=0)
        self.queue_listbox.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.queue_listbox.yview)

    def create_control_panel(self, parent):
        # Bottom control panel
        control_frame = ttk.Frame(parent, style='Card.TFrame', padding=20)
        control_frame.pack(fill='x', pady=(20, 0))

        # Control buttons
        btn_frame = tk.Frame(control_frame, bg='#16213e')
        btn_frame.pack(fill='x')

        process_btn = ttk.Button(btn_frame, text="🎬 PROSES PEMESANAN",
                               command=self.proses_pemesanan,
                               style='Custom.TButton')
        process_btn.pack(side='left', padx=(0, 10), ipady=8, ipadx=20)

        clear_btn = ttk.Button(btn_frame, text="🗑️ HAPUS ANTRIAN",
                              command=self.clear_queue,
                              style='Secondary.TButton')
        clear_btn.pack(side='left', padx=(0, 10), ipady=8, ipadx=20)

        # Status label
        self.status_label = tk.Label(btn_frame, text="Siap menerima pemesanan",
                                    bg='#16213e', fg='#ffffff',
                                    font=('Helvetica', 11))
        self.status_label.pack(side='right', padx=(10, 0))

    def update_price(self, *args):
        """Update price display based on quantity"""
        price_per_ticket = 50000  # Rp 50,000 per ticket
        total_price = self.qty_var.get() * price_per_ticket
        self.price_label.config(text=f"Harga: Rp {total_price:,}")

    def tambah_pemesanan(self):
        nama = self.nama_entry.get().strip()
        movie = self.movie_var.get()
        jumlah = self.qty_var.get()

        if not nama:
            messagebox.showerror("Error", "Mohon masukkan nama pelanggan!")
            return

        if movie == "Pilih film..." or not movie:
            messagebox.showerror("Error", "Mohon pilih film!")
            return

        # Add to queue
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        data = {
            'nama': nama,
            'movie': movie,
            'jumlah': jumlah,
            'timestamp': timestamp,
            'total_price': jumlah * 50000
        }

        self.antrian.append(data)
        self.update_queue_display()

        # Clear form
        self.nama_entry.delete(0, tk.END)
        self.movie_var.set("Pilih film...")
        self.qty_var.set(1)

        # Update status
        self.status_label.config(text=f"✅ Pemesanan atas nama {nama} berhasil ditambahkan!")
        self.root.after(3000, lambda: self.status_label.config(text="Siap menerima pemesanan"))

    def proses_pemesanan(self):
        if not self.antrian:
            messagebox.showinfo("Info", "Tidak ada pemesanan dalam antrian untuk diproses!")
            return

        # Process first booking
        data = self.antrian.popleft()

        # Show processing dialog
        result = messagebox.askyesno("Proses Pemesanan",
                                   f"Proses pemesanan untuk:\n\n"
                                   f"Pelanggan: {data['nama']}\n"
                                   f"Film: {data['movie']}\n"
                                   f"Tiket: {data['jumlah']}\n"
                                   f"Total: Rp {data['total_price']:,}\n"
                                   f"Waktu: {data['timestamp']}\n\n"
                                   f"Konfirmasi pemrosesan?")

        if result:
            self.update_queue_display()
            self.status_label.config(text=f"✅ Pemesanan atas nama {data['nama']} telah diproses")
            messagebox.showinfo("Berhasil", f"Pemesanan atas nama {data['nama']} telah berhasil diproses!")
        else:
            # Put back in queue if cancelled
            self.antrian.appendleft(data)

    def clear_queue(self):
        if not self.antrian:
            messagebox.showinfo("Info", "Antrian sudah kosong!")
            return

        result = messagebox.askyesno("Hapus Antrian",
                                   f"Apakah Anda yakin ingin menghapus semua {len(self.antrian)} pemesanan dari antrian?")
        if result:
            self.antrian.clear()
            self.update_queue_display()
            self.status_label.config(text="🗑️ Antrian telah dikosongkan")

    def update_queue_display(self):
        # Clear listbox
        self.queue_listbox.delete(0, tk.END)

        # Update queue count
        count = len(self.antrian)
        if count == 0:
            self.queue_count_label.config(text="(0 item)")
        elif count == 1:
            self.queue_count_label.config(text="(1 item)")
        else:
            self.queue_count_label.config(text=f"({count} item)")

        # Add items to listbox
        for idx, data in enumerate(self.antrian, 1):
            display_text = (f"{idx:2d}. {data['nama']:<20} | {data['movie']:<25} | "
                          f"{data['jumlah']} tiket | Rp {data['total_price']:,} | {data['timestamp']}")
            self.queue_listbox.insert(tk.END, display_text)

        # Color alternate rows
        for i in range(0, self.queue_listbox.size(), 2):
            self.queue_listbox.itemconfig(i, {'bg': '#1a2947'})

    def run(self):
        self.root.mainloop()

# Run the application
if __name__ == "__main__":
    app = PemesananTiketGUI()
    app.run()
