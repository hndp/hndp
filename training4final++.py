#[Code]
#[iPhone -]
class iphone:
    def __init__(self, iphonetype, iphonespec, iphoneprice):
        self.iphonetype = iphonetype
        self.iphonespec = iphonespec
        self.iphoneprice = iphoneprice

    def iphone11(self):
        print(self.iphonetype, self.iphonespec, self.iphoneprice)
    def iphone11pro(self):
        print(self.iphonetype, self.iphonespec, self.iphoneprice)
    def iphone11promax(self):
        print(self.iphonetype, self.iphonespec, self.iphoneprice)

iphone11_64 = iphone('iPhone 11', '64 GB Storage / 4 GB Ram', '$799')
iphone11_128 = iphone('iPhone 11', '128 GB Storage / 4 GB Ram', '$999')
iphone11_256 = iphone('iPhone 11', '256 GB Storage / 4 GB Ram', '$1199')
iphone11_512 = iphone('iPhone 11', '512 GB Storage / 4 GB Ram', '$1399')
iphone11pro_64 = iphone('iPhone 11 Pro', '64 GB Storage / 4 GB Ram', '$1199')
iphone11pro_256 = iphone('iPhone 11 Pro', '256 GB Storage / 4 GB Ram', '$1599')
iphone11pro_512 = iphone('iPhone 11 pro', '512 GB Storage / 4 GB Ram', '$1799')
iphone11promax_64 = iphone('iPhone 11 Pro Max', '64gb Storage / 4 GB Ram', '$1399')
iphone11promax_256 = iphone('iPhone 11 Pro Max', '256gb Storage / 4 GB Ram', '$1799')
iphone11promax_512 = iphone('iPhone 11 Pro Max', '512gb Storage / 4 GB Ram', '$1999')

#[Macbook Pro -]
class macbook_pro:
    def __init__(self, macbooktype, macbookspec, macbookprice):
        self.macbooktype = macbooktype
        self.macbookspec = macbookspec
        self.macbookprice = macbookprice

    def mcbpro13(self):
        print(self.macbooktype, self.macbookspec, self.macbookprice)
    def mcbpro16(self):
        print(self.macbooktype, self.macbookspec, self.macbookprice)

mcbpro13_256 = macbook_pro('Macbook Pro 13 inch', '256 GB SSD / 8 GB 2133MHz LPDDR3 memory', '$1399')
mcbpro13_512 = macbook_pro('Macbook Pro 13 inch', '512 GB SSD / 8 GB 2133MHz LPDDR3 memory', '$1599')
mcbpro16_256 = macbook_pro('Macbook Pro 16 inch', '256 GB SSD / 16 GB 3733MHz LPDDR4X memory', '$2599')
mcbpro16_512 = macbook_pro('Macbook Pro 16 inch', '512 GB SSD / 16 GB 3733MHz LPDDR4X memory', '$2799')

#[Macbook Air -]
class macbook_air:
    def __init__(self, macbooktype, macbookspec, macbookprice):
        self.macbooktype = macbooktype
        self.macbookspec = macbookspec
        self.macbookprice = macbookprice

    def mcbair(self):
        print(self.macbooktype, self.macbookspec, self.macbookprice)

mcbair13_256 = macbook_air('Macbook Air 13 inch', '256 PCle SSD / 8GB 3733MHz LPDDR4X memory', '$999')
mcbair13_512 = macbook_air('Macbook Air 13 inch', '512 PCle SSD / 8GB 3733MHz LPDDR4X memory', '$1199')

#[iMac -]
class imac:
    def __init__(self, imactype, imacspec, imacprice):
        self.imactype = imactype
        self.imacspec = imacspec
        self.imacprice = imacprice

    def imac(self):
        print(self.imactype, self.imacspec, self.imacprice)

imac21 = imac('iMac 21.5 inch', '3.6GHz quad‑core Intel Core i3', '$1599')
imac27 = imac('iMac 27 inch', '3.0GHz 6-core Intel Core i5 (Turbo Boost up to 4.1GHz', '$2299')

#[iPad -]
class ipad:
    def __init__(self, ipadtype, ipadspec, ipadprice):
        self.ipadtype = ipadtype
        self.ipadspec = ipadspec
        self.ipadprice = ipadprice

    def ipad(self):
        print(self.ipadtype, self.ipadspec, self.ipadprice)

