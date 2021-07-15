"""
功能描述：清理微头条
编写人：SongXuwen
编写日期：
实现逻辑：
    1.启动app后点击进入关注tab
    2.判断当前页面资源中有没有昵称的存在
        2.1 有昵称就证明还存在微头条，就继续循环删除第一条微头条
            2.1.1 删除微头条先刷新页面
                刷新页面调用public里的swipeDown()方法


        2.2.有昵称存在进入循环删除
            2.2.1点击进入微头条，点右上角更多，点击删除按钮，提示框点击确定


"""
import time

from selenium.webdriver.common.by import By

from common.driver import Driver
from common.log import logger
# from common.public import RunSwipe


def cleanheadline():
    driver = Driver().startUp()
    driver.launch_app()
    time.sleep(3)
    driver.find_element(By.XPATH, '//android.view.View[@content-desc="关注"]').click()
    time.sleep(3)

    # 判断当前页面的资源中有没有昵称元素
    while True:
        logger.info('开始清理微头条------')
        if '阿拉不啊卡' in driver.page_source:
            driver.find_elements(By.ID, 'com.ss.android.article.news:id/aee')[0].click()
            # time.sleep(3)
            driver.find_element(By.ID, 'com.ss.android.article.news:id/cnd').click()
            # time.sleep(3)
            driver.find_element(By.XPATH,
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ViewSwitcher/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.ImageView').click()
            # time.sleep(3)
            driver.find_element(By.ID, 'com.ss.android.article.news:id/ako').click()
            time.sleep(3)

        else:
            logger.info('所有微头条清理完毕,关闭app------')
            driver.close_app()
            break


if __name__ == '__main__':
    cleanheadline()