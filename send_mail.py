# -*-coding:utf-8-*-

# ===============================================================================
# 导入smtplib和MIMEText
# ===============================================================================
from email.mime.text import MIMEText
import smtplib

# ===============================================================================
# 要发给谁，这里发给2个人
# ===============================================================================
mailto_list = ["wangzhentao@iairportcloud.com"]

# ===============================================================================
# 设置服务器，用户名、口令以及邮箱的后缀
# ===============================================================================
mail_host = "smtp.qq.com"
mail_user = "952779404"
mail_pass = "tsvdyjbwkyecbcca"
mail_postfix = "qq.com"


# ===============================================================================
# 发送邮件
# ===============================================================================
def send_mail(to_list, sub, content):

    '''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''

    me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP_SSL(mail_host, 465)
        s.set_debuglevel(1)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False


if __name__ == '__main__':
    if send_mail(mailto_list, "here is subject", "here is content"):
        print "发送成功"
    else:
        print "发送失败"