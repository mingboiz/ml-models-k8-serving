from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentAnalysis(object):
    result = {}
    analyser = None

    def __init__(self):
        self.analyser = SentimentIntensityAnalyzer()

    def predict(self, X):
        if len(X) == 0:
            self.result["sentiment_analysis_passed"] = False
            self.result["failure_reason"] = "Invalid input"

        else:
            sentence = X[0]
            score = self.analyser.polarity_scores(sentence)
            self.result["sentiment_analysis_passed"] = True
            self.result["input_text"] = sentence
            self.result["sentiment_analysis_result"] = score

        return X

    def tags(self):
        return self.result
