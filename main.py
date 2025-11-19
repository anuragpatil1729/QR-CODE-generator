import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox, filedialog


def generate_qr():
    data = entry_data.get().strip()
    if not data:
        messagebox.showerror("Error", "Please enter some text or URL.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")],
        title="Save QR Code As"
    )

    if not file_path:
        return

    # Create QR
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

    # Display in GUI
    img_resized = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img_resized)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

    messagebox.showinfo("Success", "QR Code generated and saved!")


# GUI Setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.resizable(False, False)

tk.Label(root, text="Enter Text / URL for QR Code:", font=("Arial", 12)).pack(pady=10)

entry_data = tk.Entry(root, width=40, font=("Arial", 12))
entry_data.pack(pady=5)

btn_generate = tk.Button(root, text="Generate QR Code", font=("Arial", 12), command=generate_qr)
btn_generate.pack(pady=15)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()
