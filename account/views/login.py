from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from formlib import Formless
from django import forms
from account.models import User
from ldap3 import Server, Connection, ALL, ALL_ATTRIBUTES, NTLM

@view_function
def process_request(request):

    #process the form
    form = loginForm(request)
    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/')

    #render the template
    return request.dmp.render('login.html', {
        'form': form,
    })

class loginForm(Formless):
    def init(self):
        '''Add fields to this form'''
        self.fields['username'] = forms.CharField(label='Username')
        self.fields['password'] = forms.CharField(label='Password', widget=forms.PasswordInput())
        self.user = None

    def clean(self):
        name = self.cleaned_data.get('username')
        username = "shopfomo\\" + name
        print(username)
        password = self.cleaned_data.get('password')
        print(password)
        filter = '(sAMAccountName=' + name +')'
        s = Server('www.shopfomo.me', get_info=ALL)
        c = Connection(s, user=username, password=password, authentication=NTLM)
        c.bind()
        c.search('dc=shopfomo, dc=local', filter, attributes=['mail','sn','givenName','sAMAccountName'])
        if len(c.entries) > 0:
            if User.objects.filter(email=(name + '@shopfomo.me')).count() > 0:
                self.user = authenticate(email=(name + '@shopfomo.me'), password=self.cleaned_data.get('password'))
            else:
                #make the user
                myUser = User()

                #load up the user
                myUser.first_name = c.entries[0].givenName
                myUser.last_name = c.entries[0].sn
                myUser.email = name + '@shopfomo.me'
                myUser.set_password(self.cleaned_data.get('password'))

                #save the new user
                myUser.save()
                self.user = authenticate(email=(name + '@shopfomo.me'), password=self.cleaned_data.get('password'))
        else:
            self.user = authenticate(email=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if self.user is None:
            raise forms.ValidationError('Invalid email or password.')
        return self.cleaned_data

    def commit(self):
        '''Actually process the form'''
        login(self.request, self.user)
