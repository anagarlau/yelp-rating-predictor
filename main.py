# mains = page_soup.find_all("div", {"class": "businessName__09f24__EYSZE display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY"})
# main =mains[0]
# restaurant_name = main.find("a").text
# print(restaurant_name)
# restaurant_reviews = page_soup.find_all("div", {"class": "display--inline-block__09f24__fEDiJ margin-t0-5__09f24__gboxT border-color--default__09f24__NPAKY"})
# # print(restaurant_reviews[0].div.get("aria-label"))
# #split, take out ()
# score = restaurant_reviews[0].get_text().split()
# print(score)
# rating_overall = score[0]
# total_no_reviews = "".join(c for c in score[1] if c.isdigit())
# print(rating_overall)
# print(total_no_reviews)
#
# type_and_region = page_soup.find_all("div", {"class": "priceCategory__09f24__svarC iaPriceCategory__09f24__GPx_c display--inline-block__09f24__fEDiJ margin-t1__09f24__w96jn border-color--default__09f24__NPAKY"})
# x = type_and_region[0]
# #get specialties
# specialties = x.find_all("a")
# print(specialties[0].get_text())
# #get region
# region = x.find("span", {"class": "css-chan6m"}).get_text()
# print(region)
#
#
# import bs4 as bs
# import urllib.request as url
# import pandas as pd
# import re
# import time
# names = []
# ratings = []
# no_reviews = []
# specialties_list = []
# regions = []
# price_ranges = []
# authors = []
# comments = []
# ratings_users = []
# dates = []
#
# for i in range(0, 10, 10):
#
#     site = "https://www.yelp.com"
#     source = url.urlopen('https://www.yelp.com/search?find_desc=Restaurants&find_loc=Berlin%2C+Germany&start='+str(i))
#     page_soup = bs.BeautifulSoup(source, 'html.parser')
#     # header = "Name, Overall Rating, Total_Reviews, Specialty, Region, Price Range"
#     # f.write(header)
#
#
#     restaurants = page_soup.find_all("div", {"class": "container__09f24__mpR8_ hoverable__09f24__wQ_on border-color--default__09f24__NPAKY"})
#
#     for rest in restaurants:
#         namediv = rest.find("div", {"class": "businessName__09f24__EYSZE display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY"})
#
#         anchor_tag = namediv.find("a")
#         name = anchor_tag.get_text()
#         href = anchor_tag.attrs['href']
#
#         print(href)
#         # try:
#         rating_div = rest.find("div", {"class": "five-stars__09f24__mBKym five-stars--regular__09f24__DgBNj display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY"})
#         overall_rating = rating_div.get('aria-label').split()[0]
#
#         print(overall_rating)
#         total_reviews_string = rest.find("div", {"class": "display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY"}).get_text()
#         split_total_reviews = total_reviews_string.split()
#         total_reviews = "".join(c for c in split_total_reviews[0] if c.isdigit())
#         print(total_reviews)
#
#         type_and_region = rest.find("div", {"class": "priceCategory__09f24__svarC iaPriceCategory__09f24__GPx_c display--inline-block__09f24__fEDiJ margin-t1__09f24__w96jn border-color--default__09f24__NPAKY"})
#         anchortags_specialties = type_and_region.find_all("a")
#         specialties = ""
#         for a in anchortags_specialties:
#             specialties += a.get_text()+ " / "
#
#         berlin_region = type_and_region.find("span", {"class": "css-chan6m"}).get_text()
#         print(berlin_region)
#
#         price_range_span = type_and_region.find("span", {"class": "priceRange__09f24__mmOuH css-1s7bx9e"})
#         price_range = "";
#         if price_range_span is not None:
#             print(price_range_span.get_text())
#             price_range = str(len(price_range_span.get_text()))
#         else:
#             print("Unknown price range")
#             price_range = "Unknown"
#
#         source = url.urlopen(site + href+"&start=0")
#         page_soup = bs.BeautifulSoup(source, 'html.parser')
#         no_of_pages_span = page_soup.find("div", {"class": "border-color--default__09f24__NPAKY text-align--center__09f24__fYBGO"}).get_text()
#         reviews = page_soup.find_all("div", {"class": "review__09f24__oHr9V border-color--default__09f24__NPAKY"})
#         print("Number of Pages for Comments " +no_of_pages_span)
#         # for review in reviews:
#         #     author_tag = review.find("a", {"class": "css-1m051bw"})
#         #     author = "Unknown"
#         #     if author_tag is not None:
#         #         author = author_tag.get_text()
#         #         print(author)
#         #
#         #     comment = review.find("p", {"class": "comment__09f24__gu0rG css-qgunke"}).get_text()
#         #     print(comment)
#         #     rating = review.find("div", {
#         #         "class": "five-stars__09f24__mBKym five-stars--regular__09f24__DgBNj display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY"})[
#         #         'aria-label'].split()[0]
#         #     print(rating)
#         #     date = review.find("span", {"class": "css-chan6m"}).get_text()
#         #     print(date)
#         #     names.append(name)
#         #     ratings.append(overall_rating)
#         #     no_reviews.append(total_reviews)
#         #     specialties_list.append(specialties)
#         #     regions.append(berlin_region)
#         #     price_ranges.append(price_range)
#         #     authors.append(author)
#         #     comments.append(comment)
#         #     ratings_users.append(rating)
#         #     dates.append(date)
#         # time.sleep(30.0)
#
# data = {}
# data = {'Restaurant Name': names, 'Overall Rating': ratings, 'Total Reviews': no_reviews, 'Specialty': specialties_list, 'Region': regions, 'Price Range': price_ranges, "Author": authors, "Comment": comments, "Rating": ratings_users, "Date": dates}
# header =["Restaurant Name", "Overall Rating", "Total Reviews", "Specialty", "Region", "Price Range", "Author", "Comment", "Rating", "Date"]
#
# rest = pd.DataFrame(data)
# rest.to_csv("german_0.csv", columns = header)
#
