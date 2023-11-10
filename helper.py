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
    
    return num_messages, len(words), num_media_messages




