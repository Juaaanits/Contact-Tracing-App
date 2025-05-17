'''
Pseudocode:

Ask for the user to input their qr code
capture image


Start webcam
While webcam is running:
    DIsplay frame
    Try to detect QR code
    If QR code detected:
        Decode QR data (Full Name, Age, Email, Contact Number, Addresss)
        Get current date and time
        Save data + timestamp to text file
    If 'q' is pressed:
        Exit loop
Release webcam

'''

import cv2
import datetime
import sys
import os
import time

def get_date_and_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_to_txt(data_fields, timestamp):
    file_path = "contact_tracing.txt"
    file_exists = os.path.isfile(file_path)

    with open(file_path, mode="a") as file:
        if not file_exists:
            file.write("Full Name | Age | Email | Contact Number | Address | Timestamp\n")
            file.write("=" * 70 + "\n")
        file.write(" | ".join(data_fields) + f" | {timestamp}\n")
        file.write("-" * 70 + "\n")

def check_details(qr_data):
    try:
        fields = qr_data.strip().split("|")
        if len(fields) != 5:
            print("[!] Invalid QR format. Expected 5 fields separated by '|'.")
            return False
        
        timestamp = get_date_and_time()
        save_to_txt(fields, timestamp)
        print(f"Data saved to TXT file: {fields} at {timestamp}")
        return True
    
    except Exception as e:
        print(f"Error processing QR data: {e}")
        return False

def intro():
    print("===============================================================")
    print("      Welcome to the Open Contact Tracing QR Scanner App")
    print("===============================================================\n")
    while True:
        choice = input("1. Press 's' to start the system, \n2. Press 'q' to exit\n")
        if choice.lower() == "q":
            sys.exit()
        elif choice.lower() == "s":
            print("The system has now started. Show your QR code.")
            qr_code_scan()
            break

def qr_code_scan():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[!] Unable to access webcam.")
        sys.exit()

    detector = cv2.QRCodeDetector()
    last_scanned = ""
    last_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[!] Failed to access webcam.")
            break

        data, bbox, _ = detector.detectAndDecode(frame)
        if data:
            if data != last_scanned or time.time() - last_time > 5:
                print(f"\n[QR Detected]: {data}")
                if check_details(data):
                    last_scanned = data
                    last_time = time.time()
                    cv2.putText(frame, "QR Code Scanned", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Open Tracing QR Scanner", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Q pressed, exiting...")
            break



    cap.release()
    cv2.destroyAllWindows()
    print("Exiting QR code scanner.")

def main():
    intro()

if __name__ == "__main__":
    main()

