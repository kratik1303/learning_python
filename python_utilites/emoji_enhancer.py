#get a dictionary 
emoji_map_fun = {
    "love":"💖",
    "happy":"☺️",
    "code":"💻",
    "tea":"☕",
    "music":'🎵',
    "food":"🍕"   
}

#get user a msg
user_msg = input ("Enter a message : \n")

updated_words = [ ]

#process each word

for word in user_msg.split():
    cleaned = word.lower().strip(',.!?')
    emoji=  emoji_map_fun.get(cleaned,'')
    
    if emoji :
        updated_words.append(f"{word} {emoji} ")
    else:
        updated_words.append(f"{word}")
        
updated_msg = ' '.join(updated_words)

print("\n Enhanced msg is : \n")
print(updated_msg)