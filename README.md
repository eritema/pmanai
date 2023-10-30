# PManAI - Project Management AI Assistant

## Overview
PManAI is a standalone Python/Tkinter application designed to aid project managers by 
leveraging OpenAI's powerful language models. 
It can generate risk analyses, project summaries, schedules, scopes, and more from both documents and audio recordings.

## Features
- **Document Processing**. Import and process text documents for content generation.
- **Audio Input Support**. Transcribe and process audio recordings for content creation.
- **Content Generation**. Use OpenAI APIs to generate project-related content, including risk analyses, summaries, and more.
- **User-friendly Interface**. Simple and intuitive Tkinter-based GUI for easy operation.

## Installation Guide
PManAI is developed for Linux Ubuntu 20.04, utilizing Python and Tkinter, and requires OpenAI API Python bindings.

### Setting up on Ubuntu
Start by cloning the repository and setting up the required environment:

```bash
git clone https://github.com/eritema/pmanai
cd pmanai
conda create -n pmanai -f requirements.txt
```

Activate the environment and install the necessary OpenAI libraries (detailed guide [here](https://platform.openai.com/docs/libraries/python-library)):

```bash
conda activate pmanai
pip install openai
```

## How to Use
Figure 1 illustrates the primary workflow of PManAI ![Figure 1](/home/raf/workspace/github/openai-cookbook/apps/pmanai/docs/main_scenario.png). 

Run the application with `python main.py` within the project directory or update your PATH to include the repository workspace.

### Converting Audio to Text
From the Menu, select `File > Open Audio File`. Ensure the file size is under 25 MB (approximately an hour's recording). For a test run, choose `test.mp3` in the `example/` folder.

Click `Audio2Txt` and observe the following in your Terminal:

```plaintext
/path/to/pmanai/examples/test.mp3
Generating Transcription
```

A pop-up will notify you upon successful transcription, and the text will appear in the textbox for review and editing.

### Analyzing Text
After loading the text into the textbox, you can select one or multiple actions for analysis. Navigate to `File > Save as MD` and proceed to the `output/` folder to name your output file (e.g., `test`).

Press `Process Actions` and the terminal will display each executed action. A notification will inform you once the process is complete.

Your analysis, such as `test.md`, will be available in the selected output folder.

## Licensing
The licensing details for PManAI are currently under consideration.

## Connect with Us
For more information or queries, feel free to connect with me on [LinkedIn](linkedin.com/in/raffaele-fronza-17a85b5).



