from csv import DictReader

s_t = (input('What is the state:'))
c_r = (input('Cost or Rating:'))
o_p = (input('Operstion:'))

S_T = s_t.title()
C_R = c_r.lower()
O_P = o_p.lower()
def hotels_performance(state,cost_rating,operation):
    with open('hotels.csv', 'r') as f:
        csv_reader = DictReader(f)
        csv_data = list(csv_reader)
        max = 0
        min=float('inf')
        hotel_code=''
        avg=0
        s=0
        counter=0
        l=[]

        if cost_rating == 'cost' and operation == 'highest':
            for row in csv_data:
                if row['State'] == state:
                    if max <= int(row['Cost']):
                        max = int(row['Cost'])
                        hotel_code = row['Hotel Code']
            for row in csv_data:
                if row['State'] == state:
                    if max == int(row['Cost']):
                        l.append(row['Hotel Code'])
            print(f'Hotel with highest price in {state} is {l} with price {max}')


        if cost_rating == 'rating' and operation == 'highest':
            for row in csv_data:
                if row['State'] == state:
                    if max < float(row['Ratings']):
                        max = float(row['Ratings'])
                        hotel_code = row['Hotel Code']
            for row in csv_data:
                if row['State'] == state:
                    if max == float(row['Ratings']):
                        l.append(row['Hotel Code'])
            print(f'Hotel with highest rating in {state} is {l} with rating {max}')

        if cost_rating == 'rating' and operation == 'average':
            for row in csv_data:
                if row['State'] == state:
                    s+=float(row['Ratings'])
                    counter+=1
            avg=s/counter
            print(f'Average rating of hotel in {state} is {avg}')

        """Average cost is ok"""
        if cost_rating == 'cost' and operation == 'average':
            for row in csv_data:
                if row['State'] == state:
                    s+=int(row['Cost'])
                    counter+=1
            avg=s/counter
            print(f'Average price of hotel in {state} is {avg}')

        if cost_rating == 'cost' and operation == 'cheapest':
            for row in csv_data:
                if row['State'] == state:
                    if min > int(row['Cost']):
                        min = int(row['Cost'])
                        hotel_code = row['Hotel Code']
            for row in csv_data:
                if row['State'] == state:
                    if min == int(row['Cost']):
                        l.append(row['Hotel Code'])
            print(f'Hotel with cheapest price in {state} is {l} with price {min}')

        if cost_rating == 'rating' and operation == 'cheapest':
            for row in csv_data:
                if row['State'] == state:
                    if min > float(row['Ratings']):
                        min = float(row['Ratings'])
                        hotel_code = row['Hotel Code']
            for row in csv_data:
                if row['State'] == state:
                    if min == float(row['Ratings']):
                        l.append(row['Hotel Code'])
            print(f'Hotel with cheapest rating in {state} is {l} with rating {min}')

hotels_performance(S_T, C_R, O_P)




