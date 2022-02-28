# method1
# def first_duplicate(arr):
#     li = []
#     for item in arr:
#         if item not in li:
#             li.append(item)
#         else:
#             return item
#     return 'No Duplicate value in arr'
# arr = [int(num) for num in input().split()]
# print(first_duplicate(arr))

# method2
def fis_dup(a,n):
    for i in range(len(a)):
        if a.count(a[i])>1:
            return a[i]
    return "there is no duplicate repetition number"
arr=[10,3,5,4,7,5,10,8]
n=len(arr)
print(fis_dup(arr,n))

def player_score(arr):
    player1_score = arr[0]
    player2_score = 0
    prev = arr[0]
    current_player = 'p2' if arr[0]%2==0 else 'p1'
    for score in arr[1:]:
        if  prev%2!=0:
            current_player = 'p2' if current_player=='p1' else 'p1'
        if current_player=='p1':
            player1_score+=score
        else:
            player2_score+=score
        prev = score
    return player1_score,player2_score

arr = [int(score) for score in input().split()]
p1,p2 = player_score(arr)
print(f'player1 score is {p1}\nplayer2 score is {p2}')