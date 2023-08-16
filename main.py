import smtplib, ssl, csv, random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
import socks
import time
from loguru import logger
import tkinter as tk  # 在代码里面导入库，起一个别名，以后代码里面就用这个别名
from tkinter import filedialog
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
from tkinter import scrolledtext
import threading
from contant import get_html


class MailServer:
    def __init__(self, proxy_port, sender_file, receiver_file_list, html_file_list, subject, name, mail_file_list):
        # 如果在国内的话挂上本机VPN代理监听端口
        # if proxy_port != '-1':
        #     socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', int(proxy_port), True)
        #     socks.wrapmodule(smtplib)

        self.html_file_list = html_file_list
        self.sender_file = sender_file
        self.receiver_file_list = receiver_file_list
        self.subject = subject
        self.name = name
        self.counter = {}
        self.mail_file_list = mail_file_list

        self.window = tk.Tk()
        self.window.title("Cher8-MailRobot")
        self.window.geometry("600x600+612+180")
        # 创建一个带滚动轴的文本框
        self.text_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, width=500, height=500)
        self.text_area.place(x=50, y=25)

        thread = threading.Thread(target=self.main)
        thread.start()

        self.window.mainloop()



    def main(self):
        with open(self.sender_file) as f:
            sender_list = [row for row in csv.reader(f)]

        for receiver_file in self.receiver_file_list:
            with open(receiver_file, 'r', encoding='ISO-8859-1') as f:
                receiver_list = [row for row in csv.reader(f)]

            for receiver in receiver_list:
                random_sender = random.choice(sender_list)
                sender = random_sender[0]
                password = random_sender[1]

                if sender not in self.counter:
                    self.counter[sender] = 0

                if self.counter[sender] >= 3:
                    continue
                try:
                    # sec = [1, 2, 3, 4, 5, 6]
                    context = ssl.create_default_context()
                    time.sleep(1)
                    server = smtplib.SMTP_SSL('smtp.gmail.com', port=465, context=context, timeout=30)
                    server.login(sender, password)
                    logger.info('启动server成功')
                    try:
                        self.send_mail(server, sender, receiver, random_sender)
                        logger.info(f'Sender: {sender}, Receiver: {receiver[1]}, Status: Success!')
                        with open('res.csv', "a") as csvfile:
                            data = [sender, receiver[1], 1]
                            csv_writer = csv.writer(csvfile)
                            csv_writer.writerow(data)
                        self.text_area.insert(tk.END ,f'Sender: {sender}, Receiver: {receiver[1]}, Status: Success! \n')
                        self.window.update()

                    except Exception as e:
                        self.counter[sender] += 1
                        logger.error(f"Mail error sending email From {sender} to {receiver[1]}: {e}")
                        self.text_area.insert(tk.END ,f'Sender: {sender}, Receiver: {receiver[1]}, Status: Failed! \n')

                        with open('error.txt', "a") as file:
                            file.write(f"Mail error sending email From {sender} to {receiver[1]}: {e} \n")

                        with open('res.csv', "a") as csvfile:
                            data = [sender, receiver[1], 0]
                            csv_writer = csv.writer(csvfile)
                            csv_writer.writerow(data)
                        with open('fail_email.csv', "a") as csvfile:
                            data = [receiver[0], receiver[1]]
                            csv_writer = csv.writer(csvfile)
                            csv_writer.writerow(data)
                except Exception as e:
                    self.counter[sender] += 1
                    self.text_area.insert(tk.END ,f'Sender: {sender}, Receiver: {receiver[1]}, Status: Failed! \n')
                    logger.error(f"Server error sending email From {sender} to {receiver[1]}: {e}")
                    with open('error.txt', "a") as file:
                        file.write(f"Server error sending email From {sender} to {receiver[1]}: {e} \n")
                    with open('res.csv', "a") as csvfile:
                        data = [sender, receiver[1], 0]
                        csv_writer = csv.writer(csvfile)
                        csv_writer.writerow(data)
                    with open('fail_email.csv', "a") as csvfile:
                        data = [receiver[0], receiver[1]]
                        csv_writer = csv.writer(csvfile)
                        csv_writer.writerow(data)
        self.text_area.insert(tk.END ,f'All is OK, please close \n')
        time.sleep(2)

    def send_mail(self, server, sender, receiver, random_sender):
        message = MIMEMultipart()
        if len(self.html_file_list):
            html_file = random.choice(self.html_file_list)
            with open(html_file, 'r', encoding='utf-8') as file:
                html_content = file.read()
            soup = BeautifulSoup(html_content, 'html.parser')
            html_text = str(soup)
        else:
            html_text = get_html(receiver=receiver[0], sender = random_sender[2], category=receiver[3], index=int(receiver[2]))
        message["From"] = Header(f'{self.name} <{sender}>')
        message["To"] = Header(receiver[0].lower())
        message["Subject"] = Header(self.subject)
        mail_content = MIMEText(html_text, _subtype='html')
        message.attach(mail_content)

        for file in self.mail_file_list:
            if file.split('/')[-1].split('.')[-1] == 'pdf':
                pdfApart = MIMEApplication(open(file, 'rb').read())
                pdfApart.add_header('Content-Disposition', 'attachment', filename=file.split('/')[-1])
                message.attach(pdfApart)
            else:
                att = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
                att["Content-Type"] = 'application/octet-stream'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
                att["Content-Disposition"] = 'attachment; filename={}'.format(file.split('/')[-1])
                message.attach(att)

        server.sendmail(sender, receiver[1], message.as_string())


