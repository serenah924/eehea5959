#!/usr/bin/env python
# coding: utf-8

# ## CH 10. 입출력

# ### 10-01. 입출력의 개요

# - SSD(HDD) 사용하는 방법
# - RAM > SSD(HDD), SSD(HDD) > RAM
# - RAM > binary(byte():직렬화) > SSD(HDD)
# - pickle

# ### 10-02. 텍스트 데이터 파일로 저장 및 읽어오기

# In[1]:


# 디렉토리 만들기
import os
os.mkdir('file')


# In[2]:


# 텍스트 파일 쓰기 : write 함수 사용
data = '''datascicence
jupyter notebook write
fighting!!'''
file = open("file/test1.txt", 'wt')
file.write(data)
file.close()


# In[3]:


# 텍스트 파일 쓰기 : print 함수 사용
data = '''ipython notebook
jupyter lab'''
file = open('file/test2.txt', 'wt')
print(data, file=file)
file.close()


# In[4]:


# 텍스트 파일 쓰기 : with 사용
# with를 사용하면 close를 하지 않아도 된다.
data = 'test3 text!!!'
with open("file/test3.txt", 'wt') as file: 
    file.write(data)


# In[5]:


get_ipython().run_line_magic('ls', 'file')


# In[6]:


# 텍스트 파일 읽기
file = open("file/test1.txt", 'rt')
data = file.read()
file.close()
print(data)


# In[7]:


# 텍스트 파일 읽기 : with 사용
with open('file/test3.txt', 'rt') as file:
    data = file.read()
data


# ### 10-03. pickle을 이용하여 객체를 파일로 저장 및 읽어오기

# In[8]:


class Text:
    def __init__(self, data):
        self.data = data


# In[9]:


txt = Text('py')
txt.data


# In[10]:


# RAM(txt) > SSD(txt)
# wb : write binary
import pickle

with open('txt.pkl', 'wb') as file:
    pickle.dump(txt, file)


# In[11]:


get_ipython().run_line_magic('ls', '| grep txt.pkl')


# In[12]:


# SSD(txt) > RAM(txt)
with open('txt.pkl', 'rb') as file:
    load_txt = pickle.load(file)


# In[13]:


load_txt.data


# ### 10-04. 파일시스템을 다루는 OS 패키지
# - 파이썬 코드로 파일시스템을 다루는 패키지
# - 디렉토리 만들기, 파일 복사하기, 파일 삭제하기 등의 기능 사용

# In[14]:


import os


# In[15]:


# 디렉토리 만들기


# In[16]:


get_ipython().run_line_magic('ls', '')


# In[17]:


os.makedirs('os')


# In[18]:


get_ipython().run_line_magic('ls', '')


# In[19]:


get_ipython().run_line_magic('ls', 'os')


# In[20]:


# 파일생성
data = 'python data1'
with open('os/data1.txt', 'wt') as file:
    file.write(data)


# In[21]:


data = 'python data2'
with open('os/data2.txt', 'wt') as file:
    file.write(data)


# In[22]:


data = 'python,data3'
with open('os/data3.csv', 'wt') as file:
    file.write(data)


# In[23]:


get_ipython().run_line_magic('ls', 'os')


# In[24]:


# 파일목록 읽어오기
filenames = os.listdir('os')
filenames


# In[25]:


txt_filenames = [
    filename 
    for filename in filenames 
    if filename.split('.')[-1] == 'txt'
]
txt_filenames


# In[26]:


data = 'data1.txt'
data.split('.')[-1]


# In[27]:


# 파일삭제
os.remove('os/data3.csv')


# In[28]:


get_ipython().run_line_magic('ls', 'os')


# In[29]:


# 디렉토리삭제
# os.removedirs('os')


# In[30]:


# shutil
import shutil


# In[31]:


shutil.rmtree('os')


# In[32]:


get_ipython().run_line_magic('ls', '')


# In[33]:


# 파일복사하기


# In[34]:


os.makedirs('file1')
os.makedirs('file2')


# In[35]:


get_ipython().run_line_magic('ls', '')


# In[36]:


