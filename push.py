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
        total_num = 0
        total_available = 0
        total_used = 0
        total_error = 0
        message = f"> 抓取时间 - {time}\n"
        for site in json_content:
            message += f"##### **{site['site_name']}**\n"
            message += f"**{site['site_available']}**可用/"
            total_available += site['site_available']
            message += f"**{site['site_used']}**已用/"
            total_used += site['site_used']
            message += f"**{site['site_error']}**错误/"
            total_error += site['site_error']
            message += f"**{site['site_total']}**总端口\n\n"
            total_num += site['site_total']
        message += f"##### **总计**\n"
        message += f"**{total_available}**可用/"
        message += f"**{total_used}**已用/"
        message += f"**{total_error}**错误/"
        message += f"**{total_num}**总端口\n\n"
        message += f"使用率: **{(total_used / (total_num-total_error) * 100) if (total_num-total_error) > 0 else "NaN":.2f}%**\n\n"
        message += "> 有未收录站点请发送邮箱至 <群主邮箱>\n"
        # Send the message
        try:
            self.bot.send_markdown(title="站点状态更新", text=message)
        except Exception as e:
            print(f"Failed to send message: {e}")
            return
        print("Message sent successfully.")

    def send_error_message(self, time):
        # Prepare the error message
        message = f"抓取时间 - {time}\n"
        message += f"查询API返回异常\n"
        message += "等待十分钟后自动重试\n"
        message += "通知群主"
        # Send the error message
        try:
            self.bot.send_text(msg=message, at_mobiles=["群主手机号"])
        except Exception as e:
            print(f"Failed to send error message: {e}")
            return
        print("Error message sent successfully.")