
mbpro_list = ["", "Macbook Pro 13 inch ", "Macbook Pro 16 inch "]
mbair_list = ["", "Macbook Air "]
imac_list = ["", "iMac 21.5 inch ", "iMac 27 inch "]
ipad_list = ["", "iPad Pro 11 inch ", "iPad Pro 12.9 inch ", "iPad Air ", "iPad Mini "]
iphn_list = ["", "iPhone 11 Pro ", "iPhone 11 Pro Max ", "iPhone 11 "]
acc_list = ["", "USB Adapter ", "Magic Mouse 2 ", "Magic Trackpad 2 ", "Air Pods Pro ",
            "Macbook Air and Macbook Pro 13 inch leather sleeve ",
            "Macbook Air and Macbook Pro 16 inch leather sleeve "]

mbpro_spec_list = ["", "256 GB SSD / 8 GB 2133MHz LPDDR3 memory ",
                   "512 GB SSD / 8 GB 2133MHz LPDDR3 memory ",
                   "512 GB SSD / 16 GB 3733MHz LPDDR4X memory ",
                   "1 TB SSD / 16 GB 3733MHz LPDDR4X memory"]
mbair_spec_list = ["", "256 PCle SSD / 8GB 3733MHz LPDDR4X memory ",
                   "512 PCle SSD / 8GB 3733MHz LPDDR4X memory "]
imac_spec_list = ["", "3.6GHz quad‑core Intel Core i3 ",
                  "3.0GHz 6-core Intel Core i5 (Turbo Boost up to 4.1GHz) "]
ipad_spec_list = ["", "256 GB / Wi-Fi ",
                  "256 GB / Wi-Fi + Cellular ", ]
iphn_spec_list = ["", "128 GB ", "256 GB ", "512 GB "]

mbpro_price_list = ["", "[$1299] ", "[$1499] ", "[$1799] ", "[$1999] "]
mbair_price_list = ["", "[$999] ", "[$1299] "]
imac_price_list = ["", "[$1599] ", "[$2299] "]
ipad_price_list = ["", "[$799] ", "[$999] ", "[$1399] ", "[$1649] "]
iphn_price_list = ["", "[$999] ", "[$1299] ", "[$1499] ", "[$2349] "]
acc_price_list = ["", "[$19] ", "[$99] ", "[$149] ", "[$249] ", "[$179] ", "[$259] "]

print("Welcome to www.my-box.com")
print("Indonesia Apple authorized dealer ")
print("")
print("[a.] Macbook ")
print("[b.] iMac ")
print("[c.] iPad ")
print("[d.] iPhone ")
print("[e.] Accessories ")
print("")

