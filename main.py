import os
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import requests
import pytesseract
from pdf2image import convert_from_bytes

app = FastAPI()

AUTH_TOKEN = "test123" # This is just given in the case of authentication

class PDFRequest(BaseModel):
    pdf_url: str

@app.post("/extract_text")
async def extract_text(request: Request, body: PDFRequest):
    # Check authorization header
    auth_header = request.headers.get("authorization")
    if not auth_header or auth_header != f"Bearer {AUTH_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    # Fetch the PDF
    resp = requests.get(body.pdf_url)
    if resp.status_code != 200:
        raise HTTPException(status_code=400, detail="Could not fetch PDF from provided URL")

    pdf_bytes = resp.content

    # Convert PDF to images
    try:
        images = convert_from_bytes(pdf_bytes)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error converting PDF to images: {e}")

    # Extract text from all pages
    all_text = []
    for img in images:
        text = pytesseract.image_to_string(img)
        all_text.append(text)

    extracted_text = "\n".join(all_text)

    return {"extracted_text": extracted_text}

# Add this block to listen on port 8080
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))  # Get PORT from environment or default to 8080
    uvicorn.run(app, host="0.0.0.0", port=port)
