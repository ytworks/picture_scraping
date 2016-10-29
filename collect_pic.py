#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import requests
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

def main(page, scroll = 100, s = 0.6):
    browser = webdriver.Chrome()
    browser.get(page)
    for i in range(scroll):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = browser.find_element_by_xpath('//input[@class="ksb _kvc"]')
        print element
        try:
            element.click()
        except:
            pass
        time.sleep(s)
        print i, "scrolling done"

    save_path = os.path.abspath('.')
    download_count = 0
    for img in browser.find_elements_by_tag_name("img"):
        if img.get_attribute('src') != None:
            if img.get_attribute('src').find('gstatic.com/images?q=tbn:') > 0:
                img_url = img.get_attribute('src')
                output = '%s/%03d.jpg' % (save_path,download_count)
                print('%s : Download... %s' % (download_count, os.path.basename(img_url)))
                with open(output,'wb') as f:
                    raw = requests.get(img_url).content
                    f.write(raw)
                    time.sleep(s)
                download_count += 1

    browser.close()


if __name__ == '__main__':
    import sys
    p = sys.argv
    if len(p) == 1:
        page = "https://www.google.co.jp/search?q=%E3%82%A4%E3%83%B3%E3%83%91%E3%83%8D&espv=2&biw=1110&bih=536&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjs-L-2-OjPAhUp9IMKHVppCLUQ_AUIBigB#imgrc=_"
        main(page = page, scroll = 1000)
    else:
        page = "https://www.google.co.jp/search?tbm=isch&q="
        page += p[1]
        main(page = page, scroll = 100)
