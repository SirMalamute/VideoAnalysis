from youtube_transcript_api import YouTubeTranscriptApi
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
from better_profanity import profanity
from dotenv import dotenv_values
config = dotenv_values(".env")
#hate api: facebook
print(config['APIKEY'])
def query_hate(inp):
    #{"inputs": "I like you. I love you",}
    arr = []
    for i in inp:
        payload = {"inputs":i}
        API_URL = "https://api-inference.huggingface.co/models/facebook/roberta-hate-speech-dynabench-r4-target"
        headers = {"Authorization": config['APIKEY']}
        response = requests.post(API_URL, headers=headers, json=payload)
        arr.append(response.json())
    #print(arr)
    return arr
	
def format_for_hate(inp):
    line = inp
    n = 512
    return [line[i:i+n] for i in range(0, len(line), n)];

def hate_result_formatter(inp):
    nothate=[]
    hate = []
    for i in inp:
        print("LOOK BELOW")
        print(i)
        for j in i:
            for k in j:
                if(k['label']=='nothate'):
                    nothate.append(k['score'])
                else:
                    hate.append(k['score'])
    print("ran hate")
    return sum(nothate)/len(nothate)

    #return nothate, hate;
#nsfw api --> michellejieli
def query_nsfw(inp):
    #{"inputs": "I like you. I love you",}
    arr = []
    for i in inp:
        payload = {"inputs":i}
        API_URL = "https://api-inference.huggingface.co/models/michellejieli/NSFW_text_classifier"
        headers = {"Authorization": config['APIKEY']}        
        response = requests.post(API_URL, headers=headers, json=payload)
        arr.append(response.json())
    #print(arr)
    return arr
	
def format_for_nsfw(inp):
    line = inp
    n = 512
    return [line[i:i+n] for i in range(0, len(line), n)];

def nsfw_result_formatter(inp):
    nothate=[]
    hate = []
    for i in inp:
        for j in i:
            print(j)
            for k in j:
                if(k['label']=='SFW'):
                    nothate.append(k['score'])
                else:
                    hate.append(k['score'])
    print("ran nsfw")
    return sum(nothate)/len(nothate)


def getTranscript(video_id):
    string = ""
    for i in YouTubeTranscriptApi.get_transcript(video_id):
        string += (i['text']+" ")
    return string

def sentimentAnalysis(inp):
    sentiment = SentimentIntensityAnalyzer()
    print("ran sent")
    return sentiment.polarity_scores(inp)['compound']

def profanity_check(inp):
    custom_badwords = open("badwords.txt", "r").read().split(",")
    profanity.load_censor_words(custom_badwords)
    print("ran profanity")
    return(profanity.contains_profanity(inp))

if __name__ == "__main__":
    print()
    print("HATE")
    print("-------")
    print(hate_result_formatter(query_hate(format_for_hate(getTranscript("dhPyK8GfQFk")))))
    print()
    print("NSFW")
    print("------------")
    print(nsfw_result_formatter(query_nsfw(format_for_nsfw(getTranscript("dhPyK8GfQFk")))))
