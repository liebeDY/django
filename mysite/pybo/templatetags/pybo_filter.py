import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg


@register.filter()
def mark(value):
    """
    mark 함수 : markdown 모듈과 mark_safe 함수를 이용하여 문자열을 HTML 코드로 변환하여 반환
    """
    extensions = ["nl2br", "fenced_code"]
    # "nl2br"은 줄바꿈 문자를 <br> 태그로 바꿔 주므로 <Enter>를 한 번만 눌러도 줄바꿈으로 인식
    # "fenced_code"는 마크다운의 소스 코드 표현을 위해 적용
    return mark_safe(markdown.markdown(value, extensions=extensions))