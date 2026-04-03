#현재 경로 확인 방법 


import os  # <--- 이 줄을 꼭 추가해야 합니다!
import pandas as pd
from step_1 import IN_DIR # 여기에 파일명 넣고


# 1. 현재 주피터 노트북이 돌아가는 위치 확인
print(f"현재 위치: {os.getcwd()}")

# 2. step_1에서 가져온 경로가 실제로 존재하는지 확인
print(f"설정된 경로: {IN_DIR}")
print(f"경로 존재 여부: {os.path.exists(IN_DIR)}")

# 3. 그 폴더 안에 파일들이 뭐가 있는지 확인
if os.path.exists(IN_DIR):
    print(f"폴더 안의 파일들: {os.listdir(IN_DIR)}")

    #이걸로 펄스 뜨거나 실제 주소랑 안맞으면 경로지정 잘못된거거