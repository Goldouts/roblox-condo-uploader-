import sys
import time
import random
from requests import post, get
import requests
from os import name as os_name, system
from discord import Webhook, RequestsWebhookAdapter
import codecs
import json
import discord
import secrets
from unblacklister import uniqueId, referentt, assetId
from advertiser import adervrtise
import os
import lxml.etree
import random
from colorama import Fore, Back, Style
from xml.dom import minidom
from xml.etree import ElementTree as etree

def main(cookie):
    uniqueId()
    referentt()
    assetId()
    token = post("https://auth.roblox.com/v2/logout", #logout
                 cookies={
                     ".ROBLOSECURITY": cookie
                 }).headers['X-CSRF-TOKEN']
    userId = requests.get("https://users.roblox.com/v1/users/authenticated",
                          headers={
                              'x-csrf-token': token,
                              'User-Agent': 'Roblox/WinINet',
                                "Connection": "keep-alive"
                          },
                          cookies={
                              '.ROBLOSECURITY': cookie
                          }).json()["id"]
    print(f" [DATA] {userId}- UserID")
    gameId = requests.get("https://inventory.roblox.com/v2/users/" +
                          str(userId) + "/inventory/9?limit=10&sortOrder=Asc",
                          headers={
                              'x-csrf-token': token,
                              'User-Agent': 'Roblox/WinINet'
                          },
                          cookies={
                              '.ROBLOSECURITY': cookie
                          }).json()["data"][0]["assetId"]
    print(f" [DATA] {gameId} - GameID")
    myfiles = open("electro.rbxlx", "rb").read()
    unvid = get(
        "https://api.roblox.com/universes/get-universe-containing-place?placeid="
        + str(gameId)).json()["UniverseId"]
    print(f" [DATA] {unvid} - UniverseID")
    url = f"https://data.roblox.com/Data/Upload.ashx?assetid={str(gameId)}"

    url2 = f"https://develop.roblox.com/v2/universes/{str(unvid)}/configuration"

    avatartype = "MorphToR6"
    allowprivateservers = True

    gamedata = {
        "name": "An Automatic Uploaded Place",
        "description": ". . . . . . . . . . . . . . . . . . . . ",
        "universeAvatarType": avatartype,
        "universeAnimationType": "Standard",
        "maxPlayerCount": 2,
        "allowPrivateServers": allowprivateservers,
        "privateServerPrice": 0,
        "permissions": {
            "IsThirdPartyPurchaseAllowed": True
        }
    }
    gamedata = json.dumps(gamedata)
    gameData = requests.patch(
        url2,
        headers={
            'Content-Type': 'application/json',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'x-csrf-token': token
        },
        cookies={'.ROBLOSECURITY': cookie},
        data=gamedata)
    gameData2 = {
        "maxPlayerCount": 2,
    }
    gameData = requests.patch(
        url2,
        headers={
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'x-csrf-token': token
        },
        cookies={'.ROBLOSECURITY': cookie},
        data=gameData2)

    print(f" [DATA] {gameData.status_code} - Successfull upload")
    upload = post(url,
                  headers={
                      'Content-Type': 'application/xml',
                      'User-Agent': 'Roblox/WinINet', #Roblox
                      'x-csrf-token': token
                  },
                  cookies={'.ROBLOSECURITY': cookie},
                  data=myfiles)
    if upload.status_code == 200:
        webhook = Webhook.from_url(
            "https://discord.com/api/webhooks/952689690367107112/teEhf6_Hmv8fVn9NjoWbwjeGCkla9ZKEILXo4xuEV9NjFs71mcwj-iUlC-9qwrSvsN1l",
            adapter=RequestsWebhookAdapter())
        webhook.send("New Game Uploaded!")
        e = discord.Embed(title="Automatically Uploaded Condo",
        description="2 Player Condos | 🎀 https://discord.gg/AHbmGCMrnP")
        e.add_field(name="Max Players", value="2", inline=True)
        e.add_field(name="Avatar Type", value="R6", inline=True)
        e.add_field(name="Status", value="Playable", inline=True)
        e.add_field(name="Unblacklisted", value="✅", inline=True)
        e.add_field(name="Private Servers",
                    value=":white_check_mark:",
                    inline=True)
        e.add_field(
            name="Game Link",
            value=
            f"[Click here to play!](https://www.roblox.com/games/{gameId}/)",
            inline=True)
        e.set_thumbnail(
            url=
            'https://cdn.discordapp.com/attachments/934595444070293514/935360125101813831/static.png'
        )
        webhook.send(embed=e)
        adervrtise(gameId)
    while True:
        time.sleep(60)
        cookie2 = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_A8D5F916CE211AF798092DCFF5D2BB971B93F35FB1C162441BE8755443CA395A12E5D643C5CA6CD809542E97453C6274A0A3E6F28E69DDD375BD5FF739681C9B89AD4D301177870F45545377163FCFF9CA42473A2EC79DF4559F08BB7B5162807527222E548646E252CC82ED889487CFBEFB906D5CF2596100D21339BB6B9DCAF40CEDC25D37217A04C8A6C4FB9069825D92A059BC06A6351A64C2295ABD1F5E4A396F64F3FD821404E19FBEBF3860B4C30CCB09C1480B7EF17F667C42486A841831D4EDA9E63CCD0F736D8BFA3DABBA0761ED5EC92A69B8CD666ADE202A6A1E213744C29167E59847C7D04CC8BD861CC27BA9967B6E471C968962AED9F1ED29E0E49AB1BA8A44BDEA8B3893B8A9D9BFF01B27B448688C71B101773740C1C749CB0D5C21AD862190CAF179528F31A463F25D488000A459B7F0AD903C97F0039B57800FA7C93A0F13C8948A4BCAB37F377B7D7239"
        sheesh = get(f"https://games.roblox.com/v1/games/multiget-playability-status?universeIds={unvid}",headers={'x-csrf-token': token,'User-Agent': 'Roblox/WinINet'},cookies={'.ROBLOSECURITY': cookie2 }).json()
        sheesh = sheesh[0]['playabilityStatus']
        if sheesh == 'UnderReview':
            def start():
                k = 1
                filename = 'cookies.txt'
                with open(filename) as file:
                    lines = file.read().splitlines()

                if len(lines) > k:
                    random_lines = random.sample(lines, k)
                    with open(filename, 'w') as output_file:
                        output_file.writelines(line + "\n"
                        for line in lines if line not in random_lines)
                    main("\n".join(random_lines))
                elif lines: # file is too small
                    print("\n".join(lines)) # print all lines
                    with open(filename, 'wb', 0): # empty the file
                                pass 
                

            start()