ipadpro11_wi = ipad('iPad Pro 11 inch', '256 GB / Wi-Fi', '$999')
ipadpro11_wi_cell = ipad('iPad Pro 11 inch', '256 GB / Wi-Fi + Cellular', '$1199')
ipadpro12_wi = ipad('iPad Pro 12.9 inch', '256 GB / Wi-Fi', '$1199')
ipadpro12_wi_cell = ipad('iPad Pro 12.9 inch', '256 GB / Wi-Fi + Cellular', '$1399')

#[Accessories -]
class accessories:
    def __init__(self, acctype, accprice):
        self.acctype = acctype
        self.accprice = accprice

    def acc(self):
        print(self.acctype, self.accprice)
        
usbadapter = accessories('USB Adapter', '$19')
magicmouse2 = accessories('Magic Mouse 2', '$99')
magictrackpad2 = accessories('Magic Trackpad 2', '$99')
airpodspro = accessories('Air Pods Pro', '$249')
mac13sleeve = accessories('Macbook Air and Macbook Pro 13 inch leather sleeve', '$149')
mac16sleeve = accessories('Macbook Air and Macbook Pro 13 inch leather sleeve', '$179')
iph11siliconeblack = accessories('iPhone 11 black silicone case', '$49')
iph11siliconemidblue = accessories('iPhone 11 midnight blue silicone case', '$49')
iph11prosiliconeblack = accessories('iPhone 11 Pro black silicone case', '$49')
iph11prosiliconemidblue = accessories('iPhone 11 Pro midnight blue silicone case', '$49')
iph11promaxsiliconeblack = accessories('iPhone 11 Pro Max black silicone case', '$49')
iph11promaxsiliconemidblue = accessories('iPhone 11 Pro Max midnight blue silicone case', '$49')

#[Display]
print('Welcome to www.my-box.com')
print('Indonesia Apple authorized dealer ')
print('')
print('[a.] iPhone ')
print('[b.] Macbook Pro ')
print('[c.] Macbook Air ')
print('[d.] iMac')
print('[e.] iPad')
print('[f.] Accessories')

print("")

