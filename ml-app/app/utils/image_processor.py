from PIL import Image
import io
import base64

def validate_image(image_data):
    try:
        if isinstance(image_data, str):
            image_bytes = base64.b64decode(image_data)
            image = Image.open(io.BytesIO(image_bytes))
        elif isinstance(image_data, bytes):
            image = Image.open(io.BytesIO(image_data))
        else:
            image = image_data
        
        # Check if image format is supported (allow None and common formats)
        if image.format and image.format.upper() not in ['JPEG', 'PNG', 'JPG', 'WEBP', 'BMP', 'TIFF']:
            return False, f"Unsupported image format: {image.format}"
        
        # Verify image can be converted to RGB
        try:
            image.convert('RGB')
        except Exception:
            return False, "Image cannot be converted to RGB format"
        
        return True, image
    except Exception as e:
        return False, f"Invalid image: {str(e)}"

def resize_image(image, max_size=(224, 224)):
    image.thumbnail(max_size, Image.Resampling.LANCZOS)
    return image

def convert_to_rgb(image):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    return image