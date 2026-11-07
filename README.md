
# Ollama Workshop

This repository is a small hands-on collection of Python examples for working with local large language models through Ollama. It demonstrates how to interact with Ollama using both the text-generation API and the chat API, and it includes a simple multimodal image-processing workflow for identifying birds from local images.

The goal is to make it easy to experiment with local AI models without sending data to a cloud service.

## What is included

- `chat.py` – a minimal interactive chatbot using the Ollama `/api/chat` endpoint
- `chatbot.py` – a simple conversational loop that keeps history in memory and sends it with each user message
- `generate.py` – a small example using the Ollama `/api/generate` endpoint for a single prompt
- `project.py` – a script that encodes an image to base64 and sends it to a multimodal model for image description
- `generate_multimodal.py` – loops through all JPG images in `birds/`, asks a vision-capable model to identify each bird, and writes results to `bird_descriptions.csv`
- `birds/` – sample bird images used in the experiments
- `bird_descriptions.csv` – example output file containing image filenames and corresponding bird names
- `Devops.md` – a general overview of DevOps concepts
- `notes.txt` – short notes about local LLMs and Ollama
- `Ollama_cli.txt` – a compact command reference for Ollama CLI usage
- `Using_the _Chat_API.txt` – notes explaining how the chat API works in practice

## Prerequisites

Before running the scripts, make sure Ollama is installed and running locally.

1. Install Ollama from the official documentation.
2. Start the local server:
   ```bash
   ollama serve
   ```
3. Pull a model you want to use, for example:
   ```bash
   ollama pull llama3.2
   ollama pull ornith-1.5:9b
   ```
4. Confirm the API is available:
   ```bash
   curl http://localhost:11434/api/tags
   ```

## Usage

Run the scripts from the repository root.

### Basic chat

```bash
python chat.py
```

### Chatbot with conversation memory

```bash
python chatbot.py
```

### Single text generation prompt

```bash
python generate.py
```

### Describe a single image

```bash
python project.py
```

### Identify multiple bird images and save results

```bash
python generate_multimodal.py
```

This will create or overwrite `bird_descriptions.csv` with rows like:

```csv
Filename,Bird
bird1.jpg,Blue-and-yellow Macaw
bird2.jpg,Common Kingfisher
```

## Notes

- These scripts assume Ollama is running on `http://localhost:11434`.
- Model availability depends on what you have downloaded locally.
- The examples are intended for learning and experimentation rather than production deployment.
- The bird-identification scripts use vision-capable models when available.

## License

This project is provided as an educational workshop example and is intended for local experimentation.
