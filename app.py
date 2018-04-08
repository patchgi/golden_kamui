import os
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selene.driver import SeleneDriver
from webdriver_manager.chrome import ChromeDriverManager
import re
import urllib.request
import sys

def getPageURL():
    pages = ["https://tonarinoyj.jp/episode/10834108156629615343"]
    options = Options()
    options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
    options.add_argument('--headless')
    driver = SeleneDriver.wrap(webdriver.Chrome(executable_path="/Users/patchgi/.wdm/chromedriver/2.37/mac64/chromedriver", chrome_options=options))
    driver.get(pages[0])
    episode = driver.find_elements_by_class_name("series-episode-list-container")
    res = urllib.request.urlopen("https://tonarinoyj.jp/api/viewer/readable_products?current_readable_product_id=10834108156629615349&number_since=98&number_until=4&read_more_num=250&type=episode")
    data = str(res.read().decode('utf-8'))
    pattern = r"https://tonarinoyj.jp/episode/[0-9]+"
    reg = re.compile(pattern)
    hide_pages = reversed(reg.findall(data))
    for e in reversed(episode):
        pages.append(e.get_attribute("href"))
    driver.quit()
    result = []
    for p in pages[:4]:
        result.append(p)
    for p in hide_pages:
        result.append(p)
    for p in pages[5:]:
        result.append(p)
    return result

def getPages(_story_url, driver, idx):
    dir_path = os.path.join("data/", str(idx))
    os.mkdir(dir_path)
    driver.get(_story_url)
    ps = driver.find_elements_by_tag_name("p")
    for _idx, p  in enumerate(ps):
        child = p.find_elements_by_tag_name("img")
        if len(child) > 0:
            urllib.request.urlretrieve(child[0].get_attribute("data-src"), os.path.join(dir_path, "{0}".format(_idx)))
    driver.quit()



