import qrcode
from PIL import Image
import os

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)  # Save the QR code image
    return filename  # Return the filename

if __name__ == "__main__":
    # Directory to save the QR code images
    output_dir = "qr_codes"
    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

    # List of data for multiple QR codes
    data_list = ["https://www.example.com", "https://www.example.org", "https://www.example.net"]

    # Generate and save each QR code
    image_paths = []  # List to store the paths of generated images
    for i, data in enumerate(data_list, start=1):
        filename = os.path.join(output_dir, f"qr_code_{i}.png")  # Generate filename
        image_path = generate_qr_code(data, filename)
        image_paths.append(image_path)
        print(f"QR code {i} generated and saved as {filename}")

    # Provide download links for the images
    print("\nDownload Links:")
    for i, path in enumerate(image_paths, start=1):
        print(f"[Download QR Code {i}]({path})")
