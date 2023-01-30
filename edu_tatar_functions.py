from bs4 import BeautifulSoup
from pprint import pprint

def upload_files(session, files, proxy, target_folder='food'):
    h = {"Referer": "https://edu.tatar.ru/",
         }
    # url = "https://edu.tatar.ru/upload/storage/org1505/files/" + target_folder + '/'
    # url = "https://edu.tatar.ru/js/ckfinder/core/connector/php/connector.php?command=FileUpload&type=Files&currentFolder=/food/&hash=cc921cf4d95e67d0&langCode=ru"
    url = f"https://edu.tatar.ru/js/ckfinder/core/connector/php/connector.php"
    params = {'command': 'FileUpload',
              'type': 'Files',
              'currentFolder': f"/{target_folder}/",
              # 'hash': 'cc921cf4d95e67d0', # эти параметрыо казались не обязательными... вроде
              # 'langCode': 'ru'
              }
    f = []
    # for file in files:
    f.append(session.post(url=url,
                          headers=h,
                          params=params,
                          files=files, proxies=proxy))
    print(f)
    pprint(f)

    return f


def post_page(session, link_to_the_page_food, data, proxy, link_to_the_folder_food):
    link_to_the_folder_food_ = "/".join(link_to_the_folder_food.split("/")[3:8])
    organization_id = link_to_the_folder_food.split("/")[5][3:7]


    session.get('https://edu.tatar.ru')
    url = link_to_the_page_food
    h = {"Referer": url,
         "Content-Type": "application/x-www-form-urlencoded"}
    r = session.get(url)
    html = BeautifulSoup(r.text, 'html.parser')
    file_links = ''
    for file in data:
        file_links = f'<p><a href="{link_to_the_folder_food_}/{file[0]}">{file[0]}</a></p>\n' + file_links
    text = file_links  # + str(html.find_all('textarea', id='simple_page_data')[-1].contents[-1])
    print("text")
    pprint(text)
    r = session.post(url=url, headers=h,
                     data={'simple_page[title]': 'Ежедневные Меню',
                           'simple_page[description]': '',
                           'simple_page[data]': text,
                           'simple_page[organization_id]': organization_id}, proxies=proxy
                     )
    print(r)
    return r


def get_files(session, link_to_the_folder_food,  from_folder='food'):
    link_to_the_folder_food = "/".join(link_to_the_folder_food.split("/")[:7])
    print(link_to_the_folder_food)
    url = "https://edu.tatar.ru/js/ckfinder/core/connector/php/connector.php"
    params = {'command': 'GetFiles',
              'type': 'Files',
              'currentFolder': f'/{from_folder}/',
              # 'hash': 'cc921cf4d95e67d0',
              # 'showThumbs': 1,
              # 'langCode': 'ru'
              }
    res = session.get(url, params=params)
    print("res")
    pprint(res)
    from xml.etree import ElementTree
    files = ElementTree.fromstring(res.content).findall('Files')[0].findall('File')
    files_list = []
    for file in files:
        filename = file.get('name')
        files_list.append(
            (filename, '/'.join([link_to_the_folder_food, from_folder, filename])))
    print("file_list")
    pprint(files_list)
    return files_list
