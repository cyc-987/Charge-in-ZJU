from dingtalkchatbot.chatbot import DingtalkChatbot

class DingBot:
    def __init__(self, webhook, secret):
        self.webhook = webhook
        self.secret = secret
        self.bot = DingtalkChatbot(webhook, secret=secret)
    
    def send_status_message(self, time, json_content):
        if not json_content:
            print("No data to send.")
            return
        
        # Prepare the message
        message = f"> 抓取时间 - {time}\n"
        for site in json_content:
            message += f"##### **{site['site_name']}**-----\n"
            message += f"**{site['site_avalaible']}**可用/"
            message += f"**{site['site_used']}**已用/"
            message += f"**{site['site_error']}**错误/"
            message += f"**{site['site_total']}**总端口\n\n"
        message += "> 有未收录站点请发送邮箱至 <群主邮箱>\n"
        # Send the message
        self.bot.send_markdown(title="站点状态更新", text=message)
        print("Message sent successfully.")

    def send_error_message(self, time):
        # Prepare the error message
        message = f"抓取时间 - {time}\n"
        message += f"openId已过期\n"
        message += "群主来修一下"
        # Send the error message
        self.bot.send_text(msg=message, at_mobiles=["群主手机号"])
        print("Error message sent successfully.")