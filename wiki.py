from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
url=input("Enter URL: ")
if "wikipedia" in url:
    ll=url.split("/")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}

    html_page=requests.get(url,headers=headers)
    soup=BeautifulSoup(html_page.content,"html.parser")
    # print(soup)
    list_ref=soup.find_all("ol",class_="references")
    # list_ref.extend(soup.find_all_next("ol",class_="references"))
    with open(f'{ll[-1]}.txt', 'w',encoding='utf-8') as f:
        for i in range(len(list_ref)):
            f.write(f'{str(i)} {str(list_ref[i].get_text())}')
            f.write("\n")
            # print(f'{str(i)} {str(list_ref[i].get_text())}')
    # msg=MIMEMultipart()
    # subject = f"Reference Of {ll[-1]} from Wikipedia"
    # from_add='your gmail'
    # to=input("ENter To Email add. : ")
    
    # msg['From']=from_add
    # msg['To']=to
    # msg['Subject']=subject
    # body="Here is the attached file:"
    # msg.attach(MIMEText(body,'plain'))
    
        
    # my_file=open(f'{ll[-1]}.txt','rb')
    # part=MIMEBase('application','octet-stream')
    # part.set_payload((my_file).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition','attachment; filename= '+ f'{ll[-1]}.txt')
    # msg.attach(part)    
    
    
    # message=msg.as_string()
    
    # server=smtplib.SMTP('smtp.gmail.com',587)
    # server.starttls()
    # server.login(from_add,'your login code')
    # server.sendmail(from_add,to,message)
    # server.quit()
else:
    print("Enter Correct URL!")
