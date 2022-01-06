# SNUBH_deid
De-identifying PHI in clinical notes from Dept.Raiology, SNUBH

## How to run

### Regular expression
**정규표현식만 적용하고 싶은 경우**

    python tagging.py
- `-i` `--input` input 노트 데이터 경로를 입력하여야 하며, 노트는 (1) note_id (2) note_text 두 개의 column이 존재하는 파일 형식이어야 합니다.
- `-o` `--output` 비식별화가 완료된 노트를 저장할 경로를 설정합니다.
- `-r` `--regex` 정규표현식 표현들이 들어있는 폴더 경로를 설정합니다.
- `-a` `--asterisk` 비식별 시, 해당 argument를 설정하면, 카테고리별로 표시하지 않고 한꺼번에 asterisk(*) 형식으로 지우게 됩니다. 
### Pseudo-labeling
**BERT나 KoBERT에 적용되는 형식으로 만들고 싶은 경우**

    python pseudo-labeling.py
- `-i` `--input` input 노트 데이터 경로를 입력하여야 하며, 노트는 (1) note_id (2) note_text 두 개의 column이 존재하는 파일 형식이어야 합니다.
- `-r` `--regex` 정규표현식 표현들이 들어있는 폴더 경로를 설정합니다.
- `-p` `--purpose` pseudo-labeling을 마친 노트가 어떤 목적으로 사용되는지 구별하기 위한 argument이며, 기본적으로 파일 이름 구별을 위해 아무 text나 적어도 되지만 `predict` 용도라면 label을 붙이지 않은 채 결과물을 return합니다.
- `-b` `--bert` 일반적인 BERT 형식으로 할 것인지, KoBERT 형식으로 할 것인지 설정합니다. Default는 `KoBERT`이며, `BERT` 를 따로 설정해주면 아래 예시와 같은 형태로 return하게 됩니다.
```buildoutcfg
if bert=='KoBERT':
    2016년 판독의 아무개 확인   'DAT-B' 'O' 'PER-B' 'O'

if bert=='BERT':
    2016년   'DAT-B'
    판독의 'O'
    아무개 'PER-B'
    확인  'O'
```
- output 노트의 경로는 따로 설정해주지 않아도 되며, `data/labeled_{purpose}_{bert}.txt` 형식으로 자동 저장됩니다.

## KoBERT-NER
- `model/*`
- `KoBERT-NER_file/*`

## `regex/*` 내 파일을 추가/수정/삭제하는 경우
###일반적인 정규표현식을 추가하는 경우
1.  기본적으로 regex/{Category} 항목으로 구성되어 있으며, {Category}를 기준으로 tagging 및 pseudo-labeling을 진행하므로 {Category} 내에 추가작업을 진행해야 합니다.
2. 알맞은 디렉토리에 적절한 정규표현식 txt 파일 추가 `regex/{Category}/__.txt`
3. `regex/transform_regex.txt`을 실행하여  `regex/{Category}/___transformed.txt` 파일이 추가될 수 있게 합니다.
4. class Pattern() / class Formula()를 수정해주어야 합니다.
    - {Category}를 완전히 추가한 경우, main() 함수에 반영되어야 합니다.
    
### Vocabulary를 추가하는 경우
- Vocabulary란 `regex/transform_regex` 내의 `month_name`이나 `hos_kor`처럼 설정해주는 형식을 말합니다. 
1. 새로운 변수를 추가하여 설정해준 후, `regex = regex.replace('"""+month_name+r"""', month_name)...` 열에 추가해 적용합니다.
2. `regex/{Category}/__.txt` 파일 내부에는 설정한 변수를 넣어주고, `regex/transform_regex.txt`을 실행합니다.
    - 참고 txt 파일 : `regex/hospitals/hospital_abb_kor.txt`과 그 transformed 파일.
3. class Pattern() / class Formula()를 수정해주어야 합니다.
    - {Category}를 완전히 추가한 경우, main() 함수에 반영되어야 합니다.
    
###파일을 수정하는 경우
- 파일의 이름만 바꾸지 않으면 정상적으로 작동합니다.
- 파일의 이름을 수정하는 경우,
  - class Pattern() / class Formula()를 수정해주어야 합니다.
    
### 파일을 삭제하는 경우
- `__transformed.txt` 파일이 없으면 인식되지 않습니다.
- main() / class Pattern() / class Formula()를 수정해주어야 합니다.

