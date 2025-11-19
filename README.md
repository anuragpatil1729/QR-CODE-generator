# QR Code Generator

A simple and user-friendly desktop application for generating QR codes from text or URLs.

## Features

- 🎯 Generate QR codes from any text or URL
- 💾 Save QR codes as PNG images
- 👁️ Preview generated QR codes in the application
- 🖥️ Clean and intuitive GUI built with Tkinter
- ⚡ Fast and lightweight

## Prerequisites

Before running this application, make sure you have Python installed on your system (Python 3.6 or higher recommended).

## Installation

1. **Clone or download this repository**

2. **Install required dependencies**

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install qrcode[pil] pillow
```

## Usage

1. **Run the application**

```bash
python main.py
```

2. **Generate a QR Code**
   - Enter your text or URL in the input field
   - Click the "Generate QR Code" button
   - Choose a location and filename to save your QR code
   - The QR code will be saved and displayed in the application window

## Requirements

Create a `requirements.txt` file with the following content:

```
qrcode[pil]==7.4.2
Pillow==10.1.0
```

## Screenshots

The application window includes:
- Text input field for entering data
- Generate button to create QR codes
- Preview area to display the generated QR code

## Technical Details

- **QR Code Settings:**
  - Error Correction: Medium (ERROR_CORRECT_M)
  - Box Size: 10 pixels
  - Border: 4 boxes
  - Colors: Black on white background

- **Output:**
  - Format: PNG
  - Display Size: 200x200 pixels
  - Saved at original resolution

## Customization

You can modify the QR code parameters in `main.py`:

```python
qr = qrcode.QRCode(
    version=None,           # Auto-size or set 1-40
    error_correction=...,   # L, M, Q, or H
    box_size=10,           # Pixel size of each box
    border=4,              # Border thickness in boxes
)
```

## Error Handling

The application includes:
- Validation for empty input
- File dialog cancellation handling
- Success/error message notifications

## License

This project is open source and available for personal and commercial use.

## Contributing

Contributions, issues, and feature requests are welcome!

## Support

If you encounter any issues or have questions, please open an issue in the repository.

---

**Enjoy generating QR codes!** 📱