while True:
    print("Please enter (alphabet) or type the apple product: ")
    choice = input("Enter : ")
    print('')

    if choice in ('a', 'b', 'c', 'd', 'e', 'f'):
        if 'a' in choice:
            print('[iPhone]')
            iphone11_64.iphone11()
            iphone11_256.iphone11()
            iphone11_512.iphone11()
            iphone11pro_64.iphone11pro()
            iphone11pro_256.iphone11pro()
            iphone11pro_512.iphone11pro()
            iphone11promax_64.iphone11promax()
            iphone11promax_256.iphone11promax()
            iphone11promax_512.iphone11promax()
            print('')
        elif 'b' in choice:
            print('[Macbook Pro]')
            mcbpro13_256.mcbpro13()
            mcbpro13_512.mcbpro13()
            mcbpro16_256.mcbpro16()
            mcbpro16_512.mcbpro16()
            print('')
        elif 'c' in choice:
            print('[Macbook Air]')
            mcbair13_256.mcbair()
            mcbair13_512.mcbair()
            print('')
        elif 'd' in choice:
            print('[iMac]')
            imac21.imac()
            imac27.imac()
        elif 'e' in choice:
            print('[iPad]')
            ipadpro11_wi.ipad()
            ipadpro11_wi_cell.ipad()
            ipadpro12_wi.ipad()
            ipadpro12_wi_cell.ipad()
            print('')
        elif 'f' in choice:
            print('[Accessories]')
            usbadapter.acc()
            magicmouse2.acc()
            magictrackpad2.acc()
            airpodspro.acc()
            mac13sleeve.acc()
            mac16sleeve.acc()
            iph11siliconeblack.acc()
            iph11siliconemidblue.acc()
            iph11prosiliconeblack.acc()
            iph11prosiliconemidblue.acc()
            iph11promaxsiliconeblack.acc()
            iph11promaxsiliconemidblue.acc()
            print('')

    #[iPhone -]
    if choice in ('iphone', 'iphone11', 'iphone 11'):
        iphone11_64.iphone11()
        iphone11_256.iphone11()
        iphone11_512.iphone11()
        iphone11pro_64.iphone11pro()
        iphone11pro_256.iphone11pro()
        iphone11pro_512.iphone11pro()
        iphone11promax_64.iphone11promax()
        iphone11promax_256.iphone11promax()
        iphone11promax_512.iphone11promax()
    elif choice in ('iphone 11 pro'):
        iphone11pro_64.iphone11pro()
        iphone11pro_256.iphone11pro()
        iphone11pro_512.iphone11pro()
    elif choice in ('iphone pro max'):
        iphone11promax_64.iphone11promax()
        iphone11promax_256.iphone11promax()
        iphone11promax_512.iphone11promax()
    elif choice in ('iphone 11 pro max'):
        iphone11promax_64.iphone11promax()
        iphone11promax_256.iphone11promax()
        iphone11promax_512.iphone11promax()

    #[Macbook -]
    if choice in ('macbook'):
        mcbpro13_256.mcbpro13()
        mcbpro13_512.mcbpro13()
        mcbpro16_256.mcbpro16()
        mcbpro16_512.mcbpro16()
        mcbair13_256.mcbair()
        mcbair13_512.mcbair()
    elif choice in ('macbook pro'):
        mcbpro13_256.mcbpro13()
        mcbpro13_512.mcbpro13()
        mcbpro16_256.mcbpro16()
        mcbpro16_512.mcbpro16()
    elif choice in ('macbook pro 13', 'macbook pro 13 inch'):
        mcbpro13_256.mcbpro13()
        mcbpro13_512.mcbpro13()
    elif choice in ('macbook pro 16', 'macbook pro 16 inch'):
        mcbpro16_256.mcbpro16()
        mcbpro16_512.mcbpro16()
    elif choice in ('macbook air', 'macbook air 13', 'macbook air 13 inch'):
        mcbair13_256.mcbair()
        mcbair13_512.mcbair()

    #[iMac -]
    if choice in ('imac'):
        imac21.imac()
        imac27.imac()
    elif choice in ('imac 21', 'imac 21 inch', 'imac21', 'imac 21.5 inch'):
        imac21.imac()
    elif choice in ('imac 27', 'imac 27 inch', 'imac27', 'imac 27 inch'):
        imac27.imac()

    #[iPad -]
    if choice in ('ipad', 'ipad pro', 'ipadpro'):
        ipadpro11_wi.ipad()
        ipadpro11_wi_cell.ipad()
        ipadpro12_wi.ipad()
        ipadpro12_wi_cell.ipad()
    elif choice in ('ipad pro 11', 'ipadpro11', 'ipad pro 11 inch'):
        ipadpro11_wi.ipad()
        ipadpro11_wi_cell.ipad()
    elif choice in ('ipad pro 12', 'ipadpro12', 'ipad pro 12 inch'):
        ipadpro12_wi.ipad()
        ipadpro12_wi_cell.ipad()

    #[Accessories -]
    if choice in ('accessories', 'apple accessories'):
        usbadapter.acc()
        magicmouse2.acc()
        magictrackpad2.acc()
        airpodspro.acc()
        mac13sleeve.acc()
        mac16sleeve.acc()
        iph11siliconeblack.acc()
        iph11siliconemidblue.acc()
        iph11prosiliconeblack.acc()
        iph11prosiliconemidblue.acc()
        iph11promaxsiliconeblack.acc()
        iph11promaxsiliconemidblue.acc()

    #[Usb / Adapter -]
    if choice in ('usb adapter', 'usb'):
        usbadapter.acc()

    #[Mouse -]
    if choice in ('magicmouse2', 'magic mouse 2', 'magic mouse', 'mouse'):
        magicmouse2.acc()

    #[Trackpad -]
    if choice in ('magictrackpad2', 'magic trackpad', 'magic trackpad 2', 'trackpad', 'trackpad 2'):
        magictrackpad2.acc()

    #[Air Pods -]
    if choice in ('air pods pro', 'air pods', 'air pod'):
        airpodspro.acc()

    #[Macbook acc -]
    if choice in ('macbook sleeve', 'macbook air sleeve', 'macbook pro sleeve'):
        mac13sleeve.acc()
        mac16sleeve.acc()
    elif choice in ('macbook 13 sleeve', 'macbook pro 13 sleeve', 'macbook pro 13 inch sleeve'):
        mac13sleeve.acc()
    elif choice in ('macbook 16 sleeve', 'macbook pro 16 sleeve', 'macbook pro 16 inch sleeve'):
        mac16sleeve.acc()

    #[iPhone case -]
    if choice in ('silicone case', 'iphone case', 'iphone silicone', 'iphone pro case', 'iphone 11 case',
                    'iphone 11 silicone case', 'iphone silicone case'):
        iph11siliconeblack.acc()
        iph11siliconemidblue.acc()
        iph11prosiliconeblack.acc()
        iph11prosiliconemidblue.acc()
        iph11promaxsiliconeblack.acc()
        iph11promaxsiliconemidblue.acc()

    #[iPhone blue case -]
    if choice in ('iphone 11 silicone blue', 'iphone 11 midnight blue', 'iphone 11 midnight blue case'):
        iph11siliconemidblue.acc()
    elif choice in ('iphone 11 pro silicone blue', 'iphone 11 pro blue silicone', 'iphone 11 pro midnight blue'):
        iph11prosiliconemidblue.acc()
    elif choice in ('iphone 11 pro max silicone blue', 'iphone 11 pro max midnight blue',
                    'iphone 11 pro max midnight blue case'):
        iph11promaxsiliconemidblue.acc()

    #[iPhone black case -]
    if choice in ('iphone 11 silicone black', 'iphone 11 black', 'iphone 11 black case',
                  'iphone 11 black silicone'):
        iph11siliconeblack.acc()
    elif choice in ('iphone 11 pro silicone black', 'iphone 11 pro black', 'iphone 11 pro black case',
                    'iphone 11 pro black silicone'):
        iph11prosiliconeblack.acc()
    elif choice in ('iphone 11 pro max silicone black', 'iphone 11 pro max black', 'iphone 11 pro max black case',
                    'iphone 11 pro max black silicone'):
        iph11promaxsiliconeblack.acc()

    if choice not in ('a', 'b', 'c', 'd', 'e', 'f',
                      'iphone', 'iphone11', 'iphone 11',
                      'iphone 11 pro',
                      'iphone pro max', 'iphone 11 pro max',
                      'macbook', 'macbook pro',
                      'macbook pro 13', 'macbook pro 13 inch',
                      'macbook pro 16', 'macbook pro 16 inch',
                      'macbook air', 'macbook air 13', 'macbook air 13 inch',
                      'imac',
                      'imac 21', 'imac 21 inch', 'imac21', 'imac 21.5 inch',
                      'imac 27', 'imac 27 inch', 'imac27', 'imac 27 inch',
                      'ipad', 'ipad pro', 'ipadpro',
                      'ipad pro 11', 'ipadpro11', 'ipad pro 11 inch',
                      'ipad pro 12', 'ipadpro12', 'ipad pro 12 inch',
                      'accessories', 'apple accessories',
                      'usb adapter', 'usb',
                      'magicmouse2', 'magic mouse 2', 'magic mouse', 'mouse',
                      'magictrackpad2', 'magic trackpad', 'magic trackpad 2', 'trackpad', 'trackpad 2',
                      'air pods pro', 'air pods', 'air pod',
                      'macbook sleeve', 'macbook air sleeve', 'macbook pro sleeve',
                      'macbook 13 sleeve', 'macbook pro 13 sleeve', 'macbook pro 13 inch sleeve',
                      'macbook 16 sleeve', 'macbook pro 16 sleeve', 'macbook pro 16 inch sleeve',
                      'silicone case', 'iphone case', 'iphone silicone', 'iphone pro case', 'iphone 11 case',
                      'iphone 11 silicone case', 'iphone silicone case',
                      'iphone 11 silicone blue', 'iphone 11 midnight blue', 'iphone 11 midnight blue case',
                      'iphone 11 pro silicone blue', 'iphone 11 pro blue silicone', 'iphone 11 pro midnight blue',
                      'iphone 11 pro max silicone blue', 'iphone 11 pro max midnight blue',
                      'iphone 11 pro max midnight blue case',
                      'iphone 11 silicone black', 'iphone 11 black', 'iphone 11 black case',
                      'iphone 11 black silicone',
                      'iphone 11 pro silicone black', 'iphone 11 pro black', 'iphone 11 pro black case',
                      'iphone 11 pro black silicone',
                      'iphone 11 pro max silicone black', 'iphone 11 pro max black', 'iphone 11 pro max black case',
                      'iphone 11 pro max black silicone'):

        print("We are sorry,", choice, "is not available.")












