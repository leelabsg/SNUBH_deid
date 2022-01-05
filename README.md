# SNUBH_deid
De-identifying PHI in clinical notes from Dept.Raiology, SNUBH

## How to run
하나의 노트를 input하면 KoBERT-NER에 돌릴 수 있는 형식으로 output
(코드파일 하나 추가)


### Step by step
#### Regular expression
`python tagging.py`
- `-i` `--input` input 노트 데이터. (1) note_id (2) note_text 두 개의 column이 존재하는 파일 형식으로 설정되어 있다.
- `-o` `--output` 비식별화가 완료된 노트를 저장할 경로.
- `-r` `--regex` 정규표현식 표현들이 들어있는 폴더 경로.
- `-a` `--asterisk` 비식별 시, 해당 argument를 설정하면 asterisk(*) 형식으로 지운다.
### Pseudo-labeling
pseudo-labeling
- input data 형식/경로
- output data 형식/경로
- regex 내 파일을 추가/수정/삭제하는 경우

### KoBERT-NER
모델 파일 경로
- KOBERT-NER을 받은 뒤 어떻게 사용하는지