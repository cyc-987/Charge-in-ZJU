# ZJU Charger
> 快速查询充电桩状态的python脚本

## 功能简介
- [x] 定期查询充电桩状态
- [x] 覆盖玉泉校区
- [ ] 直接从URL解析openId
- [ ] 命令行启动
- [ ] 钉钉机器人推送

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