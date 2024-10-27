import cv2 #Library yang digunakan untuk keperluan pengolahan citra digital
import numpy as np #library Numerical Python digunakan untuk keperluan komputasi numerik seperti array
from tkinter import Tk, Canvas, Button, PhotoImage, filedialog, messagebox, Text #Library yang digunakan untuk membuat GUI.
from pathlib import Path #library python untuk dapat mengakses file berdasarkan direktori

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\myanu\OneDrive\Documents\Kuliah\Aplikasi Tugas Akhir\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("Tugas Akhir Mohamad Yanuar Wardinnansah-2011500705")
window.geometry("1280x720")
window.configure(bg = "#F8F3E6")


canvas = Canvas(
    window,
    bg = "#F8F3E6",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1280.0,
    160.0,
    fill="#378CE7",
    outline="")

canvas.create_text(
    317.0,
    48.0,
    anchor="nw",
    text="Deteksi Kepadatan Lalu Lintas",
    fill="#000000",
    font=("RobotoRoman Regular", 48 * -1)
)

# # Label untuk menampilkan koordinat
# label = Text(window, height=1, width=20, bg="#F8F3E6", bd=0, font=("RobotoRoman Regular", 15))
# label.place(x=10, y=10)

# def show_coordinates(event):
#     x, y = event.x, event.y
#     label.delete("1.0", "end")
#     label.insert("1.0", f"Koordinat: ({x}, {y})")

# # Binding event mouse movement dengan fungsi show_coordinates
# canvas.bind("<Motion>", show_coordinates)
#-----------------------------Fungsi Klik Layar--------------------------------------
#Button Tahap 1
def klik_button1():
    canvas.delete("text","judul")  # Menghapus teks pada button lain

    canvas.create_text(
        29.0,
        180.0,
        anchor="nw",
        text="Pada tahap 1 merupakan tahap untuk memilih file yang akan dilakukan proses\npendeteksian tingkat kepadatan lalu lintas. Anda bisa mengikuti langkah berikut:",
        fill="#000000",
        font=("RobotoRoman Regular", 25),
        tags="text" 
    )
    
    canvas.create_text(
        29.0,
        280.0,
        anchor="nw",
        text="1. Silahkan pilih file video terlebih dahulu.\n2. Pastikan video yang dipilih tidak salah.\n3. Klik tombol selanjutnya untuk melanjutkan ke tahap berikutnya.",
        fill="#000000",
        font=("RobotoRoman Regular", 25),
        tags="text" 
    )
    
    canvas.create_text(
        29.0,
        400.0,
        anchor="nw",
        text="Note: Jika file video yang dipilih salah, harap pilih ulang file video.",
        fill="red",
        font=("RobotoRoman Regular", 15),
        tags="text"  
    )
    
    hide_tombol()
    
    button_10.place(
        x=240.0,
        y=514.0,
        width=247.0,
        height=54.94
    )
    
    button_11.place(
        x=517.0,
        y=515.0,
        width=247.0,
        height=54.94
    )
    button_21.place(
    x=794.0,
    y=515.0,
    width=247.0,
    height=54.941650390625
    )
    
    button_22.place(
    x=42.0,
    y=47.0,
    width=75.0,
    height=63.0
    )

#Button Tahap 2
def klik_button2():
    canvas.delete("text","judul")  # Menghapus teks button lain

    canvas.create_text(
        29.0,
        180.0,
        anchor="nw",
        text="Pada Tahap 2 bertujuan untuk merubah perspektif pada video, perubahan perspektif bertujuan agar seolah-olah\nvideo direkam dari atas. Silahkan ikuti langkah berikut:",
        fill="#000000",
        font=("RobotoRoman Regular", 18),
        tags="text"  
    )
    canvas.create_text(
        29.0,
        260.0,
        anchor="nw",
        text="1. Klik button jalankan.\n2. Pilih 4 titik untuk menentukan area mana yang ingin dirubah.\n3. Pilih titik mulai kiri atas, kanan atas, kanan bawah, dan kiri bawah.\n4. Tekan tombol s pada keyboard untuk menyimpan hasil perubahan perspektif.\n5. Tunggu hingga proses perubahan perspektif selesai.\n6. Klik tombol selanjutnya untuk melanjutkan ke tahap berikutnya",
        fill="#000000",
        font=("RobotoRoman Regular", 18),
        tags="text"  
    )

    #Menyembunyikan tampilan button
    hide_tombol()

    button_12.place(
        x=517.0,
        y=435.0,
        width=247.0,
        height=54.94
    )
    button_23.place(
    x=517.0,
    y=515.0,
    width=247.0,
    height=54.941650390625
    )
    button_22.place(
    x=42.0,
    y=47.0,
    width=75.0,
    height=63.0
    )

#Button Tahap 3
def klik_button3():
    canvas.delete("text","judul")  # Menghapus teks button lain

    canvas.create_text(
        29.0,
        180.0,
        anchor="nw",
        text="Pada Tahap 3 bertujuan untuk merubah citra menjadi grayscale(abu-abu). Tahapan ini merupakan\ntahapan pre-processing yang nantinya akan digunakan pada tahap background subtraction dan frame\ndifferencing untuk menampilkan hasil dalam bentuk threshold. Silahkan ikuti langkah berikut:",
        fill="#000000",
        font=("RobotoRoman Regular", 20),
        tags="text"  
    )
    canvas.create_text(
        29.0,
        285.0,
        anchor="nw",
        text="1. Pilih file video yang telah dirubah sudut pandangnya.\n2. Klik button Jalankan untuk melihat hasil grayscale.\n3. Klik tombol selanjutnya untuk melanjutkan ke tahap berikutnya.",
        fill="#000000",
        font=("RobotoRoman Regular", 18),
        tags="text"  
    )

    #Menyembunyikan tampilan button
    hide_tombol()

    button_13.place(
        x=517.0,
        y=515.0,
        width=247.0,
        height=54.94
    ) 
    button_20.place(
        x=240.0,
        y=514.0,
        width=247.0,
        height=54.94
    )
    button_22.place(
    x=42.0,
    y=47.0,
    width=75.0,
    height=63.0
    )
    button_24.place(
    x=794.0,
    y=515.0,
    width=247.0,
    height=54.941650390625
    ) 

