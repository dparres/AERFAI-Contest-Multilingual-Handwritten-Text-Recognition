# Tutorial

```pylaia-htr-create-model --config model_config_pylaia.yaml```

```pylaia-htr-train-ctc --config train_config_pylaia.yaml```

```python prepare_transcript.py labels_train.txt tr.txt```

```python make_symb.txt tr.txt```

```bash prepare_transcript_evaluation.sh decoded_ts.txt```
