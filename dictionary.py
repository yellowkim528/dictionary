import json

my_dict = {}
# 파일 변경시 아래 변수 변경해서 사용
save_file = "dictionary.json"
with open(save_file, mode='r', encoding='utf-8') as f:
  my_dict = json.load(f)


def menu():
  print("=" * 20)
  print("단어장임니다~")
  print("1 : 단어 저장")
  print("2 : 단어 검색")
  print("3 : 단어 수정")
  print("4 : 단어 삭제")
  print("5 : 단어 목록")
  print("6 : 단어 통계")
  print("0 : 단어장 종료!")
  print("=" * 20)


while True:
  menu()
  num = input()

  # 1. 단어 저장
  if num == '1':
    # 최대 5단어 제한
    if len(my_dict) == 5:
      print("최대 5개 단어만 저장할 수 있습니다.")
      continue
    print("추가할 단어를 입력하세요 : ")
    word = input().upper()
    # 중복 검사
    if word in my_dict.keys():
      print("이미 등록되었습니다")
      continue
    print("추가할 단어의 의미를 입력하세요 : ")
    mean = input()
    my_dict[word] = mean
    print("정상적으로 등록되었습니다.")
  # 2. 단어 검색
  elif num == '2':
    # null 검사
    if not my_dict:
      print("저장된 단어가 없습니다!")
      continue
    print("찾는 단어를 입력하세요 : ")
    word = input().upper()
    found_words = False
    # 입력한 글자로 시작하는 단어 검색
    for k in my_dict.keys():
      if k.upper().startswith(word):
        print("해당 단어가 존재합니다\n")
        print(f'{k} : {my_dict.get(k)}')
        found_words = True
    if not found_words:
      print("단어를 검색할 수 없습니다.")
  # 3. 단어 수정
  elif num == '3':
    # null 검사
    if not my_dict:
      print("저장된 단어가 없습니다!")
      continue
    print("수정할 단어를 입력하세요 : ")
    word = input().upper()
    if word in my_dict.keys():
      print("수정할 단어의 뜻을 입력하세요 : ")
      mean = input()
      my_dict[word] = mean
      print("단어의 뜻을 수정하였습니다.")
    else:
      print("단어를 검색할 수 없습니다.")
  # 4. 단어 삭제
  elif num == '4':
    # null 검사
    if not my_dict:
      print("저장된 단어가 없습니다!")
      continue
    print("삭제할 단어를 입력하세요. : ")
    word = input().upper()
    try:
      del my_dict[word]
      print("단어를 삭제하였습니다.")
    # 예외처리
    except:
      print("단어를 검색할 수 없습니다.")
  # 5. 단어 목록
  elif num == '5':
    # null 검사
    if not my_dict:
      print("저장된 단어가 없습니다!")
      continue
    print("정렬하시겠습니까?(y/n)")
    select = input()
    # 정렬 선택시
    if select.upper() == 'Y':
      print("1.오름차순 / 2. 내림차순")
      select_sort = input()
      # 1.오름차순
      if select_sort == '1':
        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[0], reverse=False))
        for k, v in sorted_dict.items():
          print(f'{k} : {v}')
      # 2.내림차순
      elif select_sort == '2':
        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[0], reverse=True))
        for k, v in sorted_dict.items():
          print(f'{k} : {v}')
      else:
        print("잘못입력하셨습니다.")
        continue
    # 정렬선택 X. 있는 그대로 출력
    elif select.upper() == 'N':
      for k, v in my_dict.items():
        print(f'{k} : {v}')
  # 6. 단어 통계
  elif num == '6':
    # null 검사
    if not my_dict:
      print("저장된 단어가 없습니다!")
      continue
    # 단어 갯수 출력
    print(f"저장된 단어 갯수 : {len(my_dict)}개")
    # 가장 긴 단어 출력
    longest_word = max(my_dict.keys(), key=lambda word: len(word))
    print(f"단어의 문자수가 가장 많은 단어 : {longest_word}")
    # 단어 길이 내림차순으로 출력
    sorted_words = sorted(my_dict.keys(), key=lambda word: len(word), reverse=True)
    print("단어 목록 : ")
    for word in sorted_words:
      print(word)
  # 0. 프로그램 종료
  elif num == '0':
    print("단어장을 종료합니다!")
    # 딕셔너리를 json 파일에 저장
    with open(save_file, 'w', encoding='utf-8') as my_file:
      json.dump(my_dict, my_file, ensure_ascii=False, indent=4)
    break
  else:
    print("번호를 잘못 입력하셨습니다.(0~6 사이의 번호를 입력해주세요)")
