class Passenger:
    
    def sum_passengers(self, array:list):
        sum_p1 = 0
        sum_p2 = 0

        for i in array:
            if i[2] == 2:
                if i[3] > 6:
                    continue
                if i[5] == 0 and i[4] < 5:
                    sum_p2 += i[3]
            if i[2] == 1:
                sum_p1 += i[3]

        return {'p1': sum_p1, 'p2': sum_p2}