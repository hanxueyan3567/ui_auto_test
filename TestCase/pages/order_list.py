



class order_list():
    def __init__(self,base):
        self.base = base
        #订单列表超链接
        order_list_a = "//label[contains(text(),'订单状态：')]/following-sibling::div//input"
        # 点击订单状态
        order_status_a = "//label[contains(text(),'订单状态: ')]/following-sibling::div//input"

        # 选择待发货//span[contains(text(),"待发货")]
        base.click('点击待发货', '''//span[contains(text(),'待发货')]''')
        # 点击查询搜索//span[contains(text(),"查询搜索")]
        base.click('点击查询搜索', '''//span[contains(text(),'查询搜索')]''')
        # 选择第一笔订单进行发货//tbody/tr[1]/td[10]//span[contains(text(),"订单发货")]
        base.click('点击订单发货', '''//tbody/tr[1]/td[10]//span[contains(text(),"订单发货")]''')
        # 选择配送方式//input[@placeholder="请选择物流公司"]
        base.click('请选择物流公司', '''//input[@placeholder="请选择物流公司"]''')
        # 选择中通快递//ul//li[@class="el-select-dropdown__item"][2]
        base.click('中通快递', '''//ul//li[@class="el-select-dropdown__item"][2]''')
        # 填写物流单号(//input[@autocomplete="off"])[2]
        base.send_keys("单号", '''(//input[@class="el-input__inner"])[2]''', '458679453565')
        # 点击确定//span[contains(text(),"确定")]
        base.click('点击确定', '''(//span[contains(text(),"确定")])[1]''')
        # 点击确定//span[contains(text(),"确定")]
        base.click('点击确定', '''(//span[contains(text(),"确定")])[2]''')
        # 获取提示文本//div[@role="alert"]//p
        text = base.get_text("获取提示文本", '''//div[@role="alert"]//p''')