#Button Tahap 4
def klik_button4():
    canvas.delete("text","judul")  # Menghapus teks button lain

    canvas.create_text(
        29.0,
        180.0,
        anchor="nw",
        text="Pada Tahap 4 bertujuan untuk membuat background model dari video yang dipilih. Anda bisa\nmengikuti langkah berikut:",
        fill="#000000",
        font=("RobotoRoman Regular", 20),
        tags="text"  
    )
    canvas.create_text(
        29.0,
        260.0,
        anchor="nw",
        text="1. Pilih file video yang telah dirubah sudut pandangnya.\n2. Klik button Jalankan untuk melihat hasil background modelling.\n3. Klik tombol selanjutnya untuk melanjutkan ke tahap berikutnya.",
        fill="#000000",
        font=("RobotoRoman Regular", 18),
        tags="text"  
    )

    #Menyembunyikan tampilan button
    hide_tombol()

    button_14.place(
        x=517.0,
        y=435.0,
        width=247.0,
        height=54.941650390625
    )  
    
    button_22.place(
    x=42.0,
    y=47.0,
    width=75.0,
    height=63.0
    )
    button_25.place(
    x=517.0,
    y=515.0,
    width=247.0,
    height=54.941650390625
    ) 
    
#Button Tahap 5
def klik_button5():
    canvas.delete("text","judul")  # Menghapus teks button lain
    canvas.create_text(
        29.0,
        180.0,
        anchor="nw",
        text="Pada Tahap 5 bertujuan untuk menerapkan metode background subtraction pada video yang telah\ndipilih. Tahapan ini menampilkan hasil deteksi objek yang bergerak menggunakan metode background\nsubtraction.",
        fill="#000000",
        font=("RobotoRoman Regular", 20),
        tags="text"  
    )

    #Menyembunyikan tampilan button
    hide_tombol()

    button_15.place(
        x=517.0,
        y=435.0,
        width=247.0,
        height=54.941650390625
    ) 
    button_22.place(
    x=42.0,
    y=47.0,
    width=75.0,
    height=63.0
    )
    button_26.place(
    x=517.0,
    y=515.0,
    width=247.0,
    height=54.941650390625
    )

#Button Tahap 6
def klik_button6():
    canvas.delete("text","judul")  # Menghapus teks button lain


    canvas.create_text(
        29.0,
        180.0,
        anchor="nw",
        text="Pada Tahap 6 bertujuan untuk menerapkan metode frame differencing pada video yang telah dipilih.\nTahapan ini menampilkan hasil deteksi objek yang bergerak menggunakan metode frame differencing.",
        fill="#000000",
        font=("RobotoRoman Regular", 20),
        tags="text"  
    )

    #Menyembunyikan tampilan button
    hide_tombol()

    button_16.place(
        x=517.0,
        y=435.0,
        width=247.0,
        height=54.941650390625
    ) 
    button_22.place(
    x=42.0,
    y=47.0,
    width=75.0,
    height=63.0
    )
    button_27.place(
    x=517.0,
    y=515.0,
    width=247.0,
    height=54.941650390625
    )

#Button Tahap 7
def klik_button7():
    canvas.delete("text","judul")  # Menghapus teks button lain


    canvas.create_text(
        29.0,
        180.0,
        anchor="nw",
        text="Pada Tahap 7 menampilkan hasil gabungan metode background subtraction dan frame differencing\nyang ditampilkan dalam kondisi thresholding.",
        fill="#000000",
        font=("RobotoRoman Regular", 20),
        tags="text"  
    )

    #Menyembunyikan tampilan button
    hide_tombol()

    button_17.place(
        x=517.0,
        y=435.0,
        width=247.0,
        height=54.941650390625
    ) 
    button_22.place(
    x=42.0,
    y=47.0,
    width=75.0,
    height=63.0
    )
    button_28.place(
    x=517.0,
    y=515.0,
    width=247.0,
    height=54.941650390625
    )

#Button Tahap 8
def klik_button8():
    canvas.delete("text","judul")  # Menghapus teks button lain


    canvas.create_text(
        29.0,
        180.0,
        anchor="nw",
        text="Pada Tahap 8 bertujuan untuk membuat kotak deteksi. Kotak deteksi dibuat dengan syarat nilai\nluas contour pada objek lebih dari 2500. Berdasarkan objek yang berhasil di deteksi maka akan\ndikenali sebagai kendaraan atau objek bergerak.",
        fill="#000000",
        font=("RobotoRoman Regular", 20),
        tags="text"  
    )

    #Menyembunyikan tampilan button
    hide_tombol()

    button_18.place(
        x=517.0,
        y=435.0,
        width=247.0,
        height=54.941650390625
    ) 
    button_22.place(
    x=42.0,
    y=47.0,
    width=75.0,
    height=63.0
    )
    button_29.place(
    x=517.0,
    y=515.0,
    width=247.0,
    height=54.941650390625
    )

