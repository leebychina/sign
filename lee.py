from bs4 import BeautifulSoup
import requests
il = requests.get('https://github.com/login')
soup1 = BeautifulSoup(il.text,features='html.parser')
tag = soup1.find(name='input',attrs={'name':'authenticity_token'})
authenticity_token = tag.get('value')
c1=il.cookies.get_dict()
il.close()
form_data = {
    'authenticity_token':authenticity_token,
    'utf8':'',
    'commit':'Sign in',
    'login':"178735917@qq.com",
    'password':"13251106325fang"
}
i2 = requests.post('https://github.com/session',data=form_data,cookies=c1)
c2 = i2.cookies.get_dict()
c1.update(c2)
i3 = requests.get('https://github.com/settings/repositories',cookies=c1)
soup3 = BeautifulSoup(i3.text,features='html.parser')
list_group = soup3.find(name='div',class_='listgroup')
from bs4.element import Tag
for child in list_group.children:
    if isinstance(child,Tag):
        project_tag = child.find(name='a',class_='mr-1')
        size_tag = child.find(name='small')
        temp = '项目:%s(%s);项目路径:%s' % (project_tag.get('href'),size_tag.string,project_tag.string,)
        print(temp)