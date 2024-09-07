from flask import Flask, render_template, request, jsonify
import base64
import anthropic
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json

app = Flask(__name__)

ANTHROPIC_API_KEY = 'your-token'
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def capture_screenshot(url, width=1024, height=768):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"--window-size={width},{height}")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    
    time.sleep(5)
    
    screenshot = driver.get_screenshot_as_png()
    driver.quit()
    
    return Image.open(BytesIO(screenshot))

def optimize_image(img, max_size=(1024, 768), quality=85):
    img.thumbnail(max_size)
    buffered = BytesIO()
    img.save(buffered, format="JPEG", quality=quality, optimize=True)
    return buffered.getvalue()

def encode_image(image_bytes):
    return base64.b64encode(image_bytes).decode('utf-8')

def analyze_image(encoded_image, element_type):
    try:
        message = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/jpeg",
                                "data": encoded_image,
                            },
                        },
                        {
                            "type": "text",
                            "text": f"""Analyze this screenshot and identify all {element_type} elements.If the content is appropriate for analysis, provide details about each element. If the content is not suitable for analysis, please provide a general, respectful explanation without specifics about the content. For each element, provide a detailed description including:

1. Precise position: Describe its location using pixel coordinates or percentages.
2. Size: Estimate its dimensions (width and height).
3. Visual characteristics: Describe its color, background, borders, shadows, etc.
4. Content: Any text, icons, or images contained within the element.
5. Surrounding context: Describe nearby elements and how this element relates to them.
6. Hierarchy: If it appears to be within another element, describe this relationship.
7. Interactivity hints: If it looks clickable, hoverable, or otherwise interactive.
8. Unique identifiers: Any visible ID, name, or aria-label that might be used for identification.
9. State: If the element appears to be in a specific state (e.g., active, disabled, selected).
10. Responsive behavior: If you can infer how it might change on different screen sizes.

Provide a clear, structured response. You may use JSON format if appropriate, but a well-organized text response is also acceptable."""
                        }
                    ],
                }
            ],
        )
        return {"success": True, "data": message.content[0].text}
    except Exception as e:
        return {"success": False, "error": str(e)}
        response_text = message.content[0].text
        if "apologize" in response_text.lower() and "not comfortable" in response_text.lower():
            return {
                "success": False,
                "content_warning": True,
                "message": "The AI has flagged the content as potentially sensitive or inappropriate for analysis. Please try a different website."
            }
        
        return {"success": True, "data": response_text}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            url = request.form.get('url')
            element_type = request.form.get('element_type')
            
            if not url:
                return jsonify({"success": False, "error": "No URL provided"})
            
            screenshot = capture_screenshot(url)
            optimized_image = optimize_image(screenshot)
            encoded_image = encode_image(optimized_image)
            
            results = analyze_image(encoded_image, element_type)
            return jsonify(results)
        except Exception as e:
            return jsonify({"success": False, "error": str(e)})
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)