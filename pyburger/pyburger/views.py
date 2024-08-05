from django.http import HttpResponse
from django.shortcuts import render

from burgers.models import Burger
from lunchmenu.models import LunchMenu


# views - controller 역할.

# 터미널에서, 단위 테스트 연습해보기.
# python
# 입력 후, 모양이 >>>
# from burgers.models import Burger
# 오류 발생하면,
# 다시 터미널에서, ctrl + z
# python manage.py shell
# from burgers.models import Burger
# Burger

# 해당 모델 객체의 목록 모두 가져오기.
# Burger.objects.all()

# 하나 가져오기
# Burger.objects.get(name="불고기버거")
# 임시 변수에 담아서, 객체 형식으로 확인.
# burger = Burger.objects.get(name="불고기버거")
# 객체의 각 필드요소를 조회.
# burger.id
# burger.name
# burger.price
# burger.calories

# 조건으로 , 모델에서, 해당 객체 조회. 끝나는 이름으로 조회.
# burgers = Burger.objects.filter(name__endswith="버거")
# type(burgers)
# <class 'django.db.models.query.QuerySet'>

# len(burgers)
# 3
# >>> burgers[1]
# <Burger: 불고기버거>

# 반복문으로, 목록 요소의 내용 조회하기.
# for burger in burgers:
#     print(burger.id, burger.name, burger.price, burger.calories)





def main(request):
    # 단순 문자열만 리턴,
    # return HttpResponse("Hello, world.")
    # 화면을 연결해서 응답하기.
    return render(request, 'main.html')


def main2(request):
    # return HttpResponse("오늘 점심 뭐 먹지? 듣고 있나요? 듣고만 있나요? ")
    return render(request, 'main2.html')


def burger_list(request):
    # 디비로부터 데이터 가져오기.
    burgers = Burger.objects.all()
    # 1차 확인, 콘솔 확인
    # print(f"전체 햄버거 목록: {burgers}")
    # 데이터를 화면에 전달시, 각각 전달 가능하지만, 하나의 객체에 모두 담아서 보내기
    context = {'burgers': burgers}
    # 화면에 그려주면서, 동시에 데이터도 같이 전달.
    # 주의사항,
    # 화면에서, 타임리프 기억나요? , 해당 데이터 가져올 때,
    # 변수 사용시 기본 문법
    # {{변수명 }} ,
    # 태그 사용시,
    # {% 시작     %}  끝나는 태그
    return render(request, 'burger_list.html',context)

def lunch_list(request):
    # 디비로부터 데이터 가져오기.
    lunchMenuList = LunchMenu.objects.all()
    # 1차 확인, 콘솔 확인
    # print(f"전체 햄버거 목록: {burgers}")
    # 데이터를 화면에 전달시, 각각 전달 가능하지만, 하나의 객체에 모두 담아서 보내기
    context = {'lunchMenuList': lunchMenuList}
    # 화면에 그려주면서, 동시에 데이터도 같이 전달.
    # 주의사항,
    # 화면에서, 타임리프 기억나요? , 해당 데이터 가져올 때,
    # 변수 사용시 기본 문법
    # {{변수명 }} ,
    # 태그 사용시,
    # {% 시작     %}  끝나는 태그
    return render(request, 'lunchmenu_list.html',context)

#버거 검색 기능
# 검색 폼
def burger_search(request):
    # 화면, 웹브라우저에서, 전달 받은 검색 키워드를
    print(request.GET)
    # 꺼내서, 키워드만 추출
    keyword = request.GET.get("keyword")
    print(keyword)

    # 키워드가 있다면
    if keyword is not None:
        # 해당 키워드로 , 디비에서 조회
        burgers = Burger.objects.filter(name__contains=keyword)
        print(f"검색된 burgers: {burgers}")
    else:
        burgers = Burger.objects.none()

    context = {'burgers': burgers}
    return render(request,"burger_search.html",context)
