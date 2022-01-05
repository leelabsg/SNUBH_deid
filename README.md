# SNUBH_deid
De-identifying PHI in clinical notes from Dept.Raiology, SNUBH

# How to run
## Overall
하나의 노트를 input하면 KoBERT-NER에 돌릴 수 있는 형식으로 output
(코드파일 하나 추가)


## Separately
### Regular expression
tagging.py
- 필요 파일(regex/)
- input data 형식/경로
- output data 형식/경로
### Pseudo-labeling
pseudo-labeling
- input data 형식/경로
- output data 형식/경로
- regex 내 파일을 추가/수정/삭제하는 경우

### KoBERT-NER
모델 파일 경로
- KOBERT-NER을 받은 뒤 어떻게 사용하는지