'''
Created on Nov 13, 2018
@author: Brandon Cao
bcao4
I pledge my honor that I have abided by the Stevens Honor System.
'''
PREF_FILE='musicrecplus.txt'

def main():
    '''user is prompted for their name if the user is a new user
    If the user is not new, they should not be asked their preferences 
    and should immediately be shown the menu'''
    user_map=load_users(PREF_FILE)
    username=input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
    if username not in user_map:
        preferences=get_preferences(username, user_map)
        save_user_prefs(username,preferences,user_map,PREF_FILE)
    menu(username,user_map)
    
def load_users(filename):
    '''loads user and their preferences'''
    try:
        file=open(filename,'r')
    except:
        file=open(filename,'w')
        user_dict={}
        file.close()
        return user_dict
    user_dict={}
    for x in file:
        username, artists=x.strip().split(':')
        artist_list=artists.split(',')
        artist_list.sort()
        user_dict[username]=artist_list
    file.close()
    return user_dict

def get_preferences(username, user_map):
    '''The user enters their preferences (artists they like) one at a time'''
    new_pref=''
    if username in user_map:
        prefs=user_map[username]
        new_pref=input('Enter an artist that you like (Enter to finish):')
        prefs=[]
    else:
        prefs=[]
        new_pref=input('Enter an artist that you like (Enter to finish):')
    while new_pref!='':
        prefs.append(new_pref.strip())
        new_pref=input('Enter an artist that you like (Enter to finish):')
    prefs.sort()
    return prefs

def save_user_prefs(username,prefs,user_map,filename):
    '''saves a users preferences to a file'''
    user_map[username]=prefs
    file=open(filename,'w')
    for user in user_map:
        save=str(user)+ ':'+','.join(user_map[user])+ '\n'
        file.write(save)
    file.close

def menu(username,user_map):
    '''displays a menu'''
    while True:
        print('''Enter a letter to choose an option:
    e - Enter preferences
    r - Get recommendations
    p - Show most popular artists
    h - How popular is the most popular
    m - Which user has the most likes
    q - Save and quit''')
        user_input=input()
        if user_input=='e':
            prefs=get_preferences(username,user_map)
            save_user_prefs(username,prefs,user_map,PREF_FILE)
        elif user_input =='r':
            recs=get_recs(username,user_map[username],user_map)
            print_recs(recs,username)
            prefs=user_map[username]
            save_user_prefs(username,prefs,user_map,PREF_FILE)
        elif user_input=='p':
            fav_artist(user_map)
        elif user_input=='h':
            how_popular(user_map)
        elif user_input=='m':
            most_likes(user_map)
        elif user_input=='q':
            try:
                save_user_prefs(username,prefs,user_map,PREF_FILE)
                break
            except:
                break

def print_recs(recs,username):
    '''prints the recs for a user'''
    if len(recs)==0:
        print('No recommendations available at this time')
    else:
        for artist in recs:
            print(artist)

def get_recs(curr_user, prefs, user_map):
    '''recommendations come from the users with the most similarity to the current user.'''
    bestUser=best_user(curr_user, prefs, user_map)
    recommendations=drop(prefs, user_map[bestUser])
    return recommendations
 

def delete_dupes(lst):
    '''returns a list without any of the same elements'''
    dicti={}
    for x in lst:
        if x in dicti:
            dicti[x]+=1
        else:
            dicti[x]=1
    return list(dicti.keys())

def best_user(curr_user, prefs, user_map):
    '''returns the user with most similar preferences to the current user'''
    users = list(user_map.keys())
    best_score = -1
    best_match = None
    for user in users:
        score = num_matches(prefs, user_map[user])
        if prefs != user_map[user]:
            if score > best_score:
                best_score = num_matches(prefs, user_map[user])
                best_match = user
    return best_match

def num_matches(lst1,lst2):
    '''returns the number of matching elements in two lists'''
    matches=0
    for x in lst1:
        if x in lst2:
            matches+=1
    return matches

def drop(lst1,lst2):
    '''returns a list that has no matches in two lists'''
    lst3=[]
    for x in lst1:
        if x not in lst2:
            lst3+=[x]
    return lst3

def fav_artist(user_map):
    '''Print the artist that is liked by the most users'''
    user_list=user_map.keys()
    likes={}
    fav=[]
    maximum=0
    possible_users=[]
    for user in user_list:
        if '$' not in user:
            possible_users.append(user)
    for user in possible_users:
        for artist in user_map[user]:
            if artist in likes:
                likes[artist]+=1
            else:
                likes[artist]=1
    for artist in likes:
        if likes[artist]>maximum:
            maximum=likes[artist]
    for artist in likes:
        if likes[artist]==maximum:
            fav.append(artist)
    if len(fav)==1:
        print(fav[0])
    elif len(fav)==0:
        print('Sorry, no artists found')
    else:
        for x in fav:
            print(x)
            
def how_popular(user_map):
    '''Prints the number of likes the most popular artist(s) received'''
    user_list=user_map.keys()
    likes={}
    most_popular=[]
    maximum=0
    possible_users=[]
    for user in user_list:
        if '$' not in user:
            possible_users.append(user)
    for user in possible_users:
        for artist in user_map[user]:
            if artist in likes:
                likes[artist]+=1
            else:
                likes[artist]=1
    for artist in likes:
        if likes[artist]>maximum:
            maximum=likes[artist]
    for artist in likes:
        if likes[artist]==maximum:
            most_popular.append(artist)
    if len(most_popular)==1:
        print(maximum)
    elif len(most_popular)==0:
        print('Sorry, no artists found')
    else:
        print(maximum)
        
def most_likes(user_map):
    '''Print the full name(s) of the user(s) who likes the most artists'''
    users=list(user_map)
    maximum=0
    best_user=[]
    for x in range(len(users)):
        if len(user_map[users[x]])>maximum and users[x][-1]!='$':
            maximum=len(user_map[users[x]])
            best_user=[users[x]]
        if len(user_map[users[x]])==maximum and users[x][-1]!='$':
            maximum=len(user_map[users[x]])
            best_user.append(users[x])
    if len(best_user)==1:
        print(best_user[0])
    elif len(best_user)==0:
        print('Sorry, no user found')
    elif len(best_user)>1:
        for user in best_user[1:]:
            print(user)

main()

