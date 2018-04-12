from ldap3 import Server, Connection, ALL, ALL_ATTRIBUTES, NTLM
name = 'mwd21'
username = "shopfomo\\" + name
print(username)
password = 'jaja1234'
print(password)
filter = '(sAMAccountName=' + name +')'
s = Server('www.shopfomo.me', get_info=ALL)
print('hello')
c = Connection(s, user=username, password=password, authentication=NTLM)
print('goodbye')
c.bind()
print('bind')
c.search('dc=shopfomo, dc=local', filter, attributes=['mail','sn','givenName','sAMAccountName'])
if len(c.entries) > 0:
    print(c.entries[0].sn)
    print(c.entries[0].givenName)
    print(c.entries[0].sAMAccountName)
