import requests
import json

class Fetcher:
    def __init__(self, openId):
        self.api_address = "http://www.szlzxn.cn/wxn/getStationList"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.60(0x18003c2f) NetType/WIFI Language/zh_CN",
            "Host": "www.szlzxn.cn",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        self.openId = openId
        self.status = True
        
    def make_params(self, lat, lng):
        return {
            "openId": self.openId,
            "latitude": lat,
            "longitude": lng,
            "areaid": 6,
            "devtype": 0
        }
        
    def fetch(self, params):
        response = requests.post(self.api_address, headers=self.headers, data=params)
        try:
            json_data = response.json()
        except requests.exceptions.JSONDecodeError:
            # the response is not valid JSON
            return -2
        if json_data["success"] != True:
            return -1
        return json_data

    def save_json(self, data, filename="tmp.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            
    def full_fetch(self):
        # 读取json文件
        with open("location.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            info = []
            for site in data.get("sites_yq", []): # 遍历每个站点组
                # 获取站点基本信息
                site_total = 0
                site_avalaible = 0
                site_used = 0
                site_error = 0
                site_name = site["group_sim_name"]
                for detail in site.get("details", []): # 遍历组内每个站点
                    
                    devaddress = detail["devaddress"] # 获取设备地址
                    # print(f"Fetching data for {devaddress} at latitude {detail['latitude']} and longitude {detail['longitude']}")
                    params = self.make_params(detail["latitude"], detail["longitude"])
                    result = self.fetch(params)
                    # 错误处理
                    if result == -1:
                        print(f"Failed to fetch data for {devaddress}")
                        self.status = False
                        break
                    elif result == -2:
                        print(f"Invalid JSON response for {devaddress}")
                        print("Retrying...")
                        result = self.fetch(params)  # Retry fetching
                        if result == -1:
                            print(f"Retry failed for {devaddress}")
                            self.status = False
                            break
                        elif result == -2:
                            print(f"Retry still returned invalid JSON for {devaddress}")
                            self.status = False
                            break
                    # 解析结果
                    for item in result.get("obj", []):
                        # 寻找匹配项
                        while item["devaddress"] != devaddress:
                            continue
                        # 找到匹配项
                        # print(item)
                        portstatus = item["portstatus"]
                        if portstatus:
                            site_avalaible += portstatus.count("0")
                            site_used += portstatus.count("1")
                            site_error += portstatus.count("3")
                            site_total += len(portstatus)
                        else:
                            print(f"Port status is None for {devaddress}")
                        break
                # 封装站点组信息为json
                print(f"Site {site_name} - Total: {site_total}, Available: {site_avalaible}, Used: {site_used}, Error: {site_error}")
                site_info = {
                    "site_name": site_name,
                    "site_total": site_total,
                    "site_avalaible": site_avalaible,
                    "site_used": site_used,
                    "site_error": site_error
                }
                info.append(site_info)
                    
                if not self.status:
                    break

            if not self.status:
                print("Full fetch failed.")
                return -1
            
            self.save_json(info, "full_fetch_result.json")
            print("Full fetch completed successfully.")
            return info

if __name__ == "__main__":
    fetcher = Fetcher(" ")
    # params = fetcher.make_params(30.268537521362305, 120.12606048583984)
    # result = fetcher.fetch(params)
    # fetcher.save_json(result)
    fetcher.full_fetch()