# # if state == 'India' and cost_rating == 'cost' and operation == 'highest':
        # #     for row in csv_data:
        # #         if max <= int(row['Cost']):
        # #             max = int(row['Cost'])
        # #             hotel_code = row['Hotel Code']
        # #     for row in csv_data:
        # #         if max == int(row['Cost']):
        # #             l.append(row['Hotel Code'])
        # #     print(f'Hotel with highest price in India is {l} with price {max}')
        #
        # if cost_rating == 'rating' and operation == 'highest':
        #     for row in csv_data:
        #         if row['State'] == state or state=='India':
        #             if max < float(row['Ratings']):
        #                 max = float(row['Ratings'])
        #                 hotel_code = row['Hotel Code']
        #     for row in csv_data:
        #         if row['State'] == state or state=='India':
        #             if max == float(row['Ratings']):
        #                 l.append(row['Hotel Code'])
        #     print(f'Hotel with highest rating in {state} is {l} with rating {max}')
        #
        # if cost_rating == 'rating' and operation == 'average':
        #     for row in csv_data:
        #         if row['State'] == state or state=="India":
        #             s+=float(row['Ratings'])
        #             counter+=1
        #     avg=s/counter
        #     print(f'Average rating of hotel in {state} is {avg}')
        #
        # if cost_rating == 'cost' and operation == 'average':
        #     for row in csv_data:
        #         if row['State'] == state or state=="India":
        #             s+=int(row['Cost'])
        #             counter+=1
        #     avg=s/counter
        #     print(f'Average price of hotel in {state} is {avg}')
        # #
        # # if cost_rating == 'cost' and operation == 'cheapest':
        # #     for row in csv_data:
        # #         if row['State'] == state:
        # #             if min > int(row['Cost']):
        # #                 min = int(row['Cost'])
        # #                 hotel_code = row['Hotel Code']
        # #     for row in csv_data:
        # #         if row['State'] == state:
        # #             if min == int(row['Cost']):
        # #                 l.append(row['Hotel Code'])
        # #     print(f'Hotel with cheapest price in {state} is {l} with price {min}')
        # #
        # # if cost_rating == 'rating' and operation == 'cheapest':
        # #     for row in csv_data:
        # #         if row['State'] == state:
        # #             if min > float(row['Ratings']):
        # #                 min = float(row['Ratings'])
        # #                 hotel_code = row['Hotel Code']
        # #     for row in csv_data:
        # #         if row['State'] == state:
        # #             if min == float(row['Ratings']):
        # #                 l.append(row['Hotel Code'])
        # #     print(f'Hotel with cheapest rating in {state} is {l} with rating {min}')


# if cost_rating == 'cost' and operation == 'highest':
#     for row in csv_data:
#         if row['State'] == state:
#             if max <= int(row['Cost']):
#                 max = int(row['Cost'])
#                 hotel_code = row['Hotel Code']
#     for row in csv_data:
#         if row['State'] == state:
#             if max == int(row['Cost']):
#                 l.append(row['Hotel Code'])
#     print(f'Hotel with highest price in {state} is {l} with price {max}')
#
#
# if cost_rating == 'rating' and operation == 'highest':
#     for row in csv_data:
#         if row['State'] == state:
#             if max < float(row['Ratings']):
#                 max = float(row['Ratings'])
#                 hotel_code = row['Hotel Code']
#     for row in csv_data:
#         if row['State'] == state:
#             if max == float(row['Ratings']):
#                 l.append(row['Hotel Code'])
#     print(f'Hotel with highest rating in {state} is {l} with rating {max}')
#
# if cost_rating == 'rating' and operation == 'average':
#     for row in csv_data:
#         if row['State'] == state:
#             s+=float(row['Ratings'])
#             counter+=1
#     avg=s/counter
#     print(f'Average rating of hotel in {state} is {avg}')
#
# if cost_rating == 'cost' and operation == 'average':
#     for row in csv_data:
#         if row['State'] == state:
#             s+=int(row['Cost'])
#             counter+=1
#     avg=s/counter
#     print(f'Average price of hotel in {state} is {avg}')
#
# if cost_rating == 'cost' and operation == 'cheapest':
#     for row in csv_data:
#         if row['State'] == state:
#             if min > int(row['Cost']):
#                 min = int(row['Cost'])
#                 hotel_code = row['Hotel Code']
#     for row in csv_data:
#         if row['State'] == state:
#             if min == int(row['Cost']):
#                 l.append(row['Hotel Code'])
#     print(f'Hotel with cheapest price in {state} is {l} with price {min}')
#
# if cost_rating == 'rating' and operation == 'cheapest':
#     for row in csv_data:
#         if row['State'] == state:
#             if min > float(row['Ratings']):
#                 min = float(row['Ratings'])
#                 hotel_code = row['Hotel Code']
#     for row in csv_data:
#         if row['State'] == state:
#             if min == float(row['Ratings']):
#                 l.append(row['Hotel Code'])
#     print(f'Hotel with cheapest rating in {state} is {l} with rating {min}')

# if state=='Karnataka':
#     if cost_rating=='cost':
#         if operation=='highest':
#             for row in csv_reader:
#
#                 if row['State'] == 'Karnataka':
#                     if max < row['Cost']:
#                         max = row['Cost']