if __name__ == "__main__":
    clear = lambda: system('cls')
    def sendmsg():
        clear()
        print(Fore.RED + '''                                                                     
            ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗
            
                                                 Xavi's...
                     ▒█▀▀█ ▒█▀▀▀█ ▒█▄░▒█ ▒█▀▀▄ ▒█▀▀▀█ 　 ▒█░▒█ ▒█▀▀█ ▒█░░░ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀▄ ▒█▀▀▀ ▒█▀▀█ 
                     ▒█░░░ ▒█░░▒█ ▒█▒█▒█ ▒█░▒█ ▒█░░▒█ 　 ▒█░▒█ ▒█▄▄█ ▒█░░░ ▒█░░▒█ ▒█▄▄█ ▒█░▒█ ▒█▀▀▀ ▒█▄▄▀ 
                     ▒█▄▄█ ▒█▄▄▄█ ▒█░░▀█ ▒█▄▄▀ ▒█▄▄▄█ 　 ░▀▄▄▀ ▒█░░░ ▒█▄▄█ ▒█▄▄▄█ ▒█░▒█ ▒█▄▄▀ ▒█▄▄▄ ▒█░▒█
                                        Making Condos Easier for everyone
                             
                                         [1] Unblacklist/Unpatch         [2] Upload Condo 
               v6.0.0                                                                           Remake by Bannable
            ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════╝

        ''')
        input22 = input(" \n    Enter Task (1 or 2):  ")
        if input22 == "2":
           stuff = input("Please Insert Account Cookie: ")
           main(stuff)
           time.sleep(1)
           sendmsg()
        elif input22 == "1":
            referentt()
            uniqueId()
            assetId()
            print("\n Successfully unblacklisted map")
            time.sleep(1)
            sendmsg()
        elif input22 == "3":
            req = requests.Session()
            cookiefilefolder = os.path.dirname(__file__)
            cookiefile = (cookiefilefolder + "\cookies.txt")
            cookie = open(cookiefile).read().splitlines()
            validcount = 0
            invalidcount = 0

            if len(cookie) > 0:
                print(str(len(cookie)) + " Cookie(s) Found")
                print(" ")
                for line in cookie:
                    check = req.get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(line)})
                    if check.status_code == 200:
                        validcount += 1
                    else:
                        invalidcount += 1
                print(" Valid Cookie(s): " + str(validcount) + "\n [Reborn] Invalid Cookie(s):" + str(invalidcount))
                time.sleep(5)
                sendmsg()

            else:
                print(" No cookies found.")

    sendmsg()
