# AERFAI-Contest-Multilingual-Handwritten-Text-Recognition 
This repository contains the script used for the task evaluation.

## Installation

With conda:

```
conda env create --file env.yml
conda activate mhtr
```

With pip:
```
pip install pybind11
pip install fastwer
```

## Example

```
python example.py
```
or
```
from eval import calculate_wer, calculate_cer
list_hyps = ['This is an example .', 'This is another example .']
list_refs = ['This is the example :)', 'That is the example .']
wer = calculate_wer(list_hyps, list_refs)
cer = calculate_cer(list_hyps, list_refs)
print("wer: ", wer)
# wer:  40.0
print("cer: ", cer)
# cer:  25.58
```
## Access to the data
Register by filling out the form: https://aerfai-contest-multilingual-htr-24.blogspot.com/p/register-form.html 

Once the form is submitted, you will receive an email with access to the data and the necessary password to download them.

## Contact

Daniel Parres - aerfai.contest.mhtr24@gmail.com

<p align="center">
  <img src="https://github.com/dparres/AERFAI-Contest-Multilingual-Handwritten-Text-Recognition/assets/114649578/4b6bfd22-3e5a-478e-878c-2a6487234b29" alt="Descripción de la primera imagen" width="35%" />
  <img src="https://github.com/dparres/AERFAI-Contest-Multilingual-Handwritten-Text-Recognition/assets/114649578/b4d80375-ec95-47d1-aeb8-7fc2b9abc90e" alt="Descripción de la segunda imagen" width="25%" />
</p>
