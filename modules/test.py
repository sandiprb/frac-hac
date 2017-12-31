from sentiment import Sentiment

ans = {
    "id": "5a43e1d0f1cca02c6f5df44f",
    "questionType" : "yes/no",
    "asin" : "602260074X",
    "answerTime" : "Dec 30, 2014",
    "unixTime" : 1419926400,
    "question" : "is the surface in side the smooth?",
    "answerType" : "Y",
    "answer" : "Yes"
}
data = [{"id" : "5a4749acf1cca0eadf9574fe",
    "reviewerID" : "A3G6XNM240RMWA",
    "asin" : "7806397051",
    "reviewerName" : "Karen",
    "helpful" : [0,4],
    "unixReviewTime" : 1378425600,
    "reviewText" : "Great",
    "overall" : 4.0,
    "reviewTime" : "09 6, 2013",
    "summary" : "great quality"
},
        {"id" : "5a4749acf1cca0eadf9574fe",
    "reviewerID" : "A3G6XNM240RMWAeee",
    "asin" : "7806397051",
    "reviewerName" : "Karen",
    "helpful" : [0,4],
    "unixReviewTime" : 1378425600,
    "reviewText" : "Very Bad",
    "overall" : 4.0,
    "reviewTime" : "09 6, 2013",
    "summary" : "great quality"
},
{"id" : "5a4749acf1cca0eadf9574fe",
    "reviewerID" : "A3G6XNM240RMWA",
    "asin" : "7806397051",
    "reviewerName" : "Karen",
    "helpful" : [0,4],
    "unixReviewTime" : 1378425600,
    "reviewText" : "Yes",
    "overall" : 4.0,
    "reviewTime" : "09 6, 2013",
    "summary" : "great quality"
},

       ]

s = Sentiment()


print s.get_reviews_sentiment(data)
print s.get_answer_sentiment(ans)