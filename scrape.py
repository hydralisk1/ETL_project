from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

# scrape past rocket launches from https://nextspaceflight.com/launches/past/
def scrape_past():
    executable_path = {"executable_path":"d:/chrome_driver/chromedriver.exe"}
    url = "https://nextspaceflight.com/launches/past/"
    browser = Browser("chrome", **executable_path, headless=False)
    browser.visit(url)
    time.sleep(1)

    # Set a list to store scraped data
    db = []
    remaining_page = True

    # Loop until the last page
    while(remaining_page):
        html = browser.html
        soup = bs(html, "html.parser")
        
        # Scrape organization names
        org = soup.find_all("span", style="color: black")
        # Scrape rocket names and missions
        ro_lv = soup.find_all("h5", class_="header-style")
        # Scrape times launched and locations
        etc = soup.find_all("div", class_="mdl-card__supporting-text")
        # Scrape if it was successful or not
        success = soup.find_all("div", class_="mdl-cell mdl-cell--6-col")
        
        for i in range(len(org)):
            # If border color is #7ED47E, it was succeeded. If not, it was failed or partially failed. I'll regard partially failed missions also as failed.
            suc = True if success[i].div["style"].replace("border-color:\n\t\t\t\t\n\t                ", "").split(";")[0] == "#7ED47E" else False
            # Cleaning data and store into the list
            db.append({"Organization":org[i].text.split("\n\t")[1].replace(" ", ""),
                       "Rocket":ro_lv[i].text.split(" | ")[0].replace("\n                    ", ""),
                       "Mission":[mission for mission in ro_lv[i].text.split(" | ")[1].replace("\n                ", "").split(" (")[0].replace(" & ", ", ").split(", ")],
                       "Time":etc[i].text.split("\n")[3].replace("                                ", ""),
                       "Location":etc[i].text.split("\n")[6].replace("                        ", ""),
                       "Success": suc
                       })
        
        # If there's a next button, click the next button to get to the next page. If not, stop looping because this page is the last page.
        if browser.is_text_present("NEXT"):
            # Next button must be on the first or on the third
            if browser.find_by_css("button[class='mdc-button mdc-button--raised']").first.text == "NEXT":
                browser.find_by_css("button[class='mdc-button mdc-button--raised']").first.click()
            else:
                browser.find_by_css("button[class='mdc-button mdc-button--raised']")[2].click()
        else:
            remaining_page = False

    browser.quit()

    return db

def scrape_upcoming():
    executable_path = {"executable_path":"d:/chrome_driver/chromedriver.exe"}
    url = "https://nextspaceflight.com/launches/"
    browser = Browser("chrome", **executable_path, headless=False)
    browser.visit(url)
    time.sleep(1)

    # Set a list to store scraped data
    db = []
    remaining_page = True

    # Loop until the last page
    while(remaining_page):
        html = browser.html
        soup = bs(html, "html.parser")
        
        # Scrape organization names
        org = soup.find_all("span", style="color: black")
        # Scrape rocket names and missions
        ro_lv = soup.find_all("h5", class_="header-style")
        # Scrape times launched and locations
        etc = soup.find_all("div", class_="mdl-card__supporting-text")
        
        for i in range(len(org)):
            # Cleaning data and store into the list
            db.append({"Organization":org[i].text.split("\n\t")[1].replace(" ", ""),
                       "Rocket":ro_lv[i].text.split(" | ")[0].replace("\n                    ", ""),
                       "Mission":[mission for mission in ro_lv[i].text.split(" | ")[1].replace("\n                ", "").split(" (")[0].replace(" & ", ", ").split(", ")],
                       "Time":etc[i].text.split("\n")[2].replace("                            ", ""),
                       "Location":etc[i].text.split("\n")[4].replace("                        ", "")
                       })
        
        # If there's a next button, click the next button to get to the next page. If not, stop looping because this page is the last page.
        if browser.is_text_present("NEXT"):
            # Next button must be on the first or on the third
            if browser.find_by_css("button[class='mdc-button mdc-button--raised']").first.text == "NEXT":
                browser.find_by_css("button[class='mdc-button mdc-button--raised']").first.click()
            else:
                browser.find_by_css("button[class='mdc-button mdc-button--raised']")[2].click()
        else:
            remaining_page = False

    browser.quit()

    return db

def scrape_rocket():
    executable_path = {"executable_path":"d:/chrome_driver/chromedriver.exe"}
    url = "https://nextspaceflight.com/rockets/"
    browser = Browser("chrome", **executable_path, headless=False)
    browser.visit(url)
    time.sleep(1)

    # Set a list to store scraped data
    db = []
    remaining_page = True

    while(remaining_page):
        html = browser.html
        soup = bs(html, "html.parser")
        
        # Scrape rocket names
        rockets = soup.find_all("span", style="color: black")
        # Scrape manufacturer names and the other data
        org = soup.find_all("div", class_="mdl-grid a", style="margin: -20px")
        
        for i in range(len(rockets)):
            # Cleaning data and store into a dictionary
            my_dict = {"Name":rockets[i].text.replace("\n                                ", "").replace("\n                            ", "")}
            my_dict["Manufacturer"] = org[i].text.split("\n")[1]
            # Store the other data
            for data in org[i].text.split("\n")[2:]:
                if data != "":
                    my_dict[data.split(": ")[0]] = data.split(": ")[1]
            db.append(my_dict)

        # If there's a next button, click the next button to get to the next page. If not, stop looping because this page is the last page.
        if browser.is_text_present("NEXT"):
            # Next button must be on the first or on the third
            if browser.find_by_css("button[class='mdc-button mdc-button--raised']").first.text == "NEXT":
                browser.find_by_css("button[class='mdc-button mdc-button--raised']").first.click()
            else:
                browser.find_by_css("button[class='mdc-button mdc-button--raised']")[2].click()
        else:
            remaining_page = False

    browser.quit()

    return db