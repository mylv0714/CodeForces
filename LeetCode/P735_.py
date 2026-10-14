class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        st = []
        for aster in asteroids:
            flag = False
            if aster >= 0:
                st.append(aster)
            else: # -부호를만났을때
                # 스택이 차있고 마지막 원소가 양수이면 진행
                while len(st) and st[-1] > 0:

                    # 같을땐 둘다 제거
                    if st[-1] == aster*(-1):
                        st.pop()
                        flag = True
                        break
                    elif st[-1] < aster*(-1):
                        st.pop()
                    else:
                        break
                
                if len(st) == 0 and flag == False:
                    st.append(aster)
                elif len(st) == 0 and flag == True:
                    pass
                elif st[-1] < 0 and flag == False:
                    st.append(aster)
        return st

list = [1,-1,-2,-2]
print(Solution().asteroidCollision(list))