#Button Tahap 9
def klik_button9():
    canvas.delete("text","judul")  # Menghapus teks button lain

    canvas.create_text(
        29.0,
        180.0,
        anchor="nw",
        text="Pada Tahap 9 bertujuan untuk menghitung kepadatan lalu lintas berdasarkan area yang dipakai oleh\nobjek yang berhasil di deteksi. Pada tahap ini menampilkan informasi tentang persentase area pada\nobjek, persentase jalan yang terpakai, persentase jalan yang tidak terpakai, dan kondisi lalu lintas",
        fill="#000000",
        font=("RobotoRoman Regular", 20),
        tags="text"
    )

    #Menyembunyikan tampilan button
    hide_tombol()

    button_19.place(
        x=517.0,
        y=435.0,
        width=247.0,
        height=54.941650390625
    ) 
    button_22.place(
    x=42.0,
    y=47.0,
    width=75.0,
    height=63.0
    )

#----------------------------------Fungsi button kembali
def klik_button22():
    canvas.delete("text")
    hide_tombol()
    button_1.place(
        x=182.0,
        y=300.0,
        width=270.0,
        height=64
    )
    button_2.place(
        x=505.0,
        y=300.0,
        width=270.0,
        height=64
    )
    button_3.place(
        x=828.0,
        y=300.0,
        width=270.0,
        height=64
    )
    button_4.place(
        x=182.0,
        y=388.0,
        width=270.0,
        height=64
    )
    button_5.place(
        x=505.0,
        y=388.0,
        width=270.0,
        height=64
    )
    button_6.place(
        x=828.0,
        y=388.0,
        width=270.0,
        height=64
    )
    button_7.place(
        x=182.0,
        y=476.0,
        width=270.0,
        height=64
    )
    button_8.place(
        x=505.0,
        y=476.0,
        width=270.0,
        height=64
    )
    button_9.place(
        x=828.0,
        y=476.0,
        width=270.0,
        height=64
    )
    canvas.create_text(
        385.0,
        189.0,
        anchor="nw",
        text="SELAMAT DATANG DI APLIKASI",
        fill="#000000",
        font=("RobotoRoman Bold", 36 * -1),
        tags="judul"
    )
    canvas.create_text(
        238.0,
        231.0,
        anchor="nw",
        text="PENDETEKSI TINGKAT KEPADATAN LALU LINTAS",
        fill="#000000",
        font=("RobotoRoman Bold", 36 * -1),
        tags="judul"
    )
#-----------------------------Fungsi Jalankan--------------------------------------
#Jalankan Tahap 1
#Fungsi Buka Video
selected_video = None
def klik_button10():
    global selected_video
    filename = filedialog.askopenfilename(initialdir="/", title="Select a Video file", filetypes=(("MP4 files", "*.mp4"), ("all files", "*.*")))
    if filename:
        print("Selected file:", filename)
        selected_video = filename
        messagebox.showinfo("File Dipilih", f"Nama file yang dipilih: {filename}")
    else:
        messagebox.showinfo("File Tidak Dipilih", "Tidak ada file yang dipilih.")


def klik_button20():
    global video_ubah
    filename = filedialog.askopenfilename(initialdir="/", title="Select a Video file", filetypes=(("MP4 files", "*.mp4"), ("all files", "*.*")))
    if filename:
        video_ubah=filename
        print("Selected file:", filename)
        selected_video = filename
        messagebox.showinfo("File Dipilih", f"Nama file yang dipilih: {filename}")
    else:
        messagebox.showinfo("File Tidak Dipilih", "Tidak ada file yang dipilih.")


