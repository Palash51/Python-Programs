def check_point(arr):
    ini_ene, curr_ene = 1, 1
    for i in range(len(arr)):
        curr_ene += arr[i]
        if curr_ene <= 0:
            ini_ene = ini_ene + abs(curr_ene) + 1
            curr_ene = 1
    return ini_ene

arr = [4,4,4,4]
print(check_point(arr))