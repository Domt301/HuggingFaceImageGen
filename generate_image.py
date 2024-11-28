import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get the token from the environment variables
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

if not HUGGINGFACE_TOKEN:
    raise ValueError("Hugging Face token is missing! Make sure it's set in the .env file.")

# Initialize the Hugging Face Inference Client
client = InferenceClient("black-forest-labs/FLUX.1-dev", token=HUGGINGFACE_TOKEN)

def generate_image(prompt):
    """Generate an image based on a prompt and save it."""
    print(f"Generating image for prompt: {prompt}")
    try:
        # Generate the image
        image = client.text_to_image(prompt)

        # Save the image to the current working directory
        output_path = f"{prompt.replace(' ', '_')[:50]}.png"  # Sanitize file name
        image.save(output_path)

        print(f"Image saved as: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get user input for the prompt
    user_prompt = input("Enter a prompt to generate an image: ")
    if user_prompt.strip():
        generate_image(user_prompt)
    else:
        print("Prompt cannot be empty!")
