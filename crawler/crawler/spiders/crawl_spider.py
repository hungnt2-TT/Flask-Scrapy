import time

from flask import session
from scrapy import Spider
from scrapy_selenium import SeleniumRequest
from selenium.common import StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from app.main import db
from app.main.model.coupon import Coupon


class CouponSpider(Spider):
    name = 'crawl_coupon'
    myBaseUrl = ''
    start_urls = []

    def __init__(self, category='', **kwargs):
        self.myBaseUrl = category
        self.start_urls.append(self.myBaseUrl)
        super().__init__(**kwargs)

    def start_requests(self):
        print('ILODOOOO')
        url = self.myBaseUrl
        yield SeleniumRequest(url=url,
                              callback=self.parse, )

    def parse(self, response):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(5)
        link = response.xpath('//a[contains(@class, "block") and contains(@class, "underline")]')

        for links in link:
            href = links.xpath('./@href').get()
            if href:
                url = response.urljoin(href)
                yield SeleniumRequest(url=url, callback=self.parse_outlink, wait_time=30, meta={'driver': driver})

    def parse_outlink(self, response):
        browser = response.request.meta['driver']
        browser.get(response.url)
        wait = WebDriverWait(browser, 5)
        coupon_element = response.xpath("//li[contains(text(), 'Coupons')]")
        if coupon_element:
            offer_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                             "//div[@class='BrandOffers']//span[@class='absolute top-0 left-0 w-[calc(100%_-_56px)]']")))
            coupon_list = []
            i = 0
            while i < len(offer_elements):
                detai_coupon = offer_elements[i]
                try:
                    browser.execute_script("arguments[0].click();", detai_coupon)
                    wait.until(EC.staleness_of(detai_coupon))
                    handles = browser.window_handles
                    browser.switch_to.window(handles[-1])
                    coupon_locator = (By.XPATH, "/html/body/div[1]/div[6]/div/div/div[2]/div[1]/div/div[2]/div[1]")
                    coupon = wait.until(EC.presence_of_element_located(coupon_locator))
                    coupon_code = coupon.text
                    coupon_list.append(coupon_code)
                    browser.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/div/div[2]/span").click()
                except StaleElementReferenceException:
                    offer_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                                     "//div[@class='BrandOffers']//span[@class='absolute top-0 left-0 w-[calc(100%_-_56px)]']")))
                    if i >= len(offer_elements):
                        break
                    else:
                        continue
                except ElementClickInterceptedException:
                    time.sleep(2)
                    continue
                i += 1
            for coupon_code in coupon_list:
                coupon_model = Coupon(
                    coupon_code=coupon_code, url=response.url)
                db.session.add(coupon_model)
            db.session.commit()
        else:
            print('No coupon element found')