with open('file1/data1.txt', 'wt') as file:
    file.write('data1')


# In[37]:


get_ipython().run_line_magic('ls', 'file1')


# In[38]:


get_ipython().run_line_magic('ls', 'file2')


# In[39]:


src = 'file1/data1.txt'
dst = 'file2/data1.txt'
shutil.copy(src, dst)


# In[40]:


get_ipython().run_line_magic('ls', 'file2')


# In[41]:


# 파일이동하기 (파일이름 바꾸기)
os.rename('file2/data1.txt', 'file2/data2.txt')


# In[42]:


get_ipython().run_line_magic('ls', 'file2')


# In[ ]:





# ## CH 11. 예외처리

# ### 11-01. 예외처리의 개요와 명령어 사용

# - 코드 실행중 에러가 발생한 경우 에러를 처리하는 문법
# - try, except, finally, raise 

# In[43]:


try:
    print('connect.')
    print(1/1)
    # print('disconnect.')
except Exception as e:
    print(e)
    # print('disconnect.')
finally: # 코드 에러에 관계없이 항상 실행
    print('disconnect.')
print('kyobo')


# ### 11-02. 예외처리를 만드는 방법

# In[44]:


# raise : 강제에러발생
class LowNumber(Exception):
    def __str__(self):
        return 'Insert number greater than 10.'


# In[45]:


def input_number(number):
    if number <= 10:
        raise LowNumber()
    print(number)


# In[46]:


input_number(7)


# ### 11-03. 클래스와 예외처리를 활용한 객체생성 문제
# - 문제. 아래의 조건에 해당하는 에러를 생성하여 에러가 발생할수 있는 echo 함수를 코드로 작성하세요.
#     - NotNumber 에러 생성 : 에러메세지는 insert int or float datatype.
#     - echo 함수에서 number 파라미터를 받는데 데이터타입이 int, float이 아니면 NotNumber 에러 발생

# In[47]:


# CODE


# ## CH 12. 정규표현식

# ### 12-01. 정규표현식 개요 및 함수 사용법

# - 문자열을 처리할때 특정 패턴으로 문자열을 처리하는 방법
# - 정규표현식 함수
#     - findall : 일치하는 패턴을 모두 찾기
#     - sub : 특정 패턴에 맞는 문자열을 대체 하기

# In[50]:


import re
data = "fast campus datascience fighting. datascience fighting. fast campus fighting."


# In[51]:


# 일치하는 패턴을 모두 찾습니다.
result1 = re.findall("fast", data) # (패턴, 문자열)
result2 = re.findall("campus", data) # (패턴, 문자열)
print(result1)
print(result2)


# In[52]:


# 일치하는 패턴을 대체
print(data)
# ("패턴", "해당되는 패턴을 바꿀문자열", 전체 문자열)
re.sub("fast", "slow", data) 


# ### 12-02. 정규표현식의 문자 패턴 

# ### 3. 패턴 - pattern
# - 문자
#     - 숫자인지 문자인지 특수문자인지등을 구분
#     - `\d` : 숫자
#     - `\D` : 비숫자
#     - `\w` : 숫자, 문자, _
#     - `\W` : 숫자, 문자, _ 제외
#     - `\s` : 공백문자
#     - `\S` : 비공백문자

# In[53]:


import string
pt = string.printable
len(pt), pt


# In[54]:


# \d, \D - 숫자와 비숫자를 찾는 패턴
result = re.findall("\d", pt)
# result = re.findall("[0-9]", pt)
''.join(result)


# In[55]:


result = re.findall("\D", pt)
''.join(result)


# In[56]:


# 문자
result = re.findall("\w", pt)
print(''.join(result))
result = re.findall("\W", pt)
''.join(result)


# In[57]:


# 공백문자
result = re.findall("\S", pt)
print(''.join(result))
result = re.findall("\s", pt)
''.join(result)


# ### 12-03. 정규표현식의 지정자 패턴 

