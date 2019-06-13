
from time import sleep
import pytest


class Test_mall():
    @pytest.mark.fahuo
    def test_fahuo(self,base):
        base.driver.get("http://192.168.60.132/#/oms/order")
        #点击订单状态//label[contains(text(),"订单状态")]/following-sibling::div//input
        base.click('点击订单状态', '''//label[contains(text(),"订单状态")]/following-sibling::div//input''')
        #选择待发货//span[contains(text(),"待发货")]
        base.click('点击待发货', '''//span[contains(text(),'待发货')]''')
        #点击查询搜索//span[contains(text(),"查询搜索")]
        base.click('点击查询搜索', '''//span[contains(text(),'查询搜索')]''')
        #选择第一笔订单进行发货//tbody/tr[1]/td[10]//span[contains(text(),"订单发货")]
        base.click('点击订单发货', '''//tbody/tr[1]/td[10]//span[contains(text(),"订单发货")]''')
        #选择配送方式//input[@placeholder="请选择物流公司"]
        base.click('请选择物流公司', '''//input[@placeholder="请选择物流公司"]''')
        #选择中通快递//ul//li[@class="el-select-dropdown__item"][2]
        base.click('中通快递', '''//ul//li[@class="el-select-dropdown__item"][2]''')
        #填写物流单号(//input[@autocomplete="off"])[2]
        base.send_keys("单号",'''(//input[@class="el-input__inner"])[2]''','458679453565')
        #点击确定//span[contains(text(),"确定")]
        base.click('点击确定', '''(//span[contains(text(),"确定")])[1]''')
        # 点击确定//span[contains(text(),"确定")]
        base.click('点击确定', '''(//span[contains(text(),"确定")])[2]''')
        # 获取提示文本//div[@role="alert"]//p
        text = base.get_text("获取提示文本", '''//div[@role="alert"]//p''')
        # 断言
        assert "发货成功" in text
        sleep(3)
        pass
    @pytest.mark.tuihuo
    def test_tuihuo(self,base):
        base.driver.get("http://192.168.60.132/#/oms/returnApply")
        #点击处理状态//label[ contains(text(),'处理状态：')]/following-sibling::div//input
        base.click('点击处理状态', '''//label[ contains(text(),'处理状态：')]/following-sibling::div//input''')
        #选择待处理//ul//span[contains(text(),'待处理')]
        base.click('点击待处理', '''//ul//span[contains(text(),'待处理')]''')
        # 点击查询搜索//span[contains(text(),"查询搜索")]
        base.click('点击查询搜索', '''//span[contains(text(),'查询搜索')]''')
        # 点击第一笔订单的查看详情//span[contains(text(),"查看详情")]
        base.click('点击第一笔订单的查看详情', '''//tbody/tr[1]/td[8]//span[contains(text(),'查看详情')]''')
        #获取退款金额
        money = base.get_text("获取订单金额", '''//div[contains(text(),'订单金额')]/following-sibling::div''')
        money = money[1:]
        #填写确认退款金额
        base.send_keys("输入退款金额", '''//div[contains(text(),'确认退款金额')]/following-sibling::div//input''', str(money))
        # 点击确认退货
        base.click("点击确认退货", '''//span[contains(text(),'确认退货')]''')
        # 点击确定//span[contains(text(),'确定')]
        base.click('点击确定', '''//span[contains(text(),'确定')]''')
        # 获取操作提示文本//div[@role="alert"]//p
        actual = base.get_text("获取操作提示文本", '''//div[@role="alert"]//p''')
        #断言
        assert '操作成功' in actual