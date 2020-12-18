import urllib2, easygui, time
serverIP = easygui.enterbox("Please enter the IP address of your printer (eg. 000.000.00.00):","3D Printer WiFi Admin")
serverIP = str(serverIP)
serverIP = "http://" + serverIP
chs = ["EXIT","Home","Dance","Unlock","Go to center"]
def main():
    ans = easygui.buttonbox("Select an action:","3D Printer WiFi Admin",chs)
    if ans == "Home":
        urllib2.urlopen(serverIP + "/set?code=G28%20X%20Y")
        time.sleep(5)
        urllib2.urlopen(serverIP + "/set?code=G28%20Z")
        main()
    if ans == "Dance":
        urllib2.urlopen(serverIP + "/set?code=G02%20X60Y60%20I0J-20.0")
        urllib2.urlopen(serverIP + "/set?code=G02%20X60Y60%20I0J-20.0")
        urllib2.urlopen(serverIP + "/set?code=G02%20X60Y60%20I0J-20.0")
        urllib2.urlopen(serverIP + "/set?code=G02%20X60Y60%20I0J-20.0")
        urllib2.urlopen(serverIP + "/set?code=G02%20X60Y60%20I0J-20.0")
        main()


if __name__ == "__main__":
    main()