#Fungsi Memutar video yang di pilih
def klik_button11():
    global selected_video
    if selected_video:
        cap = cv2.VideoCapture(selected_video)

        # Membuat jendela tampilan video di luar loop
        cv2.namedWindow('Video Original', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Video Original', 640, 480)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('Video Original', frame)
            # Menunggu 25 ms untuk tombol ditekan
            key = cv2.waitKey(25)
            # Jika jendela ditutup, hentikan loop
            if cv2.getWindowProperty('Video Original', cv2.WND_PROP_VISIBLE) < 1:
                break
        cap.release()
        cv2.destroyAllWindows()
    else:
        messagebox.showwarning("Peringatan", "Anda belum memilih video")
        
#Jalankan Tahap 2
def klik_button12():
    global selected_video
    if selected_video:
        cap = cv2.VideoCapture(selected_video)                      #Mengambil informasi video berupa:
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))       #Jumlah frame dalam video
        frame_rate = int(cap.get(cv2.CAP_PROP_FPS))                 #Frame Rate video
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))              #Lebar dan tinggi video
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        perspective_points = []

        def get_mouse_click(event, x, y, flags, param):         #Ketika Mouse Di Klik
            nonlocal perspective_points
            if event == cv2.EVENT_LBUTTONDOWN:                  #Koordinat di simpan dalam Perspective_points
                if len(perspective_points) < 4:
                    perspective_points.append((x, y))
                    cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
                    cv2.imshow('Video Original', frame)
                    # Jika telah dipilih 2 titik atau lebih, gambar garis antara titik-titik
            if len(perspective_points) >= 2:
                for i in range(len(perspective_points) - 1):
                    cv2.line(frame, perspective_points[i], perspective_points[i+1], (0, 255, 0), 2)
                # Jika telah dipilih 4 titik, gambar garis dari titik terakhir ke titik pertama
                if len(perspective_points) == 4:
                    cv2.line(frame, perspective_points[-1], perspective_points[0], (0, 255, 0), 2)
                cv2.imshow('Video Original', frame)

        cv2.namedWindow('Video Original', cv2.WINDOW_NORMAL)
        cv2.setMouseCallback('Video Original', get_mouse_click)

        while True:
            ret, frame = cap.read()         #Membaca Frame video
            if not ret:
                break

            for point in perspective_points:                    #Membuat Titik berdasarkan perspektif_point
                cv2.circle(frame, point, 5, (0, 255, 0), -1)    #yang telah di pilih dari mouse klik
            
            cv2.imshow('Video Original', frame)
            cv2.resizeWindow('Video Original', 640, 480)

            key = cv2.waitKey(25)
            #Mentransformasi dengan cara menekan tombol S
            if key & 0xFF == ord('s') or key & 0xFF == ord('S'):
                if len(perspective_points) == 4:
                    original_points = np.float32(perspective_points)      #Menyimpan titik perspektif asli      
                    new_points = np.float32([[0, 0], [640, 0], [640, 480], [0, 480]])   #new_points menyimpan titik tujuan (koordinat sudut-sudut jendela 640x480).
                    matrix = cv2.getPerspectiveTransform(original_points, new_points)   #menghitung matriks transformasi perspektif dari original_points ke new_points.

                    out_filename = filedialog.asksaveasfilename(defaultextension=".mp4") #Disimpan dengan ekstensi .mp4
                    if out_filename:
                        messagebox.showinfo("Info", "Harap tidak menutup jendela proses perubahan perspektif")
                        out = cv2.VideoWriter(out_filename, cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (640, 480)) #VideoWriter Menulis Video ke file
                        cap.set(cv2.CAP_PROP_POS_FRAMES, 0) #dimulai dari frame ke 0
                        #proses perubahan perspektif
                        while True:
                            ret, frame = cap.read()
                            if not ret:
                                break
                            warped_frame = cv2.warpPerspective(frame, matrix, (640, 480))
                            out.write(warped_frame)
                            cv2.imshow('proses perubahan perspektif', warped_frame)
                            if cv2.waitKey(1) & 0xFF == 27: #Ketika tombol esc di tekan atau jendela di close
                                break                       #Proses perubahan perspektif di hentikan secara paksa
                            if cv2.getWindowProperty('proses perubahan perspektif', cv2.WND_PROP_VISIBLE) < 1:
                                break
                        out.release()
                        cv2.destroyAllWindows()
                        messagebox.showinfo("Info", "proses perubahan perspektif video selesai.")
                        break
            if key & 0xFF == 27:
                break
            # Tambahkan penanganan untuk penutupan jendela
            if cv2.getWindowProperty('Video Original', cv2.WND_PROP_VISIBLE) < 1:
                break
        cap.release()
        cv2.destroyAllWindows()
    else:
        messagebox.showwarning("Peringatan", "Anda belum memilih video pada menu tahap 1")
        klik_button1()
        messagebox.showwarning("Peringatan", "Silahkan pilih file video terlebih dahulu")

