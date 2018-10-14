from gmail import GMail,Message
import random
gmail = GMail("khanhtrandinh95@gmail.com","khanhdeptrai")
html_template = '''
<p>Chao sep,</p>
<p>Sang nay <strong>{{symtom}}</strong>)
'''
symtom_list = ["dau chan","dau bung","met"]
s = random.choice(symtom_list)
html_content = html_template.replace("{{symtom}}",s)
msg = Message("Your email has been hacked",to = "c4e.techkidsvn@gmail.com", html=html_content)
gmail.send(msg)

