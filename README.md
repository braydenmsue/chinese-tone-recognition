# Chinese Tone Recognition

![alt text](https://github.com/braydenmsue/chinese-tone-recognition/blob/main/figures/qi3.png?raw=true)
# Description
This program is designed to analyze the tones of Chinese words through analysis of waveform audio. Changes in the fundamental frequency (f0) are tracked over time to determine tone shape.

## Mandarin
 - 4 basic tones
   - flat, rising, falling-rising, falling
 - 1 neutral tone
 - Mandarin numbers with tones:\
![alt text](https://github.com/braydenmsue/chinese-tone-recognition/blob/main/figures/mand_num_chart.PNG?raw=true)

## Cantonese [Not Implemented]
 - 6 tones for simplicity (instead of 9)
   - falling 
   - low-rising, high-rising
   - high-flat, mid-neutral, low-neutral
 - Cantonese numbers with tones:\
 ![alt text](https://github.com/braydenmsue/chinese-tone-recognition/blob/main/figures/cant_num_chart.PNG?raw=true)

### To Be Implemented
 - Word block analysis
   - Average f0 for particular speaker
   - Mandarin neutral tone
 - Word block waveform audio segmentation
 - Recording user input
    - Overlay of user input f0 and correct tone
 - Cantonese

# How to Run
1. Clone the repository
```bash
https://github.com/braydenmsue/chinese-tone-recognition.git
````
2. Navigate to root directory and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate
```
3. Install the required packages
```bash
pip install -r requirements.txt
```
4. Run the program
   1. Find the name of desired Recordings subdirectory of spliced phrases/sentences
      - Provided samples:
        - Recordings/**mandonumbers**: mandarin numbers (1 - 10)
        - Recordings/**duibuqi**: 3 words, two tones (dui4 bu4 qi3) 
        - Recordings/**SampleArray**: 1 number word for each tone (er4, shi2, wu3, yi1)
   2. Enter command into CLI with the name of the subdirectory as the argument
```bash
python main.py <SubdirectoryName>
# e.g. python main.py mandonumbers OR python main.py duibuqi
```