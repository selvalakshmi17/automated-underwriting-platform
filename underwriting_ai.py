import cv2
import pytesseract
from PIL import Image
import os

# Document Analysis - Extract Text
def extract_text_from_document(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# Computer Vision - Analyze Property Image
def assess_property_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(blur, 50, 150)
    damage_detected = cv2.countNonZero(edges) > 50000  # basic check
    return "Risky" if damage_detected else "Safe"

# Risk Assessment Rule Engine
def calculate_risk(text, image_result):
    if "fire" in text.lower() or image_result == "Risky":
        return "High Risk"
    return "Low Risk"

# Main driver
if __name__ == "__main__":
    doc_text = extract_text_from_document("sample_doc.png")
    image_status = assess_property_image("sample_property.jpg")
    risk = calculate_risk(doc_text, image_status)

    print("Extracted Report:", doc_text[:300])
    print("Image Analysis:", image_status)
    print("Final Risk Assessment:", risk)
