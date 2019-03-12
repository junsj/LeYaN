import os
import re
import urllib
import urllib.request
from bs4 import BeautifulSoup
import sqlite3
import datetime

from PIL import Image
import socket

socket.setdefaulttimeout(10)

class Htmls():
  def __init__(self,url,decode='utf-8'):
    self.url = url
    self.decode = decode

  def get_single_page(self):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    response = urllib.request.Request(url=self.url, headers=headers)
    html = urllib.request.urlopen(response,timeout=20).read().decode(self.decode,'ignore')
    soup = BeautifulSoup(html,"html.parser")
    return soup

'''
===================================================================================================
| Class: Lofter                                                                                   |  
| Author: ZhouJun 2016.12                                                                         | 
|                                                                                                 |
|                                                                                                 |
===================================================================================================
'''

class Lofter():
  def __init__(self,url,d2='files\\',decode='utf-8'):
    self.url = url
    self.rooturl = 'http://' + urllib.parse.urlparse(url).netloc
    self.album   = urllib.parse.urlparse(url).netloc
    self.download_to = d2 + self.album
    self.makedirs = False
    # self.album_id = self.album_idx()

  def get_pages(self,url):
    soup = Htmls(url).get_single_page()
    soup_div = soup.findAll("div",{"class":re.compile("(link)|(image)|(pic)")})
    pages = re.compile(r'.*href="(.*?)"').findall(str(soup_div))
    pages = list(set(pages))
    nextpage = re.compile(r'.*href="(.*?)".*下一页.*').findall(str(soup))
    if nextpage == []:
      nextpage = ''
    else:
      nextpage = nextpage[0]
      nextpage = self.rooturl + '/' + nextpage
    return pages,nextpage

  def all_pages(self):
    l_url = self.url
    all_pages = []
    while not l_url == '':
      try:
        pages,nextpage = self.get_pages(l_url)
        all_pages = all_pages + pages
        l_url = nextpages
      except:
              l_url = ''
    return all_pages

  def one_page(self,url):
    soup = Htmls(url).get_single_page()
    soup_div = soup.findAll("div",{"class":re.compile("(img)|(image)|(pic)")})
    images = re.compile(r'bigimgsrc="(http://.*?.jpg).*?').findall(str(soup_div))

    soup_div = soup.findAll("div",{"class":re.compile("(text)")})
    texts = ''
    for div_text in soup_div:
      texts = str(div_text.get_text()) + '|' + texts

    rstr = r"[\/\\\:\*\?\"\<\>\n]"
    texts = re.sub(rstr, "", texts)
    
    return images,texts

  def download_one_page(self,url,dn='X'):
    images,texts = self.one_page(url)
    
    if not self.makedirs:
      if not os.path.exists(self.download_to):
        os.makedirs(self.download_to)
        self.makedirs = True

    pics = []
    for image in images:
        try:
            img1,img2 = os.path.split(image)
            filename = self.download_to + '\\' + img2 
            if not os.path.exists(filename):
              if dn == 'X' or dn == 'x':
                urllib.request.urlretrieve(image,filename)
                print('Download Image:',image)
            pic_name      = img2
            pic_url       = image
            pic_album_id  = ''
            pic_pixs      = ''
            pic_create_at = datetime.datetime.now()
            pic_sort_key  = ''
            pic_text      = texts
            pic = (pic_name,pic_url,pic_album_id,pic_pixs,pic_create_at,pic_sort_key,pic_text)
            pics.append(pic)                       
        except:
            print('@-@,Download Image Fail:',image)
    return pics

  def __del__(self):
    pass

'''
===================================================================================================
| Class: Fireworks                                                                                |  
| Author: ZhouJun 2016.12                                                                         | 
|                                                                                                 |
|                                                                                                 |
===================================================================================================
'''
class Fireworks():
    def __init__(self,path='',pos=(640,402),d2='',db=None):
      self.path = path
      self.download_to = d2
      self.xpos = pos[0]
      self.ypos = pos[1]
      self.pixs = str(self.xpos) + 'x' + str(self.ypos)
      self.outpath = self.make_outpath(path)
      self.db = self.connect_db(db)
      self.im = None


    def connect_db(self,db):
      if not db == None: 
        self.cx = sqlite3.connect(db)
        self.cu = self.cx.cursor()
        return True
      else:
        return False      

    def make_outpath(self,path):
      outpath = path + '\\' + str(self.xpos) + 'x' + str(self.ypos)
      if not os.path.exists(outpath):
        os.makedirs(outpath)
      return outpath

    def get_db_images(self):
      if self.db == True:
        pass

    def all_images(self,source='L'):
      source = source.upper()
      if source == 'L':
        pics = os.listdir(self.path)
      elif source == 'D':
        pass        
      else:
        pics = []
      return pics

    def process_images(self):
      pics = self.all_images()
      pics_list = []
      for pic in pics:
          try:
            picname = self.path + '\\' + pic
            self.im = self.open_image(picname)
            if not self.im == None:
              hsize,vsize = self.convert_size(picname)
              convert_file = self.convert_file(pic,hsize,vsize)
              if not convert_file == False:
                pics_list.append(convert_file)
          except:
            print('Convert File Error-->',pic)
      return pics_list

    def open_image(self,picname):
      im = None
      if os.path.isfile(picname):
        im = Image.open(picname)
        return im
    
    def convert_size(self,picname):
            
      hsize,vsize = self.im.size
      if hsize >= vsize:
          vsize1 = self.ypos
          t = self.ypos / vsize
          hsize1 =  hsize * t
      else:
          hsize1 = self.xpos
          t = self.xpos / hsize
          vsize1 = vsize * t
      hsize1 = int(hsize1)
      vsize1 = int(vsize1)
      return hsize1,vsize1

    def convert_file_box(self,hsize,vsize):
      lpos = (hsize - self.xpos) / 2
      tpos = (vsize - self.ypos) / 2
      rpos = lpos + self.xpos
      upos = tpos + self.ypos
      box = (int(lpos),int(tpos),int(rpos),int(upos)) 
      return box,hsize,vsize
      
    def convert_file(self,pic,hsize,vsize):
      box = ''
      outpicname = None
      if hsize > vsize and 0 <= hsize - self.xpos < 30:
        box,hsize,vsize = self.convert_file_box(hsize,vsize)

      elif hsize > vsize and hsize - self.xpos < 0:
        hsize = self.xpos
        box,hsize,vsize = self.convert_file_box(hsize,vsize)

      if hsize < vsize:
        if vsize - self.ypos <= 20:
          vsize = self.ypos
          box,hsize,vsize = self.convert_file_box(hsize,vsize)
        elif 20 < vsize - self.ypos < 50:
          box,hsize,vsize = self.convert_file_box(hsize,vsize)

      if not box == '':   
        out = self.im.resize((hsize,vsize))
        out = out.crop(box)
        outpicname = self.outpath + '\\' + pic 
        out.save(outpicname,quality=100)
        print('Save File to-->',outpicname)
        return pic
      else:
        return False

    def update_db_leyan(self,pic_list):
      print(self.db)
      if self.db:
        for pic in pic_list:
         
          update_content = (self.pixs,pic)   
          update = self.cu.execute("update website_pics set pixs = ? where name = ?",update_content)
          self.cx.commit()

     

db = r'D:\leyan\leyan.db'

path = r'files\zhaofangfang.lofter.com'

p = Fireworks(path,(640,402),db=db)
pic_list = p.process_images()
p.update_db_leyan(pic_list)

