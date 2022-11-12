import bs4 as bs
import urllib.request as url
import pandas as pd
import re
import time
names = []
ratings = []
no_reviews = []
specialties_list = []
regions = []
price_ranges = []
authors = []
comments = []
ratings_users = []
dates = []
csv_name="german_61.csv"

def scrape_reviews():
    global review, author_tag, author, comment, rating, date
    for review in reviews:
        author_tag = review.find("a", {"class": "css-1m051bw"})
        author = "Unknown"
        if author_tag is not None:
            author = author_tag.get_text()
            print(author)

        comment = review.find("p", {"class": "comment__09f24__gu0rG css-qgunke"}).get_text()
        print(comment)
        rating = review.find("div", {
            "class": "five-stars__09f24__mBKym five-stars--regular__09f24__DgBNj display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY"})[
            'aria-label'].split()[0]
        print(rating)
        date = review.find("span", {"class": "css-chan6m"}).get_text()
        print(date)
        names.append(name)
        ratings.append(overall_rating)
        no_reviews.append(total_reviews)
        specialties_list.append(specialties)
        regions.append(berlin_region)
        price_ranges.append(price_range)
        authors.append(author)
        comments.append(comment)
        ratings_users.append(rating)
        dates.append(date)
    time.sleep(20.0)
