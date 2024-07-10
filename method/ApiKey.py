import random, platform, base64, re, requests, os, urllib, sys, time

P = "\033[97m"
I = "\033[30m"
A = "\033[90m"
H = "\033[32m"
K = H
M = "\x1b[1;91m"
K2 = "\033[33m"

class UserKey:

   def __init__(self) -> None:
       pass

   def konfirkeys(self):
       from datetime import date, datetime
       if os.path.isfile('data/.keys.txt') is True:
          try:
              self.mmk  = open('data/.keys.txt','r').read()
              self.cari = requests.get('https://paste.tc/raw/licensu-64').text
              self.kunci = re.findall(self.mmk+'.*', self.cari)[0]
              self.data_exp = self.kunci.split('|')[2]
              hari,bulan,tahun = self.data_exp.split('-')
              self.sisa = date(int(tahun),int(bulan),int(hari))
              self.ptim = datetime.strptime(str(self.sisa),"%Y-%m-%d")
              self.xtim = datetime.strptime('%s%s%s'%(datetime.now().day,datetime.now().month,datetime.now().year),'%d%m%Y')
              self.meta = self.ptim - self.xtim
              if self.meta.days <1:
                 os.system('rm -rf data/.keys.txt')
                 print(f'{P}[{K}!{P}] Licensi Anda Sudah Kadarluarsa');time.sleep(3)
                 self.BuyLicen()
              else:
                 if os.path.isfile('data/.join.txt') is True:
                    self.Joined = open('data/.join.txt','r').read()
                 else:self.Joined = None
                 self.dev = base64.b16encode(platform.platform().encode('utf-8')).decode()
                 self.nam = self.kunci.split('|')[1]
                 self.jnd = self.Joined
                 self.exp = self.meta.days
                 return '%s|%s|%s'%(self.nam, self.jnd, self.exp)
          except IndexError:
              self.BuyLicen()
       else:
           self.BuyLicen()

   def BuyLicen(self):
       from datetime import datetime as Date
       os.system('clear' if 'linux' in platform.system().lower() else 'cls')
       self.new = base64.b16encode(platform.platform().encode('utf-8')).decode()
       try:
            self.req = requests.get('https://paste.tc/raw/licensu-64').text
            self.key = re.findall(self.new+'.*', str(self.req))
            if len(self.key) > 0:
               self.abc = 'abcdefghijklmnopwrstuvwxyz'
               self.asc = ''.join(random.choice(self.abc) for i in range(10))
               self.des = '%s%s'%(platform.platform(), self.asc)
               self.dev = base64.b16encode(self.des.encode('utf-8')).decode('utf-8')
            else:
               self.dev = self.new
       except Exception as e:
            exit(f'\n{P}[{K2}!{P}] Kesalahan {e}')
       self.new = Date.now()
       self.mon = 'Januari, Februari, Maret, April, Mei, Juni, Juli, Agustus, September, Oktober, November, Desember'.split(',')
       self.hari, self.bulan, self.tahun = self.new.day, self.mon[self.new.month -1], self.new.year
       self.join = '%s/%s/%s'%(self.hari, self.bulan.replace(' ',''), self.tahun)
       print(f'{P}[{K2}*{P}] Join : {H}{self.join}')
       print(f'{P}[{K2}!{P}] Licensi Kamu : {self.dev}\n')
       print(f'{P}[{K2}!{P}] {K}Kirim Licensi {P}Dan Tunggu Author Konfirmasi!')
       self.un = input(f'{P}[{H}?{P}] Masukan Username {H}Bebas {P}: ')
       while len(self.un) == 0:
           self.un = input(f'{P}[{H}?{P}] Masukan Username LU : ')
       self.xx = urllib.parse.quote(f'{self.dev}|{self.un}')
       os.system(f'xdg-open https://wa.me/+6281221523195?text={self.xx}')
       open('data/.keys.txt','w').write(f'{self.dev}')
       open('data/.join.txt','w').write(f'{self.join}')
       exit(f'\n{P}[{H}!{P}] {H}Jangan Di Run.. Sebelum Author Konfirmasi Licensi Anda\n{P}[{H}!{P}] Jalankan ulang : python {sys.argv[0]}')

#-> Simpel Code By Khamdihi Dev
