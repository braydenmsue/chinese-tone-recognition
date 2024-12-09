# Chinese Tone Recognition

![alt text](https://github.com/braydenmsue/chinese-tone-recognition/blob/main/figures/qi3.png?raw=true)
# Description
This program is designed to analyze the tones of Chinese words through analysis of waveform audio. Changes in the fundamental frequency are tracked over time to determine tone shape.

## Mandarin
 - 4 basic tones
   - flat, rising, falling-rising, falling
 - 1 neutral tone (not implemented yet)
![alt text](https://github.com/braydenmsue/chinese-tone-recognition/blob/main/figures/mand_num_chart.PNG?raw=true)

## Cantonese
 - 6 tones for simplicity (instead of 9)
   - falling 
   - low-rising, high-rising
   - high-flat, mid-neutral, low-neutral
 ![alt text](https://github.com/braydenmsue/chinese-tone-recognition/blob/main/figures/cant_num_chart.PNG?raw=true)

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
      - Provided samples:
        - Recordings/**mandonumbers**: mandarin numbers (1 - 10)
        - Recordings/**duibuqi**: 3 words, two tones (dui4 bu4 qi3) 
        - Recordings/**SampleArray**: 1 number word for each tone (er4, shi2, wu3, yi1)
   2. Enter command into CLI with the name of the subdirectory as the argument
```bash
python main.py <SubdirectoryName>
# e.g. python main.py mandonumbers OR python main.py duibuqi
```