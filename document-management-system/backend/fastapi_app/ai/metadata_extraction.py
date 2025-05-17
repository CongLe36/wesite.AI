from typing import Dict, Any
import pytesseract
from PIL import Image
import re

def extract_text_from_image(image_path: str) -> str:
    """Extract text from an image using OCR."""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def extract_metadata_from_text(text: str) -> Dict[str, Any]:
    """Extract metadata from the given text."""
    metadata = {}
    
    # Example regex patterns for extracting metadata
    date_pattern = r'\b\d{4}-\d{2}-\d{2}\b'  # YYYY-MM-DD format
    number_pattern = r'\bCVD-\d{3}\b'  # Example for document number
    
    # Extracting date
    date_matches = re.findall(date_pattern, text)
    if date_matches:
        metadata['date'] = date_matches[0]  # Take the first match
    
    # Extracting document number
    number_matches = re.findall(number_pattern, text)
    if number_matches:
        metadata['document_number'] = number_matches[0]  # Take the first match
    
    # Additional metadata extraction logic can be added here
    
    return metadata

def extract_metadata_from_image(image_path: str) -> Dict[str, Any]:
    """Extract metadata from an image file."""
    text = extract_text_from_image(image_path)
    metadata = extract_metadata_from_text(text)
    return metadata