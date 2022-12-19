# Yelp Rating Predictor & Fake Review Detection

#### Gruppe 18 - HTW BERLIN 

 
In the era of internet shopping and dining, online reviews play a pivotal role in the customers' decision-making process.

According to a 2016 Yelp-specific study, a one-star improvement in Yelp rating can help restaurants increase their revenues by 9%<sup>[1](#myfootnote1)</sup>.
Given the importance of online reviews for the hospitality industry, fake reviews detection is a great concern for restaurant owners. While the means to detect them are fairly limited, there have been several approaches to the topic. 
While some research relies heavily on metadata in order to detect potential fake reviews, some studies have focused on sentiment analysis and the disparity between the sentiment score of a given review and  the numeric rating (1 to 5) attached to the reviews.
This pattern of inconsistency between rating and the sentiment conveyed in a given review has been found to be a marker for fake reviews.<sup>[2](#myfootnote3)</sup>.

The present project follows the same approach using a self-scraped dataset of ~ 10,000 German-speaking Yelp reviews and ratings.
Our project relies heavily on Luo et al, 2021<sup>[3](#myfootnote3)</sup> and Chiny et al, 2021 <sup>[4](#myfootnote4)</sup>.
The main goals consist of 
  - detecting reviews with mismatched rating 
  - labeling mismatched reviews as potential candidates for fake reviews. 

In order to achieve these two goals, a rating prediction model was built using a hybrid sentiment classifier for 5-star ratings (cf. [4](#myfootnote4)).

The model leverages features engineered by three separate prediction models, namely TextBlob, TF-IDF-based regression and word-embedding based LSTM classifier.

### Method 

1. <b> Data collection [1_webscraping] </b>

The analyzed dataset was scraped from Yelp and contains 9719 ratings and German-speaking reviews for restaurants located in Berlin.
The CSV can be found at path: 1_scraping/intermediary_outputs/german_merged.csv
//TODO: ReadMe for Scraper


2. <b> Data cleaning and text pre-processing [2_text_preprocessing] </b>

In order to improve the accuracy of the models, links, numbers, symbols, special characters and punctuation were removed.
Stopwords were removed before tokenization and lemmatization of each textual review.

3. <b> Modelling [3_modelling] </b>

4. <b> Evaluation </b>


<a name="myfootnote1">1</a>: Luca, M. 2016, <i> [Reviews, Reputation, and Revenue: The case of Yelp.com](https://www.hbs.edu/ris/Publication%20Files/12-016_a7e4a5a2-03f9-490d-b093-8f951238dba2.pdf) </i>

<a name="myfootnote2">2</a>: Shan. G. et al. 2018, <i> [Inconsistency Investigation between Online
Review Content and Ratings](https://par.nsf.gov/servlets/purl/10095442) </i>

<a name="myfootnote3">3</a>: Luo, Y. et al. 2021, <i> [IComparative study of deep learning models for analyzing online restaurant reviews in the era of the COVID-19 pandemic](https://www.sciencedirect.com/science/article/pii/S0278431920304011) </i>

<a name="myfootnote4">4</a>: Chiny, M. et al. 2021, <i> [LSTM, VADER and TF-IDF based Hybrid Sentiment Analysis Model](https://thesai.org/Publications/ViewPaper?Volume=12&Issue=7&Code=IJACSA&SerialNo=30) </i>