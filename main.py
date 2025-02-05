from fastapi import FastAPI, File, UploadFile
import torch
import uvicorn
from PIL import Image
import io

# Load the trained YOLOv11 model
MODEL_PATH = "best.pt"  # Replace with your actual model file path
model = torch.hub.load("ultralytics/yolov5", "custom", path=MODEL_PATH)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Pipeline Leak Detection API is running!"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Read and preprocess the image
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    
    # Perform inference
    results = model(image)
    
    # Extract detections
    detections = results.pandas().xyxy[0].to_dict(orient="records")
    
    return {"detections": detections}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
