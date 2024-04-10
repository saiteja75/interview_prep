# asteroid-collision
# https://leetcode.com/problems/asteroid-collision/description/
'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
'''


def asteroidCollision(asteroids: List[int]) -> List[int]:
    st = []
    for i in asteroids:
        if st and st[-1]>0>i:
            toUpdate = False
            while(st and st[-1]>0>i):
                if st[-1]<=abs(i):
                    value = st.pop()
                    if value==abs(i):
                        toUpdate = False
                        break
                    else:
                        toUpdate = True
                else:
                    toUpdate = False
                    break
            if toUpdate == True:
                st.append(i)
        else:
            st.append(i)
    
    return st
    