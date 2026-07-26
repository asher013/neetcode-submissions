class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        st = []
        for p, s in zip(position,speed):
            cars.append([p,s])
        cars.sort(reverse=True)
        for car in cars:
            time = (target-car[0]) / car[1]
            if st and st[-1] >= time:
                continue
            st.append(time)
        return len(st)
