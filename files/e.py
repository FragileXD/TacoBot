import random

a = ""
user = input("user 1: ")
user2 = input("user 2: ")
if len(user) == 22:
    try:
        user = user.replace("!", "")
        a = ""
    except:
        user = user
if len(user2) == 22:
    try:
        user2 = user2.replace("!", "")
        a = ""
    except:
        user2 = user2
lovepercent = random.randint(1, 101)
rounded = int((round(lovepercent, -1)) / 10)
shaded = "■" * rounded
unshaded = (10 - rounded) * "□"


print(
    f"**:heartpulse: MATCHMAKING {lovepercent}% :heartpulse:**\n:small_red_triangle: {a+user+a}\n:small_red_triangle_down: {a+user2+a}",
    f"{shaded}{unshaded}",
)