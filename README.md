# Chinese Tone Recognition

# Description
This program is designed to analyze the tones of Chinese words through analysis of waveform audio. Changes in the fundamental frequency can be tracked over time to determine tone shape.

## Mandarin
 - 4 basic tones
   - flat, rising, falling-rising, falling
 - 1 neutral tone (not implemented)

## Cantonese
 - Debatable whether there are 6 or 9 tones
 - 6 tones for simplicity
   - falling 
   - low-rising, high-rising
   - high-flat, mid-neutral, low-neutral

# How to run
1. Activate the virtual environment
```bash
python -m venv venv
source venv/bin/activate
```
2. Install the required packages from root directory
```bash
pip install -r requirements.txt
```
3. Run the program
   1. Find the name of desired Recordings subdirectory of spliced phrases/sentences
      - Provided samples: mandonumbers, duibuqi, SampleArray (1 word for each tone)
   2. Enter command into CLI with the name of the subdirectory as the argument
```bash
python main.py <SubdirectoryName>
# e.g. python main.py mandonumbers OR python main.py duibuqi
```