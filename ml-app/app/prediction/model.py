import io
import base64
import transformers
from PIL import Image
from transformers import pipeline, AutoImageProcessor
from app.core.logger import setup_logging
from app.core.config import settings

logger = setup_logging()

# Set logging level to reduce warnings
transformers.logging.set_verbosity_error()

class DogCatPredictor:
    def __init__(self):
        try:
            # Initialize image processor with explicit configuration
            self.image_processor = AutoImageProcessor.from_pretrained(
                settings.MODEL_NAME,
                size={"shortest_edge": settings.MAX_IMAGE_SIZE},
                do_resize=True,
                do_normalize=True,
                do_rescale=True
            )
            
            # Initialize the pipeline with explicit image processor
            self.classifier = pipeline(
                "image-classification", 
                model=settings.MODEL_NAME,
                image_processor=self.image_processor
            )
            
            logger.info(f"Successfully initialized model: {settings.MODEL_NAME}")
            
        except Exception as e:
            logger.error(f"Error initializing image classification pipeline: {e}")
            raise
    
    def predict(self, image_data):
        if isinstance(image_data, str):
            image_bytes = base64.b64decode(image_data)
            image = Image.open(io.BytesIO(image_bytes))
        elif isinstance(image_data, bytes):
            image = Image.open(io.BytesIO(image_data))
        else:
            image = image_data
        
        logger.info(f"Image type before prediction: {type(image)}")
        
        try:
            results = self.classifier(image, top_k=10)
        except Exception as e:
            logger.error(f"Error during image classification: {e}")
            raise
        
        dog_score = 0
        cat_score = 0
        
        for result in results:
            label = result['label'].lower()
            score = result['score']
            
            if 'dog' in label:
                dog_score += score
            elif 'cat' in label:
                cat_score += score
        
        # if no dog/cat found, classify based on top prediction
        if dog_score == 0 and cat_score == 0:
            top_prediction = results[0]['label'].lower()
            if any(animal in top_prediction for animal in ['dog', 'puppy', 'canine']):
                prediction = "dog"
                confidence = results[0]['score']
                dog_score = confidence
            else:
                prediction = "cat"
                confidence = results[0]['score']
                cat_score = confidence
        else:
            if dog_score > cat_score:
                prediction = "dog"
                confidence = dog_score
            else:
                prediction = "cat"
                confidence = cat_score
        
        return {
            "prediction"    : prediction,
            "confidence"    : float(confidence),
            "dog_score"     : float(dog_score),
            "cat_score"     : float(cat_score)
        }