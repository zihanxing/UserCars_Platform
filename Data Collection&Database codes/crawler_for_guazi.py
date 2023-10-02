#example for 丰田:
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
def get_Toyota():
    #use following to avoid connection error:
    data = []
    ID = 1
    for x in ['kaluola','leiling','kaimeirui','hanlanda','xinweichi','rav4haiwai','yaris-l-zx','puladuo-jinkou','yaris-l-zhixiang','toyota-huangguan']:
        url1 = 'https://www.guazi.com/www/'+x+'/o1c-1/#bread'
        requests.adapters.DEFAULT_RETRIES = 5
        s1 = requests.session()
        s1.keep_alive = False
        r1 = s1.get(url1) #get request
        html_contents1 = r1.text #store the text of the request
        html_soup1 = BeautifulSoup(html_contents1, "html.parser") #use bs to find
        try:
            last = html_soup1.find('div', class_='list-wrap js-post').find('div', class_='pageBox').find('ul',class_='pageLink clearfix').find_all('li')[-2]
            last_int = int(last.get_text())
        except:
            continue
        for n in range(1,last_int+1):
            url = 'https://www.guazi.com/www/'+x+'/o'+str(n)+'c-1/#bread'
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            r = s.get(url) #get request
            html_contents = r.text #store the text of the request
            html_soup = BeautifulSoup(html_contents, "html.parser") #use bs to find
            try:
                div_listwrap = html_soup.find('div', class_='list-wrap js-post')
                ul_carlist = div_listwrap.find('ul', class_='carlist clearfix js-top')
                details=ul_carlist.findAll('li')
            except:
                continue
            for i in details:  # a li stores a car info
                print('正在爬取第' + str(ID) + '项...')
                info = []


                try:
                    url2 = i.find('a').get('href')
                    url2 = 'https://www.guazi.com'+url2
                    requests.adapters.DEFAULT_RETRIES = 5
                    s2 = requests.session()
                    s2.keep_alive = False
                    r2 = s2.get(url2) #get request
                    html_contents2 = r2.text #store the text of the request
                    html_soup2 = BeautifulSoup(html_contents2, "html.parser") #use bs to find
                    div_center = html_soup2.find('div', class_ = 'center js-center detail')
                    div_basic = div_center.find('div', class_ = 'basic-infor js-basic-infor js-top')
                    ul_eleven = div_basic.find('ul', class_ = 'basic-eleven clearfix')
                    div_five = ul_eleven.find('li', class_ = 'five')
                    gearbox = div_five.find('div', class_ = 'typebox')
                    if gearbox.get_text(strip=True) == '手动':
                        gearbox = 'manual'
                    elif gearbox.get_text(strip=True) == '自动':
                        gearbox = 'automatic'

                    div_six = ul_eleven.find('li', class_ = 'six')
                    volume = div_six.find('div', class_ = 'typebox')
                    div_seven = ul_eleven.find('li',class_='seven')
                    transfer = div_seven.find('div',class_='typebox')
                    div_clear = div_basic.find('div', class_ = 'detailcontent clearfix js-detailcontent active')
                    table2 = div_clear.find_all('table', class_ = 'param-table')[1]
                    horsepower = table2.find_all("tr")[4].find_all('td')[1]
                    torque = table2.find_all("tr")[5].find_all('td')[1]
                    fuel = table2.find_all("tr")[7].find_all('td')[1]
                except:
                    print('详情页获取失败')
                    continue



                name = i.find('h2', class_ = 't')
                
                
                type = name.get_text(strip=True).split(' ')[1]
                brand = name.get_text(strip=True).split(' ')[0]
                if type[:2] == '20':
                    type = brand[2:]
                    brand = brand[:2]
                if len(brand) != 2:
                    print('品牌型号错位')
                    continue
           


                age = i.find('div', class_ = 't-i')
                age, distance, service = age.get_text(strip=True).split('|')
                age_int = 2021 - int(age[:-1])
                image = i.find('img')
                price = i.find('p')
                original_price = i.find('em','line-through')
               
                info.append(ID)
                info.append(brand)
                info.append(type)
                info.append(float(volume.get_text(strip=True)[:3]))
                try:
                    info.append(gearbox)
                except:
                    info.append(np.NaN)
                try:
                    info.append(float(original_price.get_text(strip=True)[:-1]))
                except:
                    info.append(np.NaN)
                try:
                    info.append(float(price.get_text(strip=True)[:-1]))
                except:
                    info.append(np.NaN)
                try:
                    info.append(int(age[:-1]))
                except:
                    info.append(np.NaN)
                try:
                    info.append(age_int)
                except:
                    info.append(np.NaN)
                try:
                    info.append(float(distance[:-3]))
                except:
                    info.append(np.NaN)
                try:
                    info.append(float(horsepower.get_text(strip=True)))
                except:
                    info.append(np.NaN)
                try:
                    info.append(float(torque.get_text(strip=True)))
                except:
                    info.append(np.NaN)
                try:
                    info.append(int(transfer.get_text(strip=True)[0]))
                except:
                    info.append(np.NaN)
                try:
                    info.append(int(fuel.get_text(strip=True)[:2]))
                except:
                    info.append(np.NaN)
                info.append(image.get('src'))
                data.append(info)
                ID += 1


    result = pd.DataFrame(data, columns = ['ID','brand','type','volume(L)','gearbox','original price(w)','price(w)','year', 'age', 'mileage(wkm)','horsepower(Ps)','torque(N*m)','transfer number','fuel label ', 'image'])
    result = result.set_index('ID')
    
    #write to csv
    result.to_csv(r'C:\Users\78531\Desktop\Honda.csv')

    return result
get_Honda()