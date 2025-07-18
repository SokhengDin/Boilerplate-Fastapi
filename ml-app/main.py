import base64

from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import JSONResponse
from app.prediction.model import DogCatPredictor
from app.utils.image_processor import validate_image, resize_image, convert_to_rgb

from app.core.config import settings
from app.core.logger import setup_logging

logger = setup_logging()

app = FastAPI(
    title   = settings.APP_NAME,
    version = settings.APP_VERSION
)

predictor = DogCatPredictor()

@app.get("/")
async def root():
    return {"message": settings.APP_NAME, "version": settings.APP_VERSION}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    try:
        image_data = await file.read()
        
        is_valid, result = validate_image(image_data)
        if not is_valid:
            raise HTTPException(status_code=400, detail=result)
        
        image = result
        image = convert_to_rgb(image)
        image = resize_image(image)
        
        prediction = predictor.predict(image)
        logger.info(f"Prediction result: {prediction}")
        
        return JSONResponse(
            content = {
                "filename"      : file.filename,
                "prediction"    : prediction["prediction"],
                "confidence"    : round(prediction["confidence"], 4),
                "scores"        : {
                    "dog"   : round(prediction["dog_score"], 4),
                    "cat"   : round(prediction["cat_score"], 4)
                }
            }
        )
    
    except HTTPException:
        # Re-raise HTTPException without modification
        raise
    except Exception as e:
        import traceback
        error_detail = f"Prediction failed: {str(e)}"
        traceback_str = traceback.format_exc()
        logger.error(f"{error_detail}\n{traceback_str}")
        raise HTTPException(status_code=500, detail=f"{error_detail}\nTraceback: {traceback_str}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host        = "0.0.0.0",
        port        = settings.API_PORT,
        reload_dirs = ["app"],
        reload      = True
    )
