# coding:utf-8
import smtplib
from email.mime.text import MIMEText



class SendEmail():
    # global email_host
    # global send_user
    # global password
    # global total
    def __init__(self, email_host, send_user, password):
        self.email_host = email_host
        self.send_user = send_user
        self.password = password

    def send_mail(self, user_list, sub, content):
        user = "miao564103484"+"<"+self.send_user+">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(self.email_host)
        server.login(self.send_user, self.password)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    def send_main(self, pass_list, fail_list):
        pass_num = len(pass_list)
        fail_num = len(fail_list)
        count_num = pass_num + fail_num
        pass_result = "%.2f%%" %(float(pass_num)/float(count_num)*100)
        fail_result = "%.2f%%" %(float(fail_num)/float(count_num)*100)
        user_list = ['564103484@qq.com', 'miao56403484@163.com', 'chenmiao@km.com']
        sub = "接口自动化测试报告"
        content = "此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" %(count_num, pass_num, fail_num, pass_result, fail_result)
        self.send_mail(user_list, sub, content)

if __name__ == '__main__':
    sendemail = SendEmail(email_host='smtp.exmail.qq.com', send_user='chenmiao@km.com', password='Miao@123')
    sendemail.send_main([1, 2, 3, 4], [2, 3, 4, 5, 6, 7])