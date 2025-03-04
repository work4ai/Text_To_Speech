# gTTS (Google Text-to-Speech)

## Overview
[gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/) is a Python library that converts text into speech using Google's Text-to-Speech API. It provides an easy-to-use interface for generating speech from text in various languages and accents.

## Features
- Converts text into natural-sounding speech.
- Supports multiple languages and accents.
- Allows saving the speech as an audio file.
- Can be used for automation, accessibility, and voice-based applications.

## Installation
Install gTTS using pip:
```sh
pip install gtts
```

## Supported Languages
gTTS supports multiple languages, including:
- English (`en`)
- Spanish (`es`)
- French (`fr`)
- German (`de`)
- Hindi (`hi`)
- Many more (full list in gTTS documentation)

## Use Cases
- Voice assistants
- Accessibility tools for visually impaired users
- Automated voice notifications
- Language learning applications

## Additional Resources
- [Official Documentation](https://gtts.readthedocs.io/)
- [GitHub Repository](https://github.com/pndurette/gTTS)

# pyttsx3 - Text-to-Speech Conversion

## Overview
`pyttsx3` is a text-to-speech conversion library in Python that allows programs to read aloud text from a file or a string. Unlike other TTS libraries, `pyttsx3` works offline and supports multiple speech engines.

## Features
- Works offline (no internet required)
- Supports multiple speech engines (SAPI5, NSSpeechSynthesizer, espeak)
- Allows changing voice, rate, and volume
- Cross-platform support (Windows, macOS, Linux)

## Installation
Install `pyttsx3` using pip:
```sh
pip install pyttsx3
```

```

## Configuration
You can modify speech properties such as:
```python
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Select voice
```

## Use Cases
- Reading large text documents aloud
- Assisting visually impaired users
- Creating voice-enabled applications

# PyPDF2 - Read Text from PDF

## Overview
PyPDF2 is a Python library used for working with PDF files. It allows users to read, extract text, merge, split, and manipulate PDF documents. This project demonstrates using PyPDF2 to extract text from a PDF file and convert it into speech using a text-to-speech engine.

## Features
- Read and extract text from PDF files.
- Handle multiple pages and retrieve content programmatically.
- Supports text-to-speech integration with `pyttsx3`.

## Installation
Install PyPDF2 using pip:
```sh
pip install pypdf2
```

## Use Cases
- Automating PDF text extraction.
- Converting digital documents to speech.
- Processing large volumes of PDF files for text analysis.

## License
This project is licensed under the MIT License.

