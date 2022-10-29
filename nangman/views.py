from django.shortcuts import render
import configparser
import requests
import os


def index(request):
    return render(request, 'index.html')


def search(request, desc):
    # TODO: Request type 구분하기
    config = configparser.ConfigParser()
    # config.read(os.path.dirname(__file__)+'apigateway.ini', encoding='utf8')
    config.read('./apigateway.ini', encoding='utf8')
    apikey = config['AUTH']['api_key']
    # API 요청을 보내기
    response = requests.post(
        'https://8eif2hwsn6.execute-api.ap-northeast-2.amazonaws.com/nangman_stage/nangman', 
        headers={'X-API-Key':apikey},
        json={'desc':desc},
        )
    # 실패하면 다시 요청하기(3회)
    # Response 처리해서 Render하기
    pass


# 테스트용
def debug_search(request, desc):
    return render(
        request, 
        'search.html', 
        {'result':[
            {'idiom':'학수고대', 'definition':'애타게 기다리는 것'},
            {'idiom':'학수고대', 'definition':'애타게 기다리는 것'},
            {'idiom':'학수고대', 'definition':'애타게 기다리는 것'},
            {'idiom':'학수고대', 'definition':'애타게 기다리는 것'},
            ],})


def save_search_result(request):
    # DynamoDB에 검색한 내용이랑, 선택한 키워드를 세트로 저장하기 
    pass





'''
# AWS API gateway test code
import requests
resp = requests.post('https://8eif2hwsn6.execute-api.ap-northeast-2.amazonaws.com/nangman_stage/nangman', headers={'x-api-key':'7VEigUfKjQ9eHMf2wsOSw92W5WcKnC8u5IYdwyDe'}, json={'desc':'나는 끝까지 수행했다. [IDIOM]하다'})
print(resp)
print(resp.headers)
print(resp.json())
'''