tim = {
       "name": "Tim",
       "ig_handle": "Timbits_TT",
       "email":"tim@pwa.com",
       "phone":"416-123-4567"
       }
charlie = {
           "name": "Charlie",
           "ig_handle": "Charliepeanuts420",
           "email":"charlie@pwa.com",
           "phone":"647-789-1234"
           }
tiffany = {
           "name": "Tiffany",
           "ig_handle": "Tiffssnifs",
           "email":"tiffany@pwa.com",
           "phone":"416-321-7654"
           }
robert = {
          "name": "Robert",
          "ig_handle": "Robby.68",
          "email":"robert@pwa.com",
          "phone":"647-987-6543"
          }

friends = []
friends.append(tim)
friends.append(charlie)
friends.append(tiffany)
friends.append(robert)

print("My contact list")
i = 0
length = len(friends)
while i < length:
    friend = friends[i]
    print(f'{friend}')
    i += 1