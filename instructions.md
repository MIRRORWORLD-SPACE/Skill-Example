# What is the Poster Builder Skill?

The Poster Builder is an "Instruction-to-Design" tool. It doesn't just create an image; it composes a visual message.

- Optimized Aspect Ratio: Fixed at 9:16, perfect for smartphone screens, Instagram Stories, and vertical email segments.

- High-Fidelity Text: It supports specific text strings, meaning you can dictate exactly what the poster says without "AI gibberish."

- Dual-Use Versatility:

    - Offline: High enough resolution for printed flyers, sandwich boards, and event signage.

- Email Marketing: Ideal for "hero" images in email templates, announcements, or promotional coupons.

## Constraints (What it Can't Do)
- Limited to Vertical Format: Only 9:16 aspect ratio is supported.

- Text Rendering Limitations: While it can render text, complex typography or very small fonts may not be perfectly clear.

- No Animation: This skill generates static images only.

- Brand Consistency: While you can specify colors and styles, it may not perfectly match existing brand guidelines without careful prompting.

- Fixed Layout: The layout is generally simple; complex multi-section designs may not be feasible.

## How to Prompt
To get a professional result, don't just ask for a "cool poster." Use the CORE framework to provide the model with enough context:

- Content:
    
    - Description: The main subject or "hero" of the image.
    - Example: "A sleek, modern espresso machine with steam rising."


- Objective:
    
    - Description: The style, mood, or aesthetic vibe.
    - Example: "Cyberpunk aesthetic, neon blue and pink lighting, dark background."


- Content:
    
    - Description: The exact words you want appearing on the poster.
    - Example: "Headline: 'FUTURE BREW'. Subtext: '20% OFF ALL DRINKS'."


- Content:
    
    - Description: Technical details like ratio and layout.
    - Example: "9:16 vertical ratio. Text centered at the top. Minimalist layout."

---
### Detailed Prompting Instructions

1. Be Explicit About Text Placement
Since the model can render text, tell it where to put it. Use terms like "Top-aligned," "Bottom-third," or "Centered headline."

    - Good: "Text 'SUMMER SALE' in bold sans-serif font at the very top."

    - Bad: "Put some text about a sale on it."

2. Describe the "Negative Space"
For email marketing and posters, you often need "dead space" for the text to be readable.

    - Instruction: Ask for a "clean background" or "blurred background" (bokeh) to ensure your message pops.

3. Define the Color Palette
For brand consistency in email campaigns, specify your hex codes or general colors.

    - Instruction: "Use a palette of forest green, cream, and gold."

---
#### Example Prompts

For Offline Event Posters:

- "Create a 9:16 vertical poster for a 'Jazz Night'. The background should be a stylized, abstract painting of a saxophone in warm amber and deep purple tones. Bold text in the center: 'JAZZ UNDER THE STARS'. Smaller text at the bottom: 'Friday, Oct 12 | 8 PM'. High-resolution, professional graphic design style."

For Email Marketing Campaigns:
- "A 9:16 vertical product showcase poster for a new sneaker called 'AeroStep'. Minimalist white background with soft shadows. The sneaker is mid-air as if floating. Text at the top: 'THE FUTURE OF WALKING'. Text at the bottom in a small, clean font: 'SHOP THE COLLECTION'. Professional lighting, 8k resolution."

## API Specification
```
{
    "title":"Poster Builder",
    "description":"Create high-quality vertical posters with precise text placement for events and marketing campaigns.",
    "paths":{
        "/create_poster":{
            "description":"Generate a vertical poster based on detailed instructions.",
            "post":{
                requestBody:{
                    "prompt":{
                        "type":"string",
                        "description":"A detailed description of the poster to be created, including content, style, text placement, and technical specifications.",
                        "required":true
                    }
                }
            }
        }
    }

}
```