before_hack = ['MA’LOA Hawaiian Poké Bowl', 'Balthazar Spreeufer 2', 'Momiji', 'Bibi Mix','Hängemate', 'Thanh Koch',"Mr. Vertigo","FACTORY GIRL",'Frittenwerk', 'MARS', 'Miss Ploff', 'What a Treat', 'Morsh', 'Käfer', 'Bieberbau', 'L.A. Café', 'Benedict', 'Malakeh', 'BioRestaurant Mandelbaum', 'Café Mori', 'Fünf & Sechzig', 'Kreuzberger Himmel','Thai Tasty', 'Cafe Albrecht', 'Café Frau Schneider', 'YADA YADA breakfast club', 'Bebe Rebozo Steaks & Austern', 'Little Green Rabbit - Gendarmenmarkt', 'Bip', 'NEUMOND', 'Onkel Gustav', 'Kollo’s Inn', 'BLEND Restaurant', 'Black Apron', 'Weimarer Dreieck', 'Pecados - Restaurant', 'Restaurant Vitruv', 'Michelberger Restaurant', 'Burgerwood', 'Tapas y Mas', 'La Tortuga', 'La Lupa E L’ Orso','The Wilson’s', 'Klement’s', 'Avocado Club', 'Hung Anh', 'Club Burger', 'Savanna', 'La Pausa', 'Ali Baba', 'Schäfer', 'MA’LOA','100 Gramm Bar', 'Restaurant Café Madrid', 'phönicia', 'SaDu am Pergamon', 'Sarod’s Thai Restaurant', 'Cou Cou', 'Cantinerie', 'tulus lotrek', 'Zur Haxe', 'Altberliner Restaurant','Gaffel Haus Berlin', 'Cozymazu', 'Skykitchen', 'Southern Vittles', 'Angkor Wat','PeterPaul', 'Ushido', 'Katz Orange', 'Max und Moritz', 'Gogogi','Schnitzelei', 'DT Restaurant', 'Calice d´Oro', 'ULT Ramen', 'Restaurant Nolle','Boulevard Friedrichstrasse', 'Hinterhof', 'Jolly', 'Hans im Glück', 'Habel am Reichs\xadtag','Barcelona Restaurant', 'Maothai Charite', 'La Galleria Italiana', 'Pret A Manger', 'est.','Mani', 'Reinhard Bär', 'Trattoria Su e Giu', 'Pascarella', 'italofritzen','BanhXeo Saigon','Mädchen ohne Abitur', 'Al Letany Insel', 'Petrarca', 'Royals & Rice','Trattoria Peretti', 'Restaurant Bastard', 'Die Berliner Republik', 'Mamas Banh', 'Beirut der 70er','Wellenreiter','Roma', 'Peter Pane', 'Mivadu', 'Les Climats', 'Kin-Za','Thai-Elephant', 'AsiaGourmet', 'Lindengarten','Mogg', 'Otito', 'Trattoria Felice', 'Stranero', 'Gokan','Sofiabar','Zur kleinen Markthalle', 'Midtown Grill', 'Osmans Töchter','Ristorante La Sardegna', 'Eden Restaurant', 'Gasthaus Alt Wien', 'Mitho Cha!', 'Gaststätte Mediterraneo','3 Minutes Sur Mer','Marjan Grill', 'Chay Viet', 'Gaststätte Zum Ritter', 'Fontana Di Trevi', 'Der Everest','Auf der Suche nach dem verlorenen Glück', 'NaNum','Guten Dag', 'Nolas am Weinberg', 'Baraka', 'The Tree', 'Mabuhay','Schwarzwaldstuben','Supreme', 'ma’loa', 'La Focaccia', 'Steakhouse Las Malvinas', 'Ristorante a Mano','Zweistrom', 'Shiso Burger', 'Valle Dei Templi', 'Life Berlin', 'Hausbrauerei Eschenbräu','El Pepe','Hasir Burger', 'Treffpunkt Berlin', 'Focaccia', 'Zen Kitchen', 'Sisaket', 'Aigner Gendarmenmarkt', 'Ristorante Don Giovanni', 'Der Hahn ist tot', 'Restaurant DATA KITCHEN', 'Sucre et Sel','Joseph-Roth-Diele', 'Dehlers','Shikgoo', 'Capital Beach', 'Akito', 'MAISON UMAMI', 'Restaurant Alverdes','Grill Royal', 'Scent Restaurant', 'Aleppo Supper Club','Mezem', 'einsunternull',"Yam Yam","PHO - Noodlebar","Muse",'893 Ryōtei',"Peter Schlemihl","Seaside","Nguyen Kitchen Sushi & More","Feel Seoul Good",'Taverna Ousia', 'Feel Seoul Good', 'Nguyen Kitchen Sushi & More', 'Seaside', 'Peter Schlemihl','L’Osteria', 'Machiavelli', 'Berliner Ensemble Kantine', 'Hopfingerbräu im Palais', 'BraufactuM','Allermunde', 'FAME Katerschmaus', 'Restaurant M', 'Rodolfo’s Tapas Bar', 'Sagrantino 136', 'Ya Karim', 'Das Bonito', 'Son Kitchen', 'Persepolis', 'beets&roots','DaGiorgio’s', 'Mittendrin', 'Schwarze Heidi', 'Chupenga', 'Alt-Berliner Wirtshaus', 'Schlögl’s', 'Kartoffelkeller', 'Tapas Nr. 6','Asteria',"Restaurant im Podewil","El Colmado","Bonfini","Restaurant Van-Long","Cô Chu","A Telha","Cavallino Rosso","Nobelhart & Schmutzig",'Morimori Ramen','Paris-Moskau', 'Wildeküche', 'Restaurant ALvis', 'Muckrakers Pizza','Weingalerie und Café NÖ!', 'Naninka', 'Zille-Stube', 'CHIBEE', 'AmmAmma', 'Chicago Williams BBQ', 'Night Kitchen','Mozzarella & Pomodoro', 'Sotto', 'Layla', 'Fes - Turkish BBQ','Esszimmer','Mr. Hoang', 'Papà Pane di Sorrento', 'momos', 'Porta Nova', 'Sapori di Casa','Dan Thai Food', 'Steel Vintage Bikes Café', 'Tbilisi', 'Taverne Athene','Nôm Nôm Street', 'Restaurant Rossi', 'Amano Bistro', 'Casalot Restaurant',"Osteria bei Pino","Minh San","Republik Berlin","Kapitel 21","Panama","La Casa Buena Vista","LIU 成都味道 Nudelhaus","Mahlzeit Luise","Chipps","Hackethals", "Rotisserie Weingrün","Seoulkitchen","Cana Restaurant","Ständige Vertretung","+84","Good Time",'Dolores', 'Kourosh','Scheers Schnitzel', 'Sabzi', 'Louis Alfons', 'heimlichTreu', 'Historische Gesellschaft', 'Hirsch & Hase', 'Pantry','Uferlos', 'Yarok', 'Spätzle Club', 'Lichtburg', 'Wildes Fräulein', 'Zur Letzten Instanz', 'Lina Bistro & Café',"JOSEPH","Brauereigaststätte Leibhaftig","Elefant","acht&dreissig","Ngon Restaurant Berlin","Stadtklause","Volver", "Marral","Takumi‘9 Sapporo","Schnitzelei Mitte","Zollpackhof","Momotaro Tavern","Boccondivino","Steakhouse Asador",'Supersonico','Birdhouse Imbiss','Dolcini','Gayaya', 'LA BUVETTE Steakhouse', 'Shalimar','DUDU', 'Ristorante Cinque', 'Bejte Ethiopia', 'Cocolo Ramen', 'House of Small Wonder'];
print(str(len(before_hack)))
temp = []
for i in range(0, 131, 10):
    print("Query Param Seite " +str(i))
    site = "https://www.yelp.de"
    source = url.urlopen(site+'/search?find_desc=Restaurants&find_loc=Berlin%2C+Germany&start='+str(i))
    page_soup = bs.BeautifulSoup(source, 'html.parser')
    # header = "Name, Overall Rating, Total_Reviews, Specialty, Region, Price Range"
    # f.write(header)


    restaurants = page_soup.find_all("div", {"class": "container__09f24__mpR8_ hoverable__09f24__wQ_on border-color--default__09f24__NPAKY"})

    for rest in restaurants:
        namediv = rest.find("div", {"class": "businessName__09f24__EYSZE display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY"})

        anchor_tag = namediv.find("a")
        name = anchor_tag.get_text()

        if name not in before_hack and name not in temp:
            print(name + " hasn't yet been scraped . There you go")
            if len(temp) == 20:
                break
            temp.append(name)

            href = anchor_tag.attrs['href']

            print(href)
            # try:
            rating_div = rest.find("div", {"class": "five-stars__09f24__mBKym five-stars--regular__09f24__DgBNj display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY"})
            overall_rating = rating_div.get('aria-label').split()[0]

            print(overall_rating)
            total_reviews_string = rest.find("div", {"class": "display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY"}).get_text()
            split_total_reviews = total_reviews_string.split()
            total_reviews = "".join(c for c in split_total_reviews[0] if c.isdigit())
            print(total_reviews)

            type_and_region = rest.find("div", {"class": "priceCategory__09f24__svarC iaPriceCategory__09f24__GPx_c display--inline-block__09f24__fEDiJ margin-t1__09f24__w96jn border-color--default__09f24__NPAKY"})
            anchortags_specialties = type_and_region.find_all("a")
            specialties = ""
            for a in anchortags_specialties:
                specialties += a.get_text()+ " / "

            berlin_region = type_and_region.find("span", {"class": "css-chan6m"}).get_text()
            print(berlin_region)

            price_range_span = type_and_region.find("span", {"class": "priceRange__09f24__mmOuH css-1s7bx9e"})
            price_range = "";
            if price_range_span is not None:
                print(price_range_span.get_text())
                price_range = str(len(price_range_span.get_text()))
            else:
                print("Unknown price range")
                price_range = "Unknown"

            source = url.urlopen(site + href+"&start=0")
            page_soup = bs.BeautifulSoup(source, 'html.parser')
            reviews = page_soup.find_all("div", {"class": "review__09f24__oHr9V border-color--default__09f24__NPAKY"})

            no_of_pages_div = page_soup.find("div", {"role": "navigation"})
            if no_of_pages_div is None:
                continue
            # if no_of_pages_div is None:
            #     continue
            # if no_of_pages_div is not None:
            # if no_of_pages_div is None:

           # no_of_pages_div2 = page_soup.find("div", {"role": "navigation"})
                # print(no_of_pages_div2.get_text())
                # break
            no_of_pages_div2 = no_of_pages_div.find("div", {
                "class": "border-color--default__09f24__NPAKY text-align--center__09f24__fYBGO"})
            no_of_pages_span = no_of_pages_div2.find("span")
            print("Number of Pages for Comments " + no_of_pages_span.get_text())
            # else:

            print("Pages in Text > " + no_of_pages_span.get_text())
                # print(no_of_pages_div2.get_text())
                # break
            print("Number of Pages for Comments " + no_of_pages_span.get_text())
            list_spans = re.findall(r"\d+", no_of_pages_span.get_text())
            no_of_spans = int(list_spans[1])
            print(type(no_of_spans))
            if no_of_spans == 1:
               print("Only 1 Comment Page > Scraping it")
               scrape_reviews();
            else:
               print("More than 1 comment pages > Scraping page 1" )
               scrape_reviews();
               for curr_comment_page in range(10, ((no_of_spans*10)-9), 10):
                  print("Currently scraping page " + str(curr_comment_page))
                  source = url.urlopen(site + href + "&start="+str(curr_comment_page))
                  page_soup = bs.BeautifulSoup(source, 'html.parser')
                  #no_of_pages_span = page_soup.find("div", {"class": "border-color--default__09f24__NPAKY text-align--center__09f24__fYBGO"}).get_text()
                  reviews = page_soup.find_all("div", {"class": "review__09f24__oHr9V border-color--default__09f24__NPAKY"})
                  scrape_reviews()
                    #time.sleep(20.0)
        else:
            print(name + " has already been scraped. ")
        #time.sleep(20.0)
data = {}
data = {'Restaurant Name': names, 'Overall Rating': ratings, 'Total Reviews': no_reviews, 'Specialty': specialties_list, 'Region': regions, 'Price Range': price_ranges, "Author": authors, "Comment": comments, "Rating": ratings_users, "Date": dates}
header =["Restaurant Name", "Overall Rating", "Total Reviews", "Specialty", "Region", "Price Range", "Author", "Comment", "Rating", "Date"]
print(temp)
rest = pd.DataFrame(data)
rest.to_csv(csv_name, columns = header)


#%%
