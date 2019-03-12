from class_pics import Lofter

import sqlite3
import datetime

def connect_db(db=None):
    cx = False
    cu = False
    if not db == None:
        cx = sqlite3.connect(db)
        cu = cx.cursor()
    return cx,cu

def get_album_id(album,source,insert='X'):
    record = cu.execute("select * from website_albums where name=?",(album,)).fetchall()
    if record == []:
        if insert == 'X' or insert == 'x':
          album_name = album
          album_source = source
          album_description = ''
          album_group = ''
          album_create_at = datetime.datetime.now()

          album_content = (album_name,album_source,album_description,album_group,album_create_at)
          insert = cu.execute("insert into website_albums(name,source,description,group_id,create_at) values(?,?,?,?,?)",album_content)
          cx.commit()
          record = cu.execute("select * from website_albums where name=?",(album,)).fetchall()          
    try:
      album_id = record[0][0]
    except:
      album_id = None
    return album_id

def insert_one_page(pics,album_id):
    for pic in pics:
        pic_name        = pic[0]
        pic_url         = pic[1]
        pic_album_id    = album_id
        pic_pixs        = pic[3]
        pic_create_at   = pic[4]
        pic_sortkey     = pic[5]
        pic_text        = pic[6]
        pic = (pic_name,pic_url,pic_album_id,pic_pixs,pic_create_at,pic_sortkey,pic_text)

##        delete_pic = cu.execute("delete from website_pics where name = ?",(pic[0],))
##        insert_pic = cu.execute("insert into website_pics(name,url,album_id,pixs,create_at,sortkey,text) values(?,?,?,?,?,?,?)",pic)
##        cx.commit()
        try:
            delete_pic = cu.execute("delete from website_pics where name = ?",(pic[0],))
        except:
            pass
        try:
            insert_pic = cu.execute("insert into website_pics(name,url,album_id,pixs,create_at,sortkey,text) values(?,?,?,?,?,?,?)",pic)
            cx.commit()
        except:
            print('Insert DB Error--->',pic)    

def process_lofter_pics(url):
    lofter = Lofter(url)
    album_id = get_album_id(lofter.album,lofter.rooturl)
    while not url == '':
        print('='*80)
        print('|','开始处理:',url)
        print('='*80)
        pages,nextpage = lofter.get_pages(url)
        url = nextpage
        for page_url in pages:
            pics = lofter.download_one_page(page_url)
            if not cx == False:
                insert_one_page(pics,album_id)


url = 'http://zhaofangfang.lofter.com'
db = 'leyan.db'
d2 = r'files\\'

cx,cu = connect_db(db)
process_lofter_pics(url)
cx.close()




