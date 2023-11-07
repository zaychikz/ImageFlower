from fastapi import FastAPI , Request
import tensorflow as tf
import base64
import io
from PIL import Image
from tensorflow.keras.applications.resnet50 import preprocess_input

app = FastAPI()

def preprocessbase64(uri):
    encoded_data = uri.split(',')[1]
    decoded_data = base64.b64decode(encoded_data)
    image = Image.open(io.BytesIO(decoded_data))
    image = image.convert("RGB")
    image = image.resize((256, 256))
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    preprocessed_image = preprocess_input(image_array)
    return preprocessed_image
    
@app.get("/")
def root():
    return {"message": "This is my api"}

@app.get("/api/getpreimg")
async def read_str(request : Request):
    item = await request.json()
    item_str = item['img']
    img = preprocessbase64(item_str)
    
    return {"img":img.tolist()}