# - 범위가 몇회 반복과 같은 패턴을 구분
# - `[]`: 문자
# - `-` : 범위
# - `.` : 하나의 문자
# - `?` : 0회 또는 1회 반복
# - `*` : 0회 이상 반복
# - `+` : 1회 이상 반복
# - `{m,n}` : m~n회 반복
# - `()` : 그룹핑

# In[58]:


# [] : 문자
re.findall("[abc1]", pt)


# In[59]:


# - : 범위
re.findall("[01234567]", pt)


# In[60]:


re.findall("[0-7]", pt)


# In[61]:


re.findall("[a-f]", pt)


# In[62]:


re.findall("[a-fA-F]", pt)


# In[63]:


# . : 문자하나
ls = ["123aab123", "a0b", "abc"]
for s in ls:
    result = re.findall("a.b", s)
    print(s, result)


# In[64]:


# ? : ? 앞에 있는 패턴을 0회 또는 1회 반복
ls = ["aab", "a3b", "abc", "accb"]
for s in ls:
    # a + 어떤문자0개 또는 1개 + b
    result = re.findall("a.?b", s) 
    print(s, result)


# In[65]:


# * : 0회이상 반복
ls = ["ac", "abc", "abbbbc", "a3bec"]
for s in ls:
    # a + b가 0회 이상 반복 + c
    result = re.findall("ab*c", s) 
    print(s, result)


# In[66]:


# + : 1회이상 반복
ls = ["ac", "abc", "abbbbc", "a3bec"]
for s in ls:
    # a + b가 1회 이상 반복 + c
    result = re.findall("ab+c", s) 
    print(s, result)


# In[67]:


# {m} m회 반복
# {m, n} m에서 n회 반복
# + : 1회이상 반복
ls = ["ac", "abc", "abbbbbc", "abbbbbbbbbbc"] # 5회, 10회
for s in ls:
    # a + b가 m회 ~ n회 반복 + c
    result = re.findall("ab{1,8}c", s) 
    print(s, result)


# In[68]:


# () : 그룹핑
ls = ["aaa5.djfi","abdddc5","1abbbbc","a3.bec"]
for s in ls:
    # 그룹1(0~9의 숫자가 1회이상반복) + [.문자] + 그룹2(a ~ z가 2글자)
    result = re.findall("([0-9]+)[.]([a-z]{2})", s) 
    print(s, result)


# ### 12-04. 정규표현식으로 문장에서 패턴으로 데이터를 출력하는 문제
# - 문제. 아래의 문자열에서 이메일 주소를 리스트로 출력하세요.

# In[69]:


data = "저의 이메일 주소는 pdj1224@gmail.com 입니다. 또한 radajin1224@gmail.com 도 가지고 있습니다."


# In[70]:


# CODE


# ### 12-05. 정규표현식으로 문장에서 패턴으로 문자열을 변경하는 문제

# - 문제. 주민등록번호를 group 나눠서 변경하는 코드를 작성하세요.
# - 761211-1023334 -> 761211-*******
# - () 그룹핑을 사용 : 그룹핑의 데이터 사용은 \g<1> 으로 사용

# In[ ]:


data = "저의 주민등록번호는 761231-1098913 과 7612111098013 입니다."


# In[71]:


# CODE


# ### 12-06. 정규표현식을 사용하여 숫자,영문,한글로 작성된 전화번호를 숫자로 변경하는 문제

# In[72]:


data = "안녕하세요, 저의 전화번호는 영일공-48구삼삼7이사 그리고 010사팔구삼삼구삼일 입니다. 둘중에 하나로 연락하세요"


# In[73]:


# CODE


# ## CH 13. 파이썬 문법 정리

# ### 13-01. 파이썬 문법 요약정리 1

# #### 컴퓨터구조, 프로그램 동작원리
#     - CPU, RAM, SSD(HDD) > control OS > Application(python)
#     - 프로그래밍 언어 종류 2가지
#         - 컴파일러 언어 : 빌드과정 후 코드실행 : 속도빠름, 빌드시간 기다림
#         - 인터프리터 언어 : 빌드하면서 코드실행 : 속도느림, 바로 코드 실행, 문법 쉬움 : python

