#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import wget
from db import connection, Arm
import re
import os.path
url = "https://web.archive.org/web/20080406035128/http://perso.numericable.fr:80/~briantimms/rolls/charlesF10.htm"


def from_briantimms_detail(url, century, year):
    page = requests.get(url)
    assert page.status_code == 200
    soup = BeautifulSoup(page.content)

    res = soup.select("body > div:nth-of-type(1) > p ")
    cur_arm = None
    for tag in res:
        if cur_arm:
            cur_arm.blazon = tag.text.strip()
            print(cur_arm)
            cur_arm = None
        if tag.img:
            cur_arm = Arm(has_image=True,
                          name=tag.text.splitlines()[-1].strip(),
                          source_url=url,
                          century=century,
                          year=year)
            print(tag.img)
            cur_arm.has_image = True
            # #download image
            cur_arm.source_url = url
    len(res)


def from_briantimms_saved():
    # from https://web.archive.org/web/20080418010451/http://perso.numericable.fr:80/~briantimms/era/armsrollsblazons.htm
    # also see https://web.archive.org/web/20080418010451/http://perso.numericable.fr:80/~briantimms/era/early%20rolls%20of%20arms.htm
    brain_tim_url = "https://web.archive.org/web/20080418010451/http://perso.numericable.fr:80/~briantimms/era/armsrollsblazons.htm"
    roll_map = {
        "H": ("The Falkirk Roll", 1298, "England"),
        "K": ("The Caerlaverock Poem", 1300, "England"),
        "B": ("Glover's Roll", 1240, "England"),
        "C": ("Walford's Roll", 1275,  "England"),
        "D": ("The Camden Roll", 1280, "England"),
        "E": ("St George's Roll", 1285, "England"),
        "F": ("Charles' Roll", 1285, "England"),
        "ST": ("The Stirling Roll", 1304, "England"),
        "GA": ("The Galloway Roll", 1300, "England"),
        "BA": ("The Bigot Roll", 1254, "France"),
        "CP": ("The Chifflet-Prinet Roll", 1285, "France"),
        "VE": ("Vermandois", 1285, "France"),
        "WN": ("The Wijnbergen Roll", 1285, "France"),
        "HE": ("The Heralds' Roll", 1280, "England"),
        "A": ("The Dering Roll", 1370, "England"),
        "Q": ("Collins' Roll", 1296, "England"),
        "LM": ("Lord Marshal's Roll", 1295, "England"),
    }
    filename = os.path.join(os.path.dirname(__file__), 'brian_tim_saved.txt')

    with open(filename) as file:
        lines = file.readlines()
    # Order is <db_id> <blazon> <Name (starts with caps) <roll - number> <roll - number>
    # 2552 Argent a cross cantonned by four mullets gules Thomas de Banbury GA 18 Q 384
    print(len(lines))
    reg = re.compile(
        r"([0-9]+) (?P<blazon>[A-Z][a-z,0\'-9 ]+) (?P<name>[A-zêéèç,ô.â&\-'\s]+)\s+(?P<rolls>([A-Z]+\s+[0-9]+\s*)*)$")
    # now I have two problems
    matches = []
    all_arms = []
    for line in lines:
        if "---" in line or "?" in line:
            continue
        number, rest = line.split(" ", 1)
        match = reg.match(line)
        assert match
        rolls = match.group("rolls")
        for abbrev in rolls.split()[::2]:
            roll = roll_map[abbrev.strip()]
            arms = Arm(
                blazon=match.group('blazon'),
                name=match.group('name'),
                roll=roll[0],
                year=roll[1],
                country=roll[2],
                has_image=False,
                source_url=brain_tim_url,
                source_name="Brian Tim"
            )
            print(len(all_arms))
            print(arms)
            all_arms.append(arms)
            arms.save_to_db()


def from_rietstap_scrape():
    # http://www.coats-of-arms-heraldry.com/armoriaux/rietstap.html
    # This is HUGE
    top_level_urls = [
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_A.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_B.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_C.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_D.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_E.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_F.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_G.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_H.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_I.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_J.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_K.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_L.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_M.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_N.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_O.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_P.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_Q.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_R.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_S.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_T.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_U.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_V.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_W.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_X.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_Y.html",
        "http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/blasons_Z.html"]

    # top_level_urls = top_level_urls[:1]    # cripple 
    links_to_scrape = []
    for url in top_level_urls:
        soup = BeautifulSoup(requests.get(url).content)
        for link in soup.find_all('a', href=True):
            if not link['href'].startswith("blasons_"):
                continue
            print(link['href'])
            links_to_scrape.append("http://www.coats-of-arms-heraldry.com/armoriaux/rietstap/"+link['href'])
    # links_to_scrape = links_to_scrape[:1] # cripple
    total_arms = 0
    for url in links_to_scrape:
        soup = BeautifulSoup(requests.get(url).content)
        blazon_table =  soup.find('tbody').find('tbody')
        if not blazon_table:
                print(f"Couldn't find table on {url}")
                continue
        blaz_rows = blazon_table.findAll('tr')
        for row in blaz_rows:
            try:
                name, blazon = (bl.text for bl in row.findAll('td'))
            except ValueError:
                print(f"Unparsable row: {row} on {url}")
                continue
            arm = Arm(
                blazon=blazon,
                name=name,
                roll="Rietstap General Armorial of Europe",
                year=1861,
                country=None,
                has_image=False,
                source_url=url,
                source_name="Rietstap"
            )  
            total_arms += 1
            # print(arm)
            arm.save_to_db()
    print(total_arms)

# harvest(url, "13", "England")
# from_briantimms_saved()
from_rietstap_scrape()
