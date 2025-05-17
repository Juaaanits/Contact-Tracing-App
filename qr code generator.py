import qrcode

# Data in the format your scanner expects
data = "Jane Smith|25|jane.smith@example.com|5551234567|456 Oak St"

# Create QR code
qr = qrcode.make(data)

# Save it to file
qr.save("test_qr.png")

print("QR code saved as test_qr.png")