# #### 파이썬 문법
# 1. 변수선언 : RAM 저장공간 사용문법
#     - 식별자 : 저장공간을 구별하는 문자열
#     - 식별자규칙 : 문법, 컨벤션(PEP8)
#     - 변수선언 3가지 방법
# 2. 데이터타입 : RAM 저장공간 효율적 사용문법
#     - 기본 : int, float, bool, str : 동적타이핑
#     - 컬렉션 : list, tuple, dict, set
#         - create : \[ \], ( ), {key:value}, set()
#         - read : masking : \[idx\], \[key\], \[start:end\], \[start:end:stride\]
#         - update : select data = modify data
#         - delete : del select data
#     - 변수 속성값 출력 : print(), type(), id()
# 3. 연산자 : CPU 사용문법
#     - 산술, 비교, 논리, 할당, 멤버

# 4. 조건문 : 코드 효율적 작성 실행 문법
#     - 특정 조건에 따라서 코드 실행
#     - if, elif, else
# 5. 반복문
#     - 특정 코드를 반복적으로 실행
#     - while, for, break, continue, range(), enumerate(), zip()
# 6. 함수
#     - 중복되는 코드를 묶어서 코드 작성 실행
#     - 사용법 : 함수선언(코드작성) > 함수호출(코드실행)
#     - def, args-params, return, docstring(help()), \*,\*\*, scope(global), lambda, decorator
# 7. 클래스
#     - 변수, 함수 묶어서 코드 작성 실행
#     - 객체지향 : 실제 세계를 모델링하여 코드 작성 실행
#     - 사용법 : 클래스선언(코드작성) > 객체생성(메모리사용) > 메서드실행(코드실행)
#     - class, self, \_\_init\_\_(), \_\_add\_\_(), 상속, is a, has a, methods(instance, class, static)

# ### 13-02. 파이썬 문법 요약정리 2

# 8. 모듈, 패키지
#     - 모듈 : 변수, 함수, 클래스를 하나의 파일(.py)로 묶어서 코드 작성 실행
#     - 패키지 : 여러개의 모듈을 디렉토리로 구별하여 코드 작성 실행
#     - import, from, as
# 9. 입출력 : SSD(HDD) 사용문법
#     - RAM > SSD, SSD > RAM
#     - pickle
# 10. 예외처리
#     - 에러를 처리하는 방법, 에러를 발생시키는 방법
#     - try, except, finally, raise
# 11. 정규표현식
#     - 특정 패턴으로 문자열을 처리하는 문법
#     - re : findall(), sub() : 문자, 지정자

# ## CH 14. 파이썬 데이터분석 미리보기
# ### 14-01 Numpy 미리보기
# - python 에서 사용하는 과학계산용 패키지
# - c, c++, fortran(컴파일러언어) 으로 만들어져 연산속도가 빠름
# - ndarray 데이터타입 사용

# In[1]:


# 모듈, 패키지 사용
import numpy as np


# In[2]:


# 객체 생성
data = np.array([[1, 2, 3], [4, 5, 6]])
data


# In[3]:


# 데이터타입, 클래스 : ndarray
type(data)


# In[8]:


# 객체 변수, 메서드 출력
dir(data)[-12:]


# In[9]:


# 메서드 docstring 출력
help(data.sum)


# In[10]:


# 메서드 사용
data.sum(axis=1)


# ### 14-02 Pandas 미리보기
# - 데이터분석을 위한 사용이 쉽고 성능이 좋은 오픈소스 파이썬 라이브러리
# - Series, DataFrame

# In[11]:


import numpy as np
import pandas as pd


# In[12]:


data = np.random.randint(60, 100, size=(3, 4))
data


# In[13]:


type(data)


# In[14]:


# 생성자 메서드 사용하여 객체 생성
df = pd.DataFrame(data, columns=['국어', '수학', '영어', '코딩'])
df


# In[15]:


# 데이터타입, 클래스 출력
type(df)


# In[24]:


# 객체 변수, 메서드 출력
dir(df)[-8:]


# In[26]:


# 메서드 docstring 출력
help(df.min)


# In[27]:


df.min(1)

