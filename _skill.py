from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import pyperclip
import base64
import os
import dotenv
dotenv.load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

def create_poster(prompt:str):

    try:

        response = client.models.generate_images(
            model='imagen-4.0-generate-001',
            
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images= 1,
                aspect_ratio="9:16",
                output_mime_type="image/png",
                
            )
        )
        for generated_image in response.generated_images:
            #generated_image.image.show()
            img_bytes = generated_image.image.image_bytes 
            img_base64 = base64.b64encode(img_bytes).decode('utf-8')
            #pyperclip.copy('data:image/png;base64,' + img_base64)
            print(img_base64)
            return {"success": True, "response":"Image generated successfully", "file": img_base64,"file_type":"image/png"}

    except Exception as e:
        print("Error generating image:", e)
        return {"success": False, "response": str(e)}

