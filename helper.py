from urlextract import URLExtract
extract = URLExtract()

def fetch_stats(selected_user,df):

    if selected_user != "Overall":
        df = df[df['user'] == selected_user]


    #1. Fetching number of messages
    num_messages = df.shape[0]

    #2. number of words
    words = []
    for message in df['message']:
        words.extend(message.split())
    
    #3. fetch the number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>'].shape[0]
    
    #4. fetch number of links shared
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))


    return num_messages, len(words), num_media_messages, len(links)


def most_busy_users(df):
    x = df['user'].value_counts().head()

    df = round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'index':'name','user':'percent'})

    return x, df

