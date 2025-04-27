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


import cv2
import webbrowser
import qrcode

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
    _, img = cap.read()

    data, bbox, _ = detector.detectAndDecode(img)
    if data: 
        a = data
        break

    cv2.imshow("QRCODEscanner", img)
    if cv2.waitKey(1) == ord("q"):
        break

b = webbrowser.open(str(a))
cap.release()
cv2.destroyAllWindows()
'''

import cv2
import datetime
import sys

def intro():
    print("===============================================================Welcome to Contact Tracing App=====================================")
    while True:
        choice = input("1. Press 's' to start the system, \n2. Press 'q' to exit")
        if choice == ord("q"):
            sys.exit()
        elif choice == ord("s"):
            print("The system has now started. Show your QR code. ")
            qr_code_scan()

def qr_code_scan():
    count = 0
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    while True: 
        _, img = cap.read()
        data, bbox, _ = detector.detectAndDecode(img)

        if data:
            date_and_time = get_date_and_time()
            a = data
            print("QR Code scanned \n" + a + "\n")
            count = generate_text_file(a, count, date_and_time)
        cv2.imshow("QRCODEscanner", img)

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

def get_date_and_time(current_time):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_time
        
def generate_text_file(a, current_time, number):
    file1 = open("file1.txt", "w")
    file1.write(a+ "\n")


# FUll Name, Email, Phone


def main():
    intro()
    qr_code_scan()

if __name__ == "__main__":
    main()
