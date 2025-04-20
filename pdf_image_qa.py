import fitz  # PyMuPDF
from PIL import Image
import tempfile

def handle_file(file):
    if file.name.endswith(".pdf"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file.read())
            doc = fitz.open(tmp.name)
            text = ""
            for page in doc:
                text += page.get_text()
            doc.close()
        return f"📄 Extracted Text from PDF:\n{text[:1000]}..."
    
    elif file.name.lower().endswith(("png", "jpg", "jpeg")):
        image = Image.open(file)
        return f"🖼️ Image uploaded. Add vision-based AI to analyze content."
    
    return "❌ Unsupported file format."
