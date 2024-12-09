# Chinese Tone Recognition

## Mandarin

## Cantonese
 - Not implemented yet
 - Similar analysis required as Mandarin, but with more attention to average frequency of each word
   - There are high and low pitch versions of each tone

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
   2. Enter command into CLI with the name of the subdirectory as the argument
```bash
python main.py <SubDirectoryName>
```