def main():
    story_url=["https://tonarinoyj.jp/episode/10834108156629615343","https://tonarinoyj.jp/episode/10834108156629615346","https://tonarinoyj.jp/episode/10834108156629615349","https://tonarinoyj.jp/episode/10834108156629615352","https://tonarinoyj.jp/episode/10834108156629615355","https://tonarinoyj.jp/episode/10834108156629615358","https://tonarinoyj.jp/episode/10834108156629615361","https://tonarinoyj.jp/episode/10834108156629615364","https://tonarinoyj.jp/episode/10834108156629615367","https://tonarinoyj.jp/episode/10834108156629615370","https://tonarinoyj.jp/episode/10834108156629615373","https://tonarinoyj.jp/episode/10834108156629615376","https://tonarinoyj.jp/episode/10834108156629615379","https://tonarinoyj.jp/episode/10834108156629615382","https://tonarinoyj.jp/episode/10834108156629615385","https://tonarinoyj.jp/episode/10834108156629615388","https://tonarinoyj.jp/episode/10834108156629615391","https://tonarinoyj.jp/episode/10834108156629615394","https://tonarinoyj.jp/episode/10834108156629615397","https://tonarinoyj.jp/episode/10834108156629615400","https://tonarinoyj.jp/episode/10834108156629615403","https://tonarinoyj.jp/episode/10834108156629615406","https://tonarinoyj.jp/episode/10834108156629615409","https://tonarinoyj.jp/episode/10834108156629615412","https://tonarinoyj.jp/episode/10834108156629615415","https://tonarinoyj.jp/episode/10834108156629615418","https://tonarinoyj.jp/episode/10834108156629615421","https://tonarinoyj.jp/episode/10834108156629615424","https://tonarinoyj.jp/episode/10834108156629615427","https://tonarinoyj.jp/episode/10834108156629615430","https://tonarinoyj.jp/episode/10834108156629615433","https://tonarinoyj.jp/episode/10834108156629615436","https://tonarinoyj.jp/episode/10834108156629615439","https://tonarinoyj.jp/episode/10834108156629615442","https://tonarinoyj.jp/episode/10834108156629615445","https://tonarinoyj.jp/episode/10834108156629615448","https://tonarinoyj.jp/episode/10834108156629615451","https://tonarinoyj.jp/episode/10834108156629615454","https://tonarinoyj.jp/episode/10834108156629615457","https://tonarinoyj.jp/episode/10834108156629615460","https://tonarinoyj.jp/episode/10834108156629615463","https://tonarinoyj.jp/episode/10834108156629615466","https://tonarinoyj.jp/episode/10834108156629615469","https://tonarinoyj.jp/episode/10834108156629615472","https://tonarinoyj.jp/episode/10834108156629615475","https://tonarinoyj.jp/episode/10834108156629615478","https://tonarinoyj.jp/episode/10834108156629615481","https://tonarinoyj.jp/episode/10834108156629615484","https://tonarinoyj.jp/episode/10834108156629615487","https://tonarinoyj.jp/episode/10834108156629615490","https://tonarinoyj.jp/episode/10834108156629615493","https://tonarinoyj.jp/episode/10834108156629615496","https://tonarinoyj.jp/episode/10834108156629615499","https://tonarinoyj.jp/episode/10834108156629615502","https://tonarinoyj.jp/episode/10834108156629615505","https://tonarinoyj.jp/episode/10834108156629615508","https://tonarinoyj.jp/episode/10834108156629615511","https://tonarinoyj.jp/episode/10834108156629615514","https://tonarinoyj.jp/episode/10834108156629615517","https://tonarinoyj.jp/episode/10834108156629615520","https://tonarinoyj.jp/episode/10834108156629615523","https://tonarinoyj.jp/episode/10834108156629615526","https://tonarinoyj.jp/episode/10834108156629615529","https://tonarinoyj.jp/episode/10834108156629615532","https://tonarinoyj.jp/episode/10834108156629615535","https://tonarinoyj.jp/episode/10834108156629615538","https://tonarinoyj.jp/episode/10834108156629615541","https://tonarinoyj.jp/episode/10834108156629615544","https://tonarinoyj.jp/episode/10834108156629615547","https://tonarinoyj.jp/episode/10834108156629615550","https://tonarinoyj.jp/episode/10834108156629615553","https://tonarinoyj.jp/episode/10834108156629615556","https://tonarinoyj.jp/episode/10834108156629615559","https://tonarinoyj.jp/episode/10834108156629615562","https://tonarinoyj.jp/episode/10834108156629615565","https://tonarinoyj.jp/episode/10834108156629615568","https://tonarinoyj.jp/episode/10834108156629615571","https://tonarinoyj.jp/episode/10834108156629615574","https://tonarinoyj.jp/episode/10834108156629615577","https://tonarinoyj.jp/episode/10834108156629615580","https://tonarinoyj.jp/episode/10834108156629615583","https://tonarinoyj.jp/episode/10834108156629615586","https://tonarinoyj.jp/episode/10834108156629615589","https://tonarinoyj.jp/episode/10834108156629615592","https://tonarinoyj.jp/episode/10834108156629615595","https://tonarinoyj.jp/episode/10834108156629615598","https://tonarinoyj.jp/episode/10834108156629615601","https://tonarinoyj.jp/episode/10834108156629615604","https://tonarinoyj.jp/episode/10834108156629615607","https://tonarinoyj.jp/episode/10834108156629615610","https://tonarinoyj.jp/episode/10834108156629615613","https://tonarinoyj.jp/episode/10834108156629615616","https://tonarinoyj.jp/episode/10834108156629615619","https://tonarinoyj.jp/episode/10834108156629615622","https://tonarinoyj.jp/episode/10834108156629615625","https://tonarinoyj.jp/episode/10834108156629615628","https://tonarinoyj.jp/episode/10834108156629615631","https://tonarinoyj.jp/episode/10834108156629615637","https://tonarinoyj.jp/episode/10834108156629615640",]
    idx = int(sys.argv[1])
    print("___"+str(idx)+"___")
    options = Options()
    options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
    options.add_argument('--headless')
    driver = SeleneDriver.wrap(webdriver.Chrome(executable_path="/Users/patchgi/.wdm/chromedriver/2.37/mac64/chromedriver", chrome_options=options))
    getPages(story_url[idx], driver, idx)



if __name__ == "__main__":
    main()
    #print(getPageURL())
