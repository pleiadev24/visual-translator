import cv2
import pytesseract
from google.cloud import translate_v2 as translate

# Set up Tesseract OCR (update the path to your Tesseract executable if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set up Google Cloud Translation API (replace 'YOUR_API_KEY' with your actual API key)
translate_client = translate.Client(api_key='YOUR_API_KEY')

# Function to preprocess, capture, process, and translate frames in real time
def translate_text_from_frame():
    try:
        cap = cv2.VideoCapture(0)  # Open the default camera (index 0)
        
        while True:
            ret, frame = cap.read()  # Read a frame from the camera
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale
            
            # Preprocess the frame using thresholding
            _, thresholded = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)  # Adjust threshold value as needed

            # Use OCR to extract text from the preprocessed frame
            extracted_text = pytesseract.image_to_string(thresholded)

            # Translate the extracted text using Google Cloud Translation API
            if extracted_text:
                try:
                    translated_text = translate_client.translate(extracted_text, target_language='en')  # Translate to English
                    print("Extracted Text:", extracted_text)
                    print("Translated Text:", translated_text['input'])
                except Exception as translation_error:
                    print("Translation Error:", translation_error)
            
            # Display the original frame and the preprocessed frame with extracted text
            cv2.imshow('Original Frame', frame)
            cv2.imshow('Thresholded Frame', thresholded)

            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit the loop and close the window
                break

    except Exception as e:
        print("An error occurred:", e)
    finally:
        cap.release()  # Release the camera
        cv2.destroyAllWindows()  # Close all OpenCV windows

# Call the function to start real-time translation
translate_text_from_frame()
