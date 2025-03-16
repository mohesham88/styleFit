import requests
from PIL import Image
from io import BytesIO
from google import genai
import json
import re

from dotenv import load_dotenv
import os

load_dotenv()
genai_key = os.getenv("GEMINI_API")

PROMPT = """
```
Generate a JSON object representing a clothing item with the following structure.  

### **JSON Structure:**  
```json
{
    "Id": "<Unique identifier>",  
    "category": "<One of the predefined category enums>",  
    "Color": "<A relevant color based on common clothing colors>",  
    "Season": "<One of the predefined season enums>",  
    "Type": "<One of the predefined type enums>",  
    "pattern": "<A common clothing pattern such as Solid, Striped, Plaid, Floral>",  
    "material": "<A common clothing material such as Cotton, Polyester, Silk, Wool>",  
    "Description": "<A short, well-written description of the clothing item>",  
    "Image": "<A valid image URL>"
}
```

### **Constraints:**  
1. **Strict Enum Compliance:**  
   - The values for `"category"`, `"Season"`, and `"Type"` **must strictly** match the predefined enums.  
   - If the category is missing or unclear, choose from the **CategoryEnum** list.  
   - If the season is missing, default to **"other"** instead of generating a random value.  
   - If the type is missing, default to **"other"**.  

2. **Data Generation Rules:**  
   - `"Color"`: Must be a valid color name (e.g., "Red", "Blue", "Beige").  
   - `"pattern"`: Choose from common patterns (e.g., "Solid", "Striped", "Plaid", "Floral", "Printed").  
   - `"material"`: Choose from standard materials (e.g., "Cotton", "Polyester", "Silk", "Wool", "Linen").  
   - `"Description"`: Should be **concise** and **descriptive**. Example:  
     - *"A lightweight cotton summer dress with a floral pattern, perfect for warm days."*  
   - `"Image"`: Should be a **valid** image URL in `"https://example.com/image.jpg"` format.  

3. **Output Format:**  
   - **Return the response as a JSON object only, with no additional text or explanation.**  
   - Ensure all values are properly quoted and formatted as a valid JSON.  

### **Example Output:**  
```json
{
    "Id": "abc123",
    "category": "dress",
    "Color": "Blue",
    "Season": "summer",
    "Type": "casual",
    "pattern": "Floral",
    "material": "Cotton",
    "Description": "A lightweight cotton summer dress with a floral pattern, perfect for warm days.",
    "Image": "https://example.com/dress.jpg"
}
```
```
"""


def get_genai_response(image, image_url, user_id):
    # Send to Gemini API
    client = genai.Client(api_key=genai_key)
    prompt = PROMPT + f"\nHere is IMAGE_URL {image_url}\n"
    prompt += f"\nHere is the ID for the JSON Object {user_id}\n"
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=[image, prompt]
    )

    return response


def download_image(image_url):
    # Download image from URL
    response = requests.get(image_url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        print(type(image))
        return image
    else:
        print("Failed to download image")


def generate_item_schema(response_text):
    match = re.search(r"```json\s*(\{.*\})\s*```", response_text, re.DOTALL)

    if match:
        json_obj = json.loads(match.group(1))
        return json_obj
    else:
        print("Failed to match regex expression, check the response back")
        # TODO: log response in some file
        return None


def convert_uploadedfile_to_pil(uploaded_file):
    image = Image.open(uploaded_file)
    return image


def item_generator(image, image_url, user_id):
    image_url = "https://res.cloudinary.com/dyulsrqq6/image/upload/v1742127980/l5zngyliewelflpdwcxw.webp"
    image = download_image(image_url)
    response = get_genai_response(image=image, image_url=image_url, user_id=user_id)
    print(response.text)


if __name__ == "__main__":
    download_image(
        "https://res.cloudinary.com/dyulsrqq6/image/upload/v1742127980/l5zngyliewelflpdwcxw.webp"
    )
