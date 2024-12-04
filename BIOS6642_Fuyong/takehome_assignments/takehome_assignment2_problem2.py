import sys

def selfdividing(p1, p2):
    if p1 < 0 or p2 < 0:
        print('p1 and p2 should be positive.')
    if p1 > p2:
        print('p1 should not be greater than p2.')
    else:
        for p in range(p1, p2+1):
            is_selfdividing = True
            cur_n = p
            while cur_n > 0:
                cur_n, res = divmod(cur_n, 10)  # Get the quotient and remainder of the division
                if res == 0 or (p % res) != 0:  # If the inetger is divisible by the current remainder, then it is not a selfdividing integer
                    is_selfdividing = False
                    break
            if is_selfdividing:
                print(p, end=' ')   # print the selfdividing integer
        print('\n')

# Usage example (command line): python takehome_assignment2_problem2.py 30 50
if __name__ == '__main__':
    selfdividing(int(sys.argv[1]), int(sys.argv[2]))
