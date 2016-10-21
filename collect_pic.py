#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import requests
from pyquery import PyQuery as pq




def main(page):
    save_path = os.path.abspath('.')
    r = requests.get(page)
    query = pq(r.content)
    #imgs_html = query('img').filter('.btnOver')
    imgs_html = query('img')

    download_count = 0
    for img_html in imgs_html:
        img_file = pq(img_html).attr('src')
        img_url = img_file

        download_count += 1
        output = '%s/%03d.jpg' % (save_path,download_count)
        print('%s : Download... %s' % (download_count, os.path.basename(img_url)))
        with open(output,'wb') as f:
            raw = requests.get(img_url).content
            f.write(raw)

if __name__ == '__main__':
    page = "https://www.google.co.jp/search?q=%E3%82%A4%E3%83%B3%E3%83%91%E3%83%8D&espv=2&biw=1110&bih=536&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjs-L-2-OjPAhUp9IMKHVppCLUQ_AUIBigB#imgrc=_"
    main(page = page)
