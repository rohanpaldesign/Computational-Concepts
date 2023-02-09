def split_a_string(text=""):
    sample_text = sample_text.split()
    return count(sample_text)

def split_a_string(text=""):
    sample_text = text.split()
    return count(sample_text)


#WORKING
def count_all_tokens(samples=[]):
    count = 0
    for text in samples:
        sample_split = text.split()
        count = count + len(sample_split)
    print(f"Total tokens = {count}")
    return count, sample_split



#Count of all hashtags =================================================

def count_hashtags(tl=[]):
    count = 0
    for item in tl:
        if item.startswith("#"):
            count +=1
    return count



#List of hashtag tokens ==================================================

def get_hashtag_tokens(tl=[]):
    for item in tl:
        if item.startswith("#"):
            tl.append(item)
    return tl



#Creating a dictionary with two lists hashtags and mentions ======================

def get_entities():
    entities = dict()
    entities["hashtags"] = list()
    entities["mentions"] = list()

    for token in token_list:
        if token.startswith("#"):
            entities["hashtags"].append(token)
        if token.startswith("@"):
            entities["mentions"].append(token)
    return entities



#Making all tokens lower case =============================================

def tokens_to_lower(token_list=[]):
    token_lower = list()

    for item in token_list():
        new_token = item.lower()
        token_lower.append(new_token)
    return token_lower


#print(tokens_to_lower(sample_splits[0]))


#Handling Punctuaton =======================================================

#PUNCT_LIST = [",",".","?","!",";",":","(",")"]

#PUNCT_STR = "!@#$%^&*()" A string is also treated as a list of characters.

def clean_punctuation(token_list = [], punctuation = []):
    new_token_list = list()

    for item in token_list:
        for p in punctuation:
            item = item.replace(p, "")
        if item:
            new_token_list.append(item)
    return new_token_list

#clean_punctuation(sample_splits[0], PUNCT_LIST)

#clean_punctuation(sample_splits[0], PUNCT_STR)


#Remove the stop words ====================================================

#STOP_WORDS = ['this', 'that', 'the', 'be', 'will', 'or', 'for', 'in', 'by', 'a', 'was', 'what', 'as', 'how', 'from', 'where', 'about', 'is', 'who', 'of', 'it', 'at', 'are', 'i', 'on', 'with', 'an', 'to', 'when']


def remove_stop_words(token_list = [], stop_words = []):
    list_without_stop = list()

    for item in token_list:
        for s in stop_words:
            if item != s:
                list_without_stop.append(item)
    return list_without_stop

