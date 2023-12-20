# Tutorial

We recommend using the PyLaia toolkit (https://github.com/jpuigcerver/PyLaia). The following steps show how to install it.

```
conda create -n pylaia python=3.8
conda activate pylaia

git clone https://github.com/jpuigcerver/PyLaia
cd PyLaia
pip3 install -e .
```


Preparing the data for training, generating the validation partition using the training set, and creating symb.txt.

```
shuf labels_train.txt > aux.txt
head -n 18000 aux.txt > train.txt
tail -n 2000 aux.txt > valid.txt
python prepare_transcript.py train.txt tr.txt
python prepare_transcript.py valid.txt va.txt
rm -f aux.txt train.txt valid.txt
cut -f 1-1 -d “ “ tr.txt > tr.lst
cut -f 1-1 -d “ “ va.txt > va.lst
python make_symb.py <(cat tr.txt va.txt)
```


Model creation:
```
pylaia-htr-create-model --config model_config_pylaia.yaml
```


Model training:

```
pylaia-htr-train-ctc --config train_config_pylaia.yaml
```


Model inference:
```
pylaia-htr-decode-ctc --config decode_config.yaml > decoded_va.txt
```


Preparing data for evaluation:
```
bash prepare_transcript_evaluation.sh decoded_va.txt
```

Finally, to know the WER and CER metrics, you should use the "calculate_wer" and "calculate_cer" functions from "eval.py".