video_ubah=""
#jalankan tahap 3
def klik_button13():
    global video_ubah
    if video_ubah:
        # Buka video menggunakan OpenCV
        cap = cv2.VideoCapture(video_ubah)
        cv2.namedWindow('Grayscale Video', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Grayscale Video', 640, 480)
        
        if not cap.isOpened():
            messagebox.showerror("Error", "Gagal membuka video")
            return
        try:
            # Loop untuk menampilkan citra grayscale
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                # Konversi frame ke citra grayscale
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # Tampilkan citra grayscale di jendela GUI
                cv2.imshow('Grayscale Video', gray_frame)
                # Tunggu tombol keyboard 'ESC' ditekan untuk keluar
                if cv2.waitKey(30) & 0xFF == 27:
                    break
                if cv2.getWindowProperty('Grayscale Video', cv2.WND_PROP_VISIBLE) < 1:
                    break
        
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
        
        finally:
            cap.release()
            cv2.destroyAllWindows()
    else:
        messagebox.showwarning("Peringatan", "Silahkan pilih file video terlebih dahulu")

#jalankan Tahap 4
def klik_button14():
    global video_ubah
    if video_ubah:
        cap = cv2.VideoCapture(video_ubah)
        # Akumulasi background
        background_frames = []
        num_background_frames = 100  # Jumlah f rame untuk diakumulasi
        cv2.namedWindow('Background Bersih', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Background Bersih', 640, 480)
        # Ambil beberapa frame awal untuk diakumulasi menjadi latar belakang
        for _ in range(num_background_frames):
            ret, frame = cap.read()
            if ret:
                background_frames.append(frame)
            else:
                break
        
        # Hitung median dari frame yang diambil
        accumulated_background = np.median(background_frames, axis=0).astype(np.uint8)  #mencari nilai median untuk membuat background modell
        # Hapus noise dari latar belakang
        accumulated_background = cv2.medianBlur(accumulated_background, 9) #Mengurangi noise dengan cara blur
        
        # Tampilkan latar belakang yang dihasilkan
        cv2.imshow('Background Bersih', accumulated_background)
        cv2.waitKey(0) #menunjukkan bahwa program akan menunggu selamanya sampai ada tombol yang ditekan. 
        cap.release()
        cv2.destroyAllWindows()
    else:
        messagebox.showwarning("Peringatan", "Anda belum memilih file video pada tahap 3")
        klik_button3()
        messagebox.showwarning("Peringatan", "Anda belum memilih video")

#jalankan tahap 5
def klik_button15():
    global video_ubah
    if video_ubah:
        # Buka video menggunakan OpenCV
        cap = cv2.VideoCapture(video_ubah)
        cv2.namedWindow('Background Subtraction', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Background Subtraction', 640, 480)

        if not cap.isOpened():
            messagebox.showerror("Error", "Gagal membuka video")
            return

        try:
            # Akumulasi beberapa frame awal untuk latar belakang
            num_background_frames = 100
            background_frames = []
            
            for _ in range(num_background_frames): #Membaca video dari awal frame dan disimpan pada
                ret, frame = cap.read()
                if not ret:
                    break
                background_frames.append(frame)     #variabel background_frames
            
            # Hitung median dari frame yang diambil                    #uint8 tipe data yang umum digunakan untuk gambar
            accumulated_background = np.median(background_frames, axis=0).astype(np.uint8)  #mencari nilai median untuk membuat background modell
            accumulated_background = cv2.medianBlur(accumulated_background, 21)             #Mengurangi noise dengan cara blur
            # Loop untuk melakukan background subtraction
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Kurangi frame dengan latar belakang yang dihasilkan
                bs_frame = cv2.absdiff(frame, accumulated_background)
                
                # Lakukan thresholding pada perbedaan frame (bs_frame)
                gray_bs_frame = cv2.cvtColor(bs_frame, cv2.COLOR_BGR2GRAY)
                _, thresholded_frame = cv2.threshold(gray_bs_frame, 30, 255, cv2.THRESH_BINARY)
                # Tampilkan frame hasil background subtraction di jendela GUI
                cv2.imshow('Background Subtraction', thresholded_frame)
                
                # Tunggu tombol keyboard 'ESC' ditekan untuk keluar
                if cv2.waitKey(30) & 0xFF == 27:
                    break
                if cv2.getWindowProperty('Background Subtraction', cv2.WND_PROP_VISIBLE) < 1: 
                    break
        
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
        
        finally:
            # Bebaskan sumber daya
            cap.release()
            cv2.destroyAllWindows()
    else:
        messagebox.showwarning("Peringatan", "Anda belum memilih file video pada tahap 3")
        klik_button3()
        messagebox.showwarning("Peringatan", "Silahkan pilih file video terlebih dahulu")

#jalankan tahap 6
def klik_button16():
    global video_ubah
    if video_ubah:
        # Buka video menggunakan OpenCV
        cap = cv2.VideoCapture(video_ubah)
        cv2.namedWindow('Frame Differencing', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Frame Differencing', 640, 480)
        
        if not cap.isOpened():
            messagebox.showerror("Error", "Gagal membuka video")
            return
        
        try:
            # Baca frame pertama sebagai frame referensi
            ret, prev_frame = cap.read()
            if not ret:
                messagebox.showerror("Error", "Gagal membaca frame pertama")
                return
            
            # Loop untuk melakukan frame differencing
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Hitung perbedaan antara frame saat ini dan frame sebelumnya
                bs_frame = cv2.absdiff(frame, prev_frame)
                gray_bs_frame = cv2.cvtColor(bs_frame, cv2.COLOR_BGR2GRAY)
                _, thresholded_frame = cv2.threshold(gray_bs_frame, 30, 255, cv2.THRESH_BINARY)
                
                # Tampilkan hasil frame differencing di jendela GUI
                cv2.imshow('Frame Differencing', thresholded_frame)
                # Update frame referensi
                prev_frame = frame
                
                # Tunggu tombol keyboard 'ESC' ditekan untuk keluar
                if cv2.waitKey(30) & 0xFF == 27:
                    break
                if cv2.getWindowProperty('Frame Differencing', cv2.WND_PROP_VISIBLE) < 1:
                    break
        
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
        
        finally:
            # Bebaskan sumber daya
            cap.release()
            cv2.destroyAllWindows()
    else:
        messagebox.showwarning("Peringatan", "Anda belum memilih file video pada tahap 3")
        klik_button3()
        messagebox.showwarning("Peringatan", "Silahkan pilih file video terlebih dahulu")
        
#jalankan tahap 7
def klik_button17():
    global video_ubah
    if video_ubah:
        # Buka video menggunakan OpenCV
        cap = cv2.VideoCapture(video_ubah)
        
        if not cap.isOpened():
            messagebox.showerror("Error", "Gagal membuka video")
            return
        
        try:
            # Akumulasi beberapa frame awal untuk background subtraction
            num_background_frames = 100
            background_frames = []
            
            # Mengambil beberapa frame pertama untuk dijadikan latar belakang
            for _ in range(num_background_frames):
                ret, frame = cap.read()
                if not ret:
                    break
                background_frames.append(frame)
            
            # Menghitung median dari frame yang diambil
            accumulated_background = np.median(background_frames, axis=0).astype(np.uint8)  #mencari nilai median untuk membuat background modell
            accumulated_background = cv2.medianBlur(accumulated_background, 21)             #Mengurangi noise dengan cara blur
            # Buka jendela GUI untuk menampilkan hasil
            cv2.namedWindow('Background Subtraction and Frame Differencing', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Background Subtraction and Frame Differencing', 640, 480)
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Proses background subtraction
                bs_frame = cv2.absdiff(frame, accumulated_background)
                
                # Proses frame differencing (perbandingan dengan frame sebelumnya)
                if 'prev_frame' in locals():
                    frame_diff = cv2.absdiff(frame, prev_frame)
                else:
                    frame_diff = np.zeros_like(frame)
                
                # Gabungkan hasil background subtraction dan frame differencing
                combined_frame = cv2.addWeighted(bs_frame, 0.5, frame_diff, 0.5, 0)
                
                # Konversi ke citra grayscale
                gray_frame = cv2.cvtColor(combined_frame, cv2.COLOR_BGR2GRAY)

                # Lakukan proses thresholding
                _, combined_frame_thresh = cv2.threshold(gray_frame, 30, 255, cv2.THRESH_BINARY)

                # Tampilkan hasil gabungan dalam satu jendela GUI
                cv2.imshow('Background Subtraction and Frame Differencing', combined_frame_thresh)
                # Simpan frame untuk frame differencing selanjutnya
                prev_frame = frame
                
                # Tunggu tombol keyboard 'ESC' ditekan untuk keluar
                if cv2.waitKey(30) & 0xFF == 27:
                    break
                if cv2.getWindowProperty('Background Subtraction and Frame Differencing', cv2.WND_PROP_VISIBLE) < 1:
                    break
        
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
        
        finally:
            # Bebaskan sumber daya
            cap.release()
            cv2.destroyAllWindows()
    else:
        messagebox.showwarning("Peringatan", "Anda belum memilih file video pada tahap 3")
        klik_button3()
        messagebox.showwarning("Peringatan", "Silahkan pilih file video terlebih dahulu")

# jalankan tahap 8
def klik_button18():
    global video_ubah
    if video_ubah:
        # Buka video menggunakan OpenCV
        cap = cv2.VideoCapture(video_ubah)
        
        if not cap.isOpened():
            messagebox.showerror("Error", "Gagal membuka video")
            return
        
        try:
            # Akumulasi beberapa frame awal untuk background subtraction
            num_background_frames = 100
            background_frames = []
            
            # Mengambil beberapa frame pertama untuk dijadikan latar belakang
            for _ in range(num_background_frames):
                ret, frame = cap.read()
                if not ret:
                    break
                background_frames.append(frame)
            
            if not background_frames:
                messagebox.showerror("Error", "Gagal mengumpulkan frame latar belakang")
                return

            # Menghitung median dari frame yang diambil
            accumulated_background = np.median(background_frames, axis=0).astype(np.uint8)  #mencari nilai median untuk membuat background modell
            accumulated_background = cv2.medianBlur(accumulated_background, 21)         #Mengurangi noise dengan cara blur
            # Buka jendela GUI untuk menampilkan hasil
            cv2.namedWindow('Hasil Deteksi', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Hasil Deteksi', 640, 480)
            cv2.namedWindow('Hasil Deteksi Kontur', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Hasil Deteksi Kontur', 640, 480)
            
            prev_frame = None
            
            # Membuat kernel untuk dilasi
            kernel = np.ones((15, 15), np.uint8)
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Proses background subtraction
                bs_frame = cv2.absdiff(frame, accumulated_background)
                
                # Proses frame differencing (perbandingan dengan frame sebelumnya)
                if prev_frame is not None:
                    frame_diff = cv2.absdiff(frame, prev_frame)
                else:
                    frame_diff = np.zeros_like(frame)
                
                prev_frame = frame.copy()
                
                # Gabungkan hasil background subtraction dan frame differencing
                combined_frame = cv2.addWeighted(bs_frame, 0.5, frame_diff, 0.5, 0)
                
                # Konversi ke citra grayscale
                gray_frame = cv2.cvtColor(combined_frame, cv2.COLOR_BGR2GRAY)
                
                # Lakukan proses thresholding
                _, combined_frame_thresh = cv2.threshold(gray_frame, 30, 255, cv2.THRESH_BINARY)
                
                # Lakukan dilasi pada hasil thresholding
                dilated_frame = cv2.dilate(combined_frame_thresh, kernel, iterations=1)
                
                # Temukan kontur pada hasil dilasi
                contours, _ = cv2.findContours(dilated_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #Chain Approx Simple digunakan untuk mengurangi kompleksitas data, mempercepat proses komputasi, dan memudahkan interpretasi bentuk atau kontur.
                
                # Buat salinan tampilan dilasi untuk digambar kotak persegi di atasnya
                dilated_with_boxes = cv2.cvtColor(dilated_frame, cv2.COLOR_GRAY2BGR)
                
                # Gambar kotak persegi panjang di atas area putih (kontur) pada tampilan dilasi
                for contour in contours:
                    if cv2.contourArea(contour) > 2500:
                        # Dapatkan koordinat bounding box dari kontur
                        x, y, w, h = cv2.boundingRect(contour)
                        
                        # Gambar kotak persegi di atas area putih (kontur)
                        cv2.rectangle(dilated_with_boxes, (x, y), (x + w, y + h), (255, 255, 255), 2)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        
                        # Tambahkan teks "kendaraan" pada bounding box
                        cv2.putText(frame, "kendaraan", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                        cv2.putText(dilated_with_boxes, "kendaraan", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                
                # Tampilkan frame asli (berwarna penuh) dengan kotak persegi hasil deteksi
                cv2.imshow('Hasil Deteksi', frame)
                cv2.imshow('Hasil Deteksi Kontur', dilated_with_boxes)
                
                # Tunggu tombol keyboard 'ESC' ditekan untuk keluar
                if cv2.waitKey(30) & 0xFF == 27:
                    break
                
                # Periksa status visibilitas jendela pertama
                if cv2.getWindowProperty('Hasil Deteksi', cv2.WND_PROP_VISIBLE) < 1:
                    break
                
                # Periksa status visibilitas jendela kedua
                if cv2.getWindowProperty('Hasil Deteksi Kontur', cv2.WND_PROP_VISIBLE) < 1:
                    break
                
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
        
        finally:
            # Bebaskan sumber daya
            cap.release()
            cv2.destroyAllWindows()
    
    else:
        messagebox.showwarning("Peringatan", "Anda belum memilih file video pada tahap 3")
        klik_button3()
        messagebox.showwarning("Peringatan", "Silahkan pilih file video terlebih dahulu")
        
# jalankan tahap 9
def klik_button19():
    global video_ubah
    if video_ubah:
        # Buka video menggunakan OpenCV
        cap = cv2.VideoCapture(video_ubah)
        
        if not cap.isOpened():
            messagebox.showerror("Error", "Gagal membuka video")
            return
        
        try:
            # Akumulasi beberapa frame awal untuk background subtraction
            num_background_frames = 100
            background_frames = []
            
            # Mengambil beberapa frame pertama untuk dijadikan latar belakang
            for _ in range(num_background_frames):
                ret, frame = cap.read()
                if not ret:
                    break
                background_frames.append(frame)
            
            # Menghitung median dari frame yang diambil
            accumulated_background = np.median(background_frames, axis=0).astype(np.uint8)  #mencari nilai median untuk membuat background modell
            accumulated_background = cv2.medianBlur(accumulated_background, 21)     #Mengurangi noise dengan cara blur
            # Buka jendela GUI untuk menampilkan hasil
            cv2.namedWindow('Hasil Akhir', cv2.WINDOW_NORMAL)
            # Mengatur properti jendela menjadi fullscreen
            #cv2.setWindowProperty('Hasil Akhir', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.resizeWindow('Hasil Akhir', 640, 480)
            cv2.namedWindow('HA Threshold', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('HA Threshold', 640, 480)
            
            prev_frame = None

            # Membuat kernel untuk dilasi
            kernel = np.ones((15, 15), np.uint8)
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                total_area_terpakai = 0
                # Proses background subtraction
                bs_frame = cv2.absdiff(frame, accumulated_background)
                
                # Proses frame differencing (perbandingan dengan frame sebelumnya)
                if prev_frame is not None:
                    frame_diff = cv2.absdiff(frame, prev_frame)
                else:
                    frame_diff = np.zeros_like(frame)
                
                prev_frame = frame.copy()
                
                # Gabungkan hasil background subtraction dan frame differencing
                combined_frame = cv2.addWeighted(bs_frame, 0.5, frame_diff, 0.5, 0)
                
                # Konversi ke citra grayscale
                gray_frame = cv2.cvtColor(combined_frame, cv2.COLOR_BGR2GRAY)
                
                # Lakukan proses thresholding
                _, combined_frame_thresh = cv2.threshold(gray_frame, 30, 255, cv2.THRESH_BINARY)
                
                # Lakukan dilasi pada hasil thresholding
                dilated_frame = cv2.dilate(combined_frame_thresh, kernel, iterations=1)
                
                # Temukan kontur pada hasil dilasi
                contours, _ = cv2.findContours(dilated_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                
                for contour in contours:
                    if cv2.contourArea(contour) > 2500:
                        x, y, w, h = cv2.boundingRect(contour)
                        cv2.rectangle(dilated_frame, (x, y), (x + w, y + h), (255, 255, 255), -1) #-1 ketebalan garis, karena negatif maka kotak deteksi di isi dengan warna putih

                for contour in contours:
                    if cv2.contourArea(contour) > 2500:
                        # Hitung kotak pembatas (bounding box) dari kontur
                        x, y, w, h = cv2.boundingRect(contour)
                        area_bbox = w * h  # Hitung luas kotak pembatas

                        # Tambahkan luas kotak pembatas ke total_area_terpakai
                        total_area_terpakai += area_bbox
                        # Hitung persentase luas area bounding box terhadap total luas frame
                        persentase_area = (area_bbox / (frame.shape[0] * frame.shape[1])) * 100
        
                        # Gambar kotak pembatas pada frame asli
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        # Tambahkan teks "kendaraan" pada bounding box
                        cv2.putText(frame, "kendaraan", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                        # Tampilkan teks persentase luas area di dalam bounding box
                        text = f"Persentase Area: {persentase_area:.2f}%"
                        cv2.putText(frame, text, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
                
                # Hitung total luas jalanan berdsarkan area frame 
                total_area_jalan = frame.shape[0] * frame.shape[1]
                # Menghitung sisa area yang tidak terpakai
                area_tidak_terpakai = total_area_jalan - total_area_terpakai
                # Hitung persentase area terpakai dan tidak terpakai
                persentase_area_terpakai = (total_area_terpakai / total_area_jalan) * 100
                percentage_area_tidak_terpakai = (area_tidak_terpakai / total_area_jalan) * 100

                # Tentukan kondisi lalu lintas berdasarkan persentase area terpakai
                if persentase_area_terpakai > 50:
                    traffic_condition = "Padat"
                    color = (0, 0, 255)     # Warna Merah
                elif 50 >= persentase_area_terpakai >= 30:
                    traffic_condition = "Ramai"
                    color = (0, 255, 255)   # Warna Kuning
                elif 30 > persentase_area_terpakai > 0:
                    traffic_condition = "Lancar"
                    color = (0, 255, 0)     # Warna Hijau
                else:
                    traffic_condition = "Lengang"
                    color = (255, 255, 255) # Warna Putih

                # Tampilkan keterangan "Kondisi Lalu Lintas" dengan warna putih
                cv2.putText(frame, "Kondisi Lalu Lintas:", (350, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                # Tampilkan kondisi lalu lintas dengan warna yang sesuai
                cv2.putText(frame, traffic_condition, (510, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                # Tampilkan presentase jalanan terpakai dengan warna putih
                cv2.putText(frame, "Jalanan Terpakai", (20, 425), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                cv2.putText(frame, ":", (215, 425), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                cv2.putText(frame, f" {persentase_area_terpakai:.2f}%", (220, 425), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                # Tampilkan presentase jalanan tidak terpakai dengan warna putih
                cv2.putText(frame, "Jalanan Tidak Terpakai", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                cv2.putText(frame, ":", (215, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                cv2.putText(frame, f" {percentage_area_tidak_terpakai:.2f}%", (220, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
                
                # Tampilkan frame asli (berwarna penuh) dengan kotak kontur hasil deteksi dan keterangan kondisi lalu lintas
                cv2.imshow('Hasil Akhir', frame)
                cv2.imshow('HA Threshold', dilated_frame)

                if cv2.waitKey(30) & 0xFF == 27:
                    break
                if cv2.getWindowProperty('Hasil Akhir', cv2.WND_PROP_VISIBLE) < 1:
                    break
                if cv2.getWindowProperty('HA Threshold', cv2.WND_PROP_VISIBLE) < 1:
                    break
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
        
        finally:
            # Bebaskan sumber daya
            cap.release()
            cv2.destroyAllWindows()
    
    else:
        messagebox.showwarning("Peringatan", "Anda belum memilih file video pada tahap 3")
        klik_button3()
        messagebox.showwarning("Peringatan", "Silahkan pilih file video terlebih dahulu")
#Menghilangkan Tombol
def hide_tombol():
    button_1.place_forget()
    button_2.place_forget()
    button_3.place_forget()
    button_4.place_forget()
    button_5.place_forget()
    button_6.place_forget()
    button_7.place_forget()
    button_8.place_forget()
    button_9.place_forget()
    button_10.place_forget()
    button_11.place_forget()
    button_12.place_forget()
    button_13.place_forget()
    button_14.place_forget()
    button_15.place_forget()
    button_16.place_forget()
    button_17.place_forget()
    button_18.place_forget()
    button_19.place_forget()
    button_20.place_forget()
    button_21.place_forget()
    button_22.place_forget()
    button_23.place_forget()
    button_24.place_forget()
    button_25.place_forget()
    button_26.place_forget()
    button_27.place_forget()
    button_28.place_forget()
    button_29.place_forget()
#-----------------------------Tombol--------------------------------------
button_image_1 = PhotoImage(
    file=relative_to_assets("Button-1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button1,
    relief="flat",
)
button_1.place(
    x=182.0,
    y=300.0,
    width=270.0,
    height=64
)

button_image_2 = PhotoImage(
    file=relative_to_assets("Button-2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button2,
    relief="flat",
)
button_2.place(
    x=505.0,
    y=300.0,
    width=270.0,
    height=64
)

button_image_3 = PhotoImage(
    file=relative_to_assets("Button-3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button3,
    relief="flat",
)
button_3.place(
    x=828.0,
    y=300.0,
    width=270.0,
    height=64
)

button_image_4 = PhotoImage(
    file=relative_to_assets("Button-4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button4,
    relief="flat",
)
button_4.place(
    x=182.0,
    y=388.0,
    width=270.0,
    height=64
)

button_image_5 = PhotoImage(
    file=relative_to_assets("Button-5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button5,
    relief="flat",
)
button_5.place(
    x=505.0,
    y=388.0,
    width=270.0,
    height=64
)

button_image_6 = PhotoImage(
    file=relative_to_assets("Button-6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button6,
    relief="flat",
)
button_6.place(
    x=828.0,
    y=388.0,
    width=270.0,
    height=64
)

button_image_7 = PhotoImage(
    file=relative_to_assets("Button-7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button7,
    relief="flat",
)
button_7.place(
    x=182.0,
    y=476.0,
    width=270.0,
    height=64
)

button_image_8 = PhotoImage(
    file=relative_to_assets("Button-8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button8,
    relief="flat",
)
button_8.place(
    x=505.0,
    y=476.0,
    width=270.0,
    height=64
)

button_image_9 = PhotoImage(
    file=relative_to_assets("Button-9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button9,
    relief="flat",
)
button_9.place(
    x=828.0,
    y=476.0,
    width=270.0,
    height=64
)

#Button Pilih File Video
button_image_10 = PhotoImage(
    file=relative_to_assets("btn_10.png"))
button_10 = Button( #pada tampilan Home
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button10,
    relief="flat"
)
button_20 = Button( #pada tampilan tahap2
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button20,
    relief="flat"
)

button_image_11 = PhotoImage(
    file=relative_to_assets("btn_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button11,
    relief="flat"
)
#button selanjutnya
button_image_21 = PhotoImage(
    file=relative_to_assets("btn_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button2,
    relief="flat"
)
button_23 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button3,
    relief="flat"
)
button_24 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button4,
    relief="flat"
)
button_25 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button5,
    relief="flat"
)
button_26 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button6,
    relief="flat"
)
button_27 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button7,
    relief="flat"
)
button_28 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button8,
    relief="flat"
)
button_29 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button9,
    relief="flat"
)
#button Home
button_home = PhotoImage(
    file=relative_to_assets("btn_home.png"))
button_22 = Button(
    image=button_home,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button22,
    relief="flat"
)

#----------------------------------------Tombol Jalankan---------------------------
button_image_12 = PhotoImage(
    file=relative_to_assets("btn_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button12,
    relief="flat"
)
button_13 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button13,
    relief="flat"
)
button_14 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button14,
    relief="flat"
)
button_15 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button15,
    relief="flat"
)
button_16 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button16,
    relief="flat"
)
button_17 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button17,
    relief="flat"
)
button_18 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button18,
    relief="flat"
)
button_19 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=klik_button19,
    relief="flat"
)

#------------------------------------------------------------------------------------

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    1140.0,
    86.0,
    image=image_image_1
)

canvas.create_rectangle(
    0.0,
    595.0,
    1280.0,
    720.0,
    fill="#378CE7",
    outline="")

canvas.create_text(
    420.0,
    657.0,
    anchor="nw",
    text="@copyright Mohamad Yanuar Wardinnansah - 2011500705",
    fill="#000000",
    font=("RobotoRoman Regular", 20 * -1)
)

canvas.create_text(
    385.0,
    189.0,
    anchor="nw",
    text="SELAMAT DATANG DI APLIKASI",
    fill="#000000",
    font=("RobotoRoman Bold", 36 * -1),
    tags="judul"
)
canvas.create_text(
    238.0,
    231.0,
    anchor="nw",
    text="PENDETEKSI TINGKAT KEPADATAN LALU LINTAS",
    fill="#000000",
    font=("RobotoRoman Bold", 36 * -1),
    tags="judul"
)

window.resizable(False, False)
window.mainloop()
