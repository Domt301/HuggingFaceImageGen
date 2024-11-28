# Hugging Face Image Generator

This Python program generates images based on text prompts using the Hugging Face API. It securely reads your Hugging Face API token from an `.env` file, takes a user input prompt, generates an image, and saves it to your current working directory.

![Hugging Face Logo](https://huggingface.co/front/assets/huggingface_logo.svg)

---

## Features

- **Text-to-Image Generation**: Create images using the Hugging Face `black-forest-labs/FLUX.1-dev` model.
- **Secure Token Handling**: API tokens are securely managed using a `.env` file.
- **Interactive Prompt**: Enter custom text prompts to generate unique images.
- **Automatic File Naming**: Images are saved with sanitized filenames derived from the prompt.

---

## Installation

### Prerequisites

Ensure Python 3.7 or later is installed on your system.

### Setup Instructions

1. Clone the repository or copy the project files to your working directory.

2. Install the required Python packages:
   ```bash
   pip install huggingface_hub pillow python-dotenv
   ```

3. Create a `.env` file in your project directory with your Hugging Face token:
   ```plaintext
   HUGGINGFACE_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

---

## Usage

1. Run the Python script:
   ```bash
   python generate_image.py
   ```

2. Enter a text prompt when prompted, for example:
   ```
   Enter a prompt to generate an image: Astronaut riding a horse
   ```

3. The generated image will be saved in your working directory with a filename based on your prompt, such as `Astronaut_riding_a_horse.png`.

---

## File Structure

Here’s the file structure for the project:

```
huggingface_image_generator/
│
├── .env                # Stores your Hugging Face API token
├── generate_image.py   # Main Python script for image generation
├── README.md           # Project documentation
└── requirements.txt    # List of required Python packages (optional)
```

---

## Example Output

After running the program with the prompt `Astronaut riding a horse`, you will see:

- A generated image saved in your directory.
- The console will display:
  ```
  Generating image for prompt: Astronaut riding a horse
  Image saved as: Astronaut_riding_a_horse.png
  ```

---

## Dependencies

This project requires the following Python packages:

- `huggingface_hub`: For accessing the Hugging Face API.
- `pillow`: For working with and saving images.
- `python-dotenv`: For securely loading environment variables.

You can install these dependencies using `pip`:
```bash
pip install huggingface_hub pillow python-dotenv
```

---

## Notes

- Ensure you have a valid Hugging Face API token in the `.env` file.
- You can find more models on [Hugging Face](https://huggingface.co/models) for different image-generation tasks.
- Images are saved in `.png` format in the current working directory.

---


![Hugging Face Logo](https://huggingface.co/front/assets/huggingface_logo.svg)

---

## License

This project is open source and free to use under the [MIT License](LICENSE).
