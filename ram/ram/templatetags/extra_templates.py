from django import template
register = template.Library()


@register.filter
def gaps(var):
    # print("gaps: ",12-len(var))
    ans=12-len(var)-1
    if ans<0:
        ans=0
    return ans

@register.filter
def atindex(var,num):
    # print("index: ",num,var[num])
    return var[num]