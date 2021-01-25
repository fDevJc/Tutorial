'''
정규식
주민등록번호
900210-1111111

이메일 주소
asdb@fsdf.com

차량번호
11가 1234
123가 1234

ip주소
192.168.10.10

'''
import re
#알파벳 4개
# abcd .... zzzz
# ca?e

def print_match(m):
    if m:
        print("m.group() : ",m.group())     #일치하는 문자열 반환
        print("m.string : ",m.string)       #입력받은 문자열
        print("m.start() : ",m.start())     #일치하는 문자열의 시작 index
        print("m.end() : ",m.end())         #일치하는 문자열의 끝 index
        print("m.span : ",m.span())         #일치하는 문자열의 시작 / 끝 index
    else:
        print("no")
       
p = re.compile("ca.e")
#. ca.e : 하나의 문자를 의미 > care , cafe (O) / caffe (X)
#^ ^de  : 문자열의 시작 > desk , destination (O) / fade (X)
#$ se$  : 문자열의 끝 > case , base (O) / face (X)

#m = p.match("careless") #주어진 문자열의 처음부터 일치하는지 확인하는것이기떄문에 매치됨
#m = p.match("careless")
#print_match(m)
#print(m.group()) #매치되지않으면 에러
'''
if m:
    print(m.group())
else:
    print("no")
    


m = p.search("good care") #search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m)
'''

lst = p.findall("good care cafe") #findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)

'''
1.
p = re.compile("원하는 형태")
2.
m = p.match("비교할 문자열")
m = p.search("비교할 문자열")
lst = p.findall("비교할 문자열")

원하는 형태 : 정규식
#. ca.e : 하나의 문자를 의미 > care , cafe (O) / caffe (X)
#^ ^de  : 문자열의 시작 > desk , destination (O) / fade (X)
#$ se$  : 문자열의 끝 > case , base (O) / face (X)

#실습관련 사이트
w3school
lean python
regular expression에서 공부

python re
공식 파이썬 홈페이지에 있음

'''