while True:
    print("Please enter (alphabet) or type the apple product you want : ")
    choice = input("Enter : ")

    if choice in ('a', 'b', 'c', 'd', 'e'):

        if 'a' in choice:
            print("Macbook : ")
        if 'a' in choice:
            print("- ", mbpro_list[1], mbpro_spec_list[1], mbpro_price_list[1])
            print("- ", mbpro_list[1], mbpro_spec_list[2], mbpro_price_list[2])
            print("- ", mbpro_list[2], mbpro_spec_list[1], mbpro_price_list[3])
            print("- ", mbpro_list[2], mbpro_spec_list[2], mbpro_price_list[4])
            print("- ", mbair_list[1], mbair_spec_list[1], mbair_price_list[1])
            print("- ", mbair_list[1], mbair_spec_list[2], mbair_price_list[2])

        if 'b' in choice:
            print("iMac : ")
        if 'b' in choice:
            print("- ", imac_list[1], imac_spec_list[1], imac_price_list[1])
            print("- ", imac_list[2], imac_spec_list[2], imac_price_list[2])

        if 'c' in choice:
            print("iPad : ")
        if 'c' in choice:
            print("- ", ipad_list[1], ipad_spec_list[1], ipad_price_list[2])
            print("- ", ipad_list[1], ipad_spec_list[2], ipad_price_list[3])
            print("- ", ipad_list[2], ipad_spec_list[1], ipad_price_list[3])
            print("- ", ipad_list[2], ipad_spec_list[2], ipad_price_list[4])
            print("- ", ipad_list[3], ipad_spec_list[1], ipad_price_list[1])
            print("- ", ipad_list[3], ipad_spec_list[2], ipad_price_list[2])
            print("- ", ipad_list[4], ipad_spec_list[1], ipad_price_list[2])
            print("- ", ipad_list[4], ipad_spec_list[2], ipad_price_list[3])

        if 'd' in choice:
            print("iPhone : ")
        if 'd' in choice:
            print("- ", iphn_list[1], iphn_spec_list[2], iphn_price_list[2])
            print("- ", iphn_list[1], iphn_spec_list[3], iphn_price_list[3])
            print("- ", iphn_list[2], iphn_spec_list[2], iphn_price_list[3])
            print("- ", iphn_list[2], iphn_spec_list[3], iphn_price_list[4])
            print("- ", iphn_list[3], iphn_spec_list[1], iphn_price_list[1])

        if 'e' in choice:
            print("Accessories : ")
        if 'e' in choice:
            print("- ", acc_list[1], acc_price_list[1])
            print("- ", acc_list[2], acc_price_list[2])
            print("- ", acc_list[3], acc_price_list[3])
            print("- ", acc_list[4], acc_price_list[4])
            print("- ", acc_list[5], acc_price_list[5])
            print("- ", acc_list[6], acc_price_list[6])
            input("Enter : ")

    if choice in ('macbook', 'imac', 'ipad', 'iphone', 'accessories'):

        if "macbook" in choice:
            print("Result for " + choice, ":")
            print("- ", mbpro_list[1], mbpro_spec_list[1], mbpro_price_list[1])
            print("- ", mbpro_list[1], mbpro_spec_list[2], mbpro_price_list[2])
            print("- ", mbpro_list[2], mbpro_spec_list[1], mbpro_price_list[3])
            print("- ", mbpro_list[2], mbpro_spec_list[2], mbpro_price_list[4])
            print("- ", mbair_list[1], mbair_spec_list[1], mbair_price_list[1])
            print("- ", mbair_list[1], mbair_spec_list[2], mbair_price_list[2])

        if 'imac' in choice:
            print("Result for " + choice, ":")
            print("- ", imac_list[1], imac_spec_list[1], imac_price_list[1])
            print("- ", imac_list[2], imac_spec_list[2], imac_price_list[2])

        if 'ipad' in choice:
            print("Result for " + choice, ":")
            print("- ", ipad_list[1], ipad_spec_list[1], ipad_price_list[2])
            print("- ", ipad_list[1], ipad_spec_list[2], ipad_price_list[3])
            print("- ", ipad_list[2], ipad_spec_list[1], ipad_price_list[3])
            print("- ", ipad_list[2], ipad_spec_list[2], ipad_price_list[4])
            print("- ", ipad_list[3], ipad_spec_list[1], ipad_price_list[1])
            print("- ", ipad_list[3], ipad_spec_list[2], ipad_price_list[2])
            print("- ", ipad_list[4], ipad_spec_list[1], ipad_price_list[2])
            print("- ", ipad_list[4], ipad_spec_list[2], ipad_price_list[3])

        if 'iphone' in choice:
            print("Result for " + choice, ":")
            print("- ", iphn_list[1], iphn_spec_list[2], iphn_price_list[2])
            print("- ", iphn_list[1], iphn_spec_list[3], iphn_price_list[3])
            print("- ", iphn_list[2], iphn_spec_list[2], iphn_price_list[3])
            print("- ", iphn_list[2], iphn_spec_list[3], iphn_price_list[4])
            print("- ", iphn_list[3], iphn_spec_list[1], iphn_price_list[1])

        if 'accessories' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[1], acc_price_list[1])
            print("- ", acc_list[2], acc_price_list[2])
            print("- ", acc_list[3], acc_price_list[3])
            print("- ", acc_list[4], acc_price_list[4])
            print("- ", acc_list[5], acc_price_list[5])
            print("- ", acc_list[6], acc_price_list[6])

    if choice in ('macbook pro', 'macbook air', 'ipad pro', 'ipad air', 'ipad mini', 'iphone pro',
                  'iphone 11', 'iphone 11 pro', 'iphone 11 pro max'):

        if 'macbook pro' in choice:
            print("Result for " + choice, ":")
            print("- ", mbpro_list[1], mbpro_spec_list[1], mbpro_price_list[1])
            print("- ", mbpro_list[1], mbpro_spec_list[2], mbpro_price_list[2])
            print("- ", mbpro_list[2], mbpro_spec_list[1], mbpro_price_list[3])
            print("- ", mbpro_list[2], mbpro_spec_list[2], mbpro_price_list[4])

        if 'macbook air' in choice:
            print("Result for " + choice, ":")
            print("- ", mbair_list[1], mbair_spec_list[1], mbair_price_list[1])
            print("- ", mbair_list[1], mbair_spec_list[2], mbair_price_list[2])

        if 'imac' in choice:
            print("Result for " + choice, ":")
            print("- ", imac_list[1], imac_spec_list[1], imac_price_list[1])
            print("- ", imac_list[2], imac_spec_list[2], imac_price_list[2])

        if 'ipad pro' in choice:
            print("Result for " + choice, ":")
            print("- ", ipad_list[1], ipad_spec_list[1], ipad_price_list[2])
            print("- ", ipad_list[1], ipad_spec_list[2], ipad_price_list[3])
            print("- ", ipad_list[2], ipad_spec_list[1], ipad_price_list[3])
            print("- ", ipad_list[2], ipad_spec_list[2], ipad_price_list[4])

        if 'ipad air' in choice:
            print("Result for " + choice, ":")
            print("- ", ipad_list[3], ipad_spec_list[1], ipad_price_list[1])
            print("- ", ipad_list[3], ipad_spec_list[2], ipad_price_list[2])

        if 'ipad mini' in choice:
            print("Result for " + choice, ":")
            print("- ", ipad_list[4], ipad_spec_list[1], ipad_price_list[2])
            print("- ", ipad_list[4], ipad_spec_list[2], ipad_price_list[3])

        if 'iphone 11' in choice:
            print("Result for " + choice, ":")
            print("- ", iphn_list[1], iphn_spec_list[2], iphn_price_list[2])
            print("- ", iphn_list[1], iphn_spec_list[3], iphn_price_list[3])
            print("- ", iphn_list[2], iphn_spec_list[2], iphn_price_list[3])
            print("- ", iphn_list[2], iphn_spec_list[3], iphn_price_list[4])
            print("- ", iphn_list[3], iphn_spec_list[1], iphn_price_list[1])
            print("- ", iphn_list[3], iphn_spec_list[1], iphn_price_list[1])

        if 'iphone pro' in choice:
            print("Result for " + choice, ":")
            print("- ", iphn_list[1], iphn_spec_list[2], iphn_price_list[2])
            print("- ", iphn_list[1], iphn_spec_list[3], iphn_price_list[3])
            print("- ", iphn_list[2], iphn_spec_list[2], iphn_price_list[3])
            print("- ", iphn_list[2], iphn_spec_list[3], iphn_price_list[4])

        if 'iphone 11 pro' in choice:
            print("Result for " + choice, ":")
            print("- ", iphn_list[1], iphn_spec_list[2], iphn_price_list[2])
            print("- ", iphn_list[1], iphn_spec_list[3], iphn_price_list[3])
            print("- ", iphn_list[2], iphn_spec_list[2], iphn_price_list[3])
            print("- ", iphn_list[2], iphn_spec_list[3], iphn_price_list[4])

        if 'iphone 11 pro max' in choice:
            print("Result for " + choice, ":")
            print("- ", iphn_list[2], iphn_spec_list[2], iphn_price_list[3])
            print("- ", iphn_list[2], iphn_spec_list[3], iphn_price_list[4])

    if choice in ('macbook pro 13', 'macbook pro 16'):

        if 'macbook pro 13' in choice:
            print("Result for " + choice, ":")
            print("- ", mbpro_list[1], mbpro_spec_list[1], mbpro_price_list[1])
            print("- ", mbpro_list[1], mbpro_spec_list[2], mbpro_price_list[2])

        if 'macbook pro 16' in choice:
            print("Result for " + choice, ":")
            print("- ", mbpro_list[2], mbpro_spec_list[1], mbpro_price_list[3])
            print("- ", mbpro_list[2], mbpro_spec_list[2], mbpro_price_list[4])

    if choice in ('macbook 13', 'macbook 16'):

        if 'macbook 13' in choice:
            print("Result for " + choice, ":")
            print("- ", mbpro_list[1], mbpro_spec_list[1], mbpro_price_list[1])
            print("- ", mbpro_list[1], mbpro_spec_list[2], mbpro_price_list[2])
            
        if 'macbook 16' in choice:
            print("Result for " + choice, ":")
            print("- ", mbpro_list[2], mbpro_spec_list[1], mbpro_price_list[3])
            print("- ", mbpro_list[2], mbpro_spec_list[2], mbpro_price_list[4])

    if choice in ('usb', 'usb adapter', 'adapter'):

        if 'usb' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[1], acc_price_list[1])
        elif 'usb adapter' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[1], acc_price_list[1])
        elif 'adapter' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[1], acc_price_list[1])

    if choice in ('magic mouse', 'magic mouse 2', 'mouse', 'mouse 2'):

        if 'magic mouse' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[2], acc_price_list[2])
        elif 'magic mouse 2 ' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[2], acc_price_list[2])
        elif 'mouse' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[2], acc_price_list[2])
        elif 'mouse 2' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[2], acc_price_list[2])

    if choice in ('magic trackpad', 'magic trackpad 2', 'trackpad', 'trackpad 2'):
        if 'magic trackpad' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[3], acc_price_list[3])
        elif 'magic trackpad 2' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[3], acc_price_list[3])
        elif 'trackpad' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[3], acc_price_list[3])
        elif 'trackpad 2' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[3], acc_price_list[3])

    if choice in ('air pods', 'air pods pro', 'air pod'):
        if 'air pods' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[4], acc_price_list[4])
        elif 'air pods pro' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[4], acc_price_list[4])
        elif 'air pod' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[4], acc_price_list[4])

    if choice in ('macbook cover', 'macbook case', 'macbook sleeve', 'macbook leather sleeve',
                  'macbook leather cover', ',macbook leather case', 'macbook leather', 'case',
                  'cover'):
        if 'macbook cover' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[5], acc_price_list[5])
        elif 'macbook case' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[5], acc_price_list[5])
        elif 'macbook sleeve' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[5], acc_price_list[5])
        elif 'macbook leather sleeve' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[5], acc_price_list[5])
        elif 'macbook leather cover' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[5], acc_price_list[5])
        elif 'macbook leather case' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[5], acc_price_list[5])
        elif 'macbook leather' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[5], acc_price_list[5])
        elif 'case' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[5], acc_price_list[5])
        elif 'cover' in choice:
            print("Result for " + choice, ":")
            print("- ", acc_list[5], acc_price_list[5])

    if choice not in ('a', 'b', 'c', 'd', 'e', 'macbook', 'macbook pro', 'ipad', 'ipad pro', 'ipad mini', 'iphone',
                      'macbook pro 13', 'macbook pro 16', 'iphone 11', 'iphone 11 pro', 'imac', 'iphone 11 pro max',
                      'accessories', 'usb', 'usb adapter', 'adapter', 'magic mouse', 'magic mouse 2', 'mouse',
                      'mouse 2', 'magic trackpad', 'magic trackpad 2', 'trackpad', 'trackpad 2', 'air pods',
                      'air pods pro', 'air pod', 'macbook cover', 'macbook case', 'macbook sleeve',
                      'macbook leather sleeve', 'macbook leather cover', ',macbook leather case', 'macbook leather',
                      'case', 'cover', 'macbook 13', 'macbook 16'):

        print("We are sorry,", choice, " product is not available.")


