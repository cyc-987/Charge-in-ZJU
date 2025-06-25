# ZJU Charger
> 快速查询充电桩状态的python脚本

## 功能简介
- [x] 定期查询充电桩状态
- [x] 覆盖玉泉校区
- [x] 直接从URL解析openId
- [x] 命令行启动
- [x] 钉钉机器人推送

## 关于缺省的location.json
`location.json`文件包含了充电桩的位置信息。出于隐私和安全考虑，我并没有上传该文件。

如果你想使用该脚本，请自行创建一个`location.json`文件，格式如下：

```json
{
    "last_modified": "",
    "maintainer": "",
    "sites_yq":[
        {
            "group_id": 1,
            "group_site_nums": 3,
            "group_sim_name": "<这个站点名称会显示在最后的查询结果里>",
            "details":[
                {
                    "devid": ,
                    "areaid": ,
                    "devaddress": , # 此为必填项
                    "devdescript": "",
                    "longitude": , # 此为必填项
                    "latitude": , # 此为必填项
                    "simDevaddress": ""
                }
            ]
        }
    ]
}
```

## 依赖库
`pip install -r requirements.txt`

## 使用方法

### 配置`location.json`
至于里面的参数如何获得，请自行抓包。

### 配置钉钉机器人
webhook和secret在`main.py`中配置。

群主的电话号和邮箱需要在`push.py`中配置，用于发生错误时在群中at群主。

### 启动脚本
本脚本支持直接从npd的充电桩链接url中提取openId，因此你可以直接在命令行中运行：
```bash
python main.py "<url>"
```