class robot_gui:
    def __init__(self):
        self.sender_file_list = ''
        self.receiver_file_list = []
        self.content_file_list = []
        self.extend_file_list = []


        self.window = tk.Tk()
        self.window.title("Cher8-MailRobot")
        self.window.geometry("600x600+612+180")
        img = Image.open(r'logo.jpg')
        photo = ImageTk.PhotoImage(img.resize((40, 40)))  # 改变图片显示大小
        lbl = tk.Label(self.window, image=photo, )
        lbl.place(x=150, y=15)
        lbl = tk.Label(self.window, text="Cher8-MailRobot", font=("楷体", 20))
        lbl.place(x=200, y=20)

        # 发送邮件csv
        sender_lbl = tk.Label(self.window, text="选择你的发送邮件csv文件：", font=("宋体", 12))
        sender_lbl.place(x=100, y=100)
        sender_btn = tk.Button(self.window, text="选择文件", command=self.sender_btn_clicked, font=("宋体", 12))
        sender_btn.place(x=330, y=95)
        self.sender_file_list_lbl = tk.Label(self.window, text="已选择的文件：", font=("宋体", 12))
        self.sender_file_list_lbl.place(x=100, y=135)

        # 接收邮件csv
        receiver_lbl = tk.Label(self.window, text="选择你的接收邮件csv文件：", font=("宋体", 12))
        receiver_lbl.place(x=100, y=170)
        receiver_btn = tk.Button(self.window, text="选择文件", command=self.receiver_btn_clicked, font=("宋体", 12))
        receiver_btn.place(x=330, y=165)
        self.receiver_file_list_lbl = tk.Label(self.window, text="已选择的文件：", font=("宋体", 12))
        self.receiver_file_list_lbl.place(x=100, y=205)

        # 邮件内容
        content_lbl = tk.Label(self.window, text="选择你的邮件内容-HTML文件：", font=("宋体", 12))
        content_lbl.place(x=100, y=240)
        content_btn = tk.Button(self.window, text="选择文件", command=self.content_btn_clicked, font=("宋体", 12))
        content_btn.place(x=330, y=235)
        self.content_file_list_lbl = tk.Label(self.window, text="已选择的文件：", font=("宋体", 12))
        self.content_file_list_lbl.place(x=100, y=275)

        # 选择附件
        extend_lbl = tk.Label(self.window, text="选择你的邮件附件：", font=("宋体", 12))
        extend_lbl.place(x=100, y=310)
        extend_btn = tk.Button(self.window, text="选择文件", command=self.extend_btn_clicked, font=("宋体", 12))
        extend_btn.place(x=330, y=305)
        self.extend_file_list_lbl = tk.Label(self.window, text="已选择的文件：", font=("宋体", 12))
        self.extend_file_list_lbl.place(x=100, y=345)

        # 邮件主题
        subject_lbl = tk.Label(self.window, text="输入你的邮件主题：", font=("宋体", 12))
        subject_lbl.place(x=100, y=380)
        self.subject_entry = tk.Entry(self.window, font=("宋体", 12), fg="red", width=20)
        self.subject_entry.place(x=250, y=380)

        # 发送邮件者
        name_lbl = tk.Label(self.window, text="输入发送者名称：", font=("宋体", 12))
        name_lbl.place(x=100, y=430)
        self.name_entry = tk.Entry(self.window, font=("宋体", 12), fg="red", width=20)
        self.name_entry.place(x=250, y=430)

        # 本地VPN监听端口号，可以填-1表示没有
        port_lbl = tk.Label(self.window, text="本地VPN监听端口号(-1表示没有)：", font=("宋体", 12))
        port_lbl.place(x=100, y=480)
        self.port_entry = tk.Entry(self.window, font=("宋体", 12), fg="red", width=20)
        self.port_entry.place(x=350, y=480)

        # 确认按钮
        confirm_btn = tk.Button(self.window, text="确认", command=self.confirm_btn_clicked, font=("宋体", 16))
        confirm_btn.place(x=250, y=540)

        self.window.mainloop()

    def sender_btn_clicked(self):
        file_path = filedialog.askopenfilename(
            title="选择CSV文件",
            filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
        )
        self.sender_file_list = file_path
        self.sender_file_list_lbl.configure(text=f'已选择的文件：{file_path.split("/")[-1]}')

    def receiver_btn_clicked(self):
        file_paths = filedialog.askopenfilenames(
            title="选择CSV文件",
            filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
        )
        self.receiver_file_list = file_paths
        file_paths_str = ''
        for file_path in file_paths:
            file_paths_str = file_paths_str + f'{file_path.split("/")[-1]},'
        self.receiver_file_list_lbl.configure(text=f'已选择的文件：{file_paths_str}')

    def extend_btn_clicked(self):
        file_paths = filedialog.askopenfilenames(
            title="选择附件",
            filetypes=(("All files", "*.*"),)
        )
        self.extend_file_list = file_paths
        file_paths_str = ''
        for file_path in file_paths:
            file_paths_str = file_paths_str + f'{file_path.split("/")[-1]},'
        self.extend_file_list_lbl.configure(text=f'已选择的文件：{file_paths_str}')

    def content_btn_clicked(self):
        file_paths = filedialog.askopenfilenames(
            title="选择HTML文件",
            filetypes=(("HTML files", "*.html"), ("All files", "*.*"))
        )
        self.content_file_list = file_paths
        file_paths_str = ''
        for file_path in file_paths:
            file_paths_str = file_paths_str + f'{file_path.split("/")[-1]},'
        self.content_file_list_lbl.configure(text=f'已选择的文件：{file_paths_str}')

    def confirm_btn_clicked(self):
        if len(self.receiver_file_list) and len(self.sender_file_list) \
                and self.name_entry.get() and self.subject_entry.get()  and self.port_entry.get():
            logger.info('sender_file_list:' + str(self.sender_file_list) + '\n'
                        + 'receiver_file_list:' + str(self.receiver_file_list) + '\n'
                        + 'content_file_list:' + str(self.content_file_list) + '\n'
                        + 'subject:' + str(self.subject_entry.get()) + '\n'
                        + 'name:' + str(self.name_entry.get()) + '\n'
                        + 'port:' + str(self.port_entry.get()))

            sender_file_list = self.sender_file_list
            port = self.port_entry.get()
            receiver_file_list = self.receiver_file_list
            content_file_list = self.content_file_list
            subject = self.subject_entry.get()
            name = self.name_entry.get()
            extend_file_list = self.extend_file_list
            self.window.destroy()
            MailServer(proxy_port=port, sender_file=sender_file_list,
                       receiver_file_list=receiver_file_list, html_file_list=content_file_list,
                       subject=subject, name=name, mail_file_list=extend_file_list)
        else:
            logger.error('请填好所有')


if __name__ == '__main__':
    robot_gui()
    # proxy_port = 10808
    # sender_file = 'user_csv/user7.csv'
    # receiver_file = 'receiver_csv/mails_test.csv'
    # reply_to = 'support@cher8.com'
    # subject = ' Alumni Start-up Support'
    # name = 'NYU Extreprenuership'
    # mail_file_list = ['receiver_csv/mails_test.csv']
    #
    # MailServer(proxy_port=proxy_port, sender_file=sender_file, receiver_file=receiver_file,
    #            reply_to=reply_to, subject=subject, name=name, mail_file_list=mail_file_list)