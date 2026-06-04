# KoreanLearning

A simple Streamlit app for practicing Korean vocabulary with audio playback.

## Features

- Vocabulary review for Korean words with Vietnamese translations
- Audio pronunciation for each word loaded from local MP3 files
- Responsive table layout using custom HTML styling

## Requirements

- Python 3.8+
- Streamlit

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Run the app

```bash
streamlit run korean.py
```

## Project structure

- `korean.py` - main Streamlit application
- `requirements.txt` - Python dependencies
- `Files/` - local audio files used by the app

## Notes

The app embeds audio files as base64 data URIs so pronunciation can be played directly inside the browser.
