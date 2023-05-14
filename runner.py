from transcriptFunctions import hate_result_formatter, query_hate, format_for_hate
from transcriptFunctions import nsfw_result_formatter, query_nsfw, format_for_nsfw
from transcriptFunctions import sentimentAnalysis, profanity_check
from transcriptFunctions import getTranscript

def main(inp):
    sentiments = []
    hate = []
    nsfw = []
    prof = []
    for i in inp:
        print(i)
        sentiments.append(sentimentAnalysis(getTranscript(i)))
        print("DONE WITh SENTIMENT ANALYSIS")
        hate.append(hate_result_formatter(query_hate(format_for_hate(getTranscript(i)))))
        print("DONE WITH HATE")
        nsfw.append(nsfw_result_formatter(query_nsfw(format_for_nsfw(getTranscript(i)))))
        print("DONE WITH NSFW")
        if(profanity_check(getTranscript(i))):
            prof.append(1)
        else:
            prof.append(0)
        print("DONE WITH PROF")
    return [sentiments[0], hate[0], nsfw[0], prof[0]]

if __name__ == "__main__":
    print(main(['OfOotGjXP1Q']))