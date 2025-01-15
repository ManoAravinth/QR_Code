import qrcode
from PIL import Image
qr=qrcode.QRCode (version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=2, border=4,)
qr.add_data("https://www.figma.com/proto/efIeEcJhnjx7No7dVmxiZR/Portfolio-Design-(Community)?node-id=16-6&t=jI3Ureap9KzRQKBt-0&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1")
qr.make(fit=True)
img=qr.make_image(fill_color="red", back_color="white")
img.save("new_QR.jpeg")