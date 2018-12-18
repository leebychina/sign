from bs4 import BeautifulSoup
import requests
url = requests.get('https://github.com/login')
soup1 = BeautifulSoup(url.text,features='html.parser')
tag = soup1.find(name='input',attrs={'name':'authenticity_token'})
authenticity_token = tag.get('value')
c1=url.cookies.get_dict()
url.close()
form_data = {
    'authenticity_token':authenticity_token,
    'utf8':'',
    'commit':'Sign in',
    'login':"",#you github email
    'password':""#you password
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
        temp = 'project:%s(%s);projectpath:%s' % (project_tag.get('href'),size_tag.string,project_tag.string,)
        print(temp)