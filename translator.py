import pytesseract
from google.cloud import translate_v2 as translate

# Set up Tesseract OCR (update the path to your Tesseract executable if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set up Google Cloud Translation API (replace 'YOUR_API_KEY' with your actual API key)
translate_client = translate.Client(api_key='YOUR_API_KEY')

import cv2

# capture, process, and translate frames in real time
def translate_text_from_frame():
    cap = cv2.VideoCapture(0)  # Open the default camera (index 0)

    while True:
        ret, frame = cap.read()  # Read a frame from the camera
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

        # Use OCR to extract text from the frame
        extracted_text = pytesseract.image_to_string(gray)

        # Translate the extracted text using Google Cloud Translation API
        if extracted_text:
            translated_text = translate_client.translate(extracted_text, target_language='en')  # Translate to English
            print("Extracted Text:", extracted_text)
            print("Translated Text:", translated_text['input'])
        
        # Display the original frame with extracted text
        cv2.imshow('Real-Time Translator', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit the loop and close the window
            break

    cap.release()  # Release the camera
    cv2.destroyAllWindows()  # Close all OpenCV windows

#start real-time translation
translate_text_from_frame()
