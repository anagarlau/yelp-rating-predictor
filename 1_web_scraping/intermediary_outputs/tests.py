import re
import pandas as pd
str = "1 of 121"


list_spans = re.findall(r"\d+", str)
no_of_spans = int(list_spans[1])
print(type(no_of_spans))

# dataFrame = pd.concat(map(pd.read_csv, ['german_0.csv', 'german_1.csv','german_2.csv', 'german_3.csv', 'german_4.csv', 'german_5.csv', 'german_6.csv','german_7.csv','german_8.csv','german_9.csv', 'german_10.csv','german_11.csv','german_12.csv','german_13.csv','german_14.csv','german_15.csv','german_16.csv','german_17.csv','german_18.csv','german_19.csv','german_20.csv','german_21.csv','german_22.csv','german_23.csv','german_24.csv','german_25.csv','german_26.csv','german_27.csv','german_28.csv','german_29.csv','german_30.csv','german_31.csv','german_32.csv','german_33.csv','german_34.csv', 'german_35.csv', 'german_36.csv','german_37.csv','german_38.csv','german_39.csv', 'german_40.csv','german_41.csv','german_42.csv','german_43.csv',"german_44.csv","german_45.csv","german_46.csv","german_47.csv","german_48.csv","german_49.csv","german_50.csv", "german_51.csv","german_52.csv","german_53.csv","german_54.csv","german_55.csv","german_56.csv","german_57.csv","german_58.csv","german_59.csv","german_60.csv","german_61.csv"]), ignore_index=True)
# dataFrame.drop(['Unnamed: 0'], axis=1, inplace=True)
#
#
#
# header =["Index", "Restaurant Name", "Overall Rating", "Total Reviews", "Specialty", "Region", "Price Range", "Author", "Comment", "Rating", "Date"]
# dataFrame.to_csv("test_german_merged.csv")



# unique_rest = len(yelp['Restaurant Name'].unique())
# print(unique_rest)