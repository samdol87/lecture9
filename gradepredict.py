# Discussion section: 13, drop: 2
# homeworks: 14, drop: 2
# lecture exercises: 26, drop: 4
# midterms: 2
# projects: 3
# final project: 1

# 1. get data into program
# return: dictionary with keys: assigment group names,
#                         values: lists of scores
def get_data():
    pass

# 2. identify lowerst grades for discussion, homeworks, lecture exercises
# returns: list of scores, with the lowerst dropped
def drop_lowest_scores(list_of_scores, num_to_drop):
    pass

# param: list for a compute
# returns: total for that score
def compute_group_total(list_of_scores):
    pass

# 3. compute total points across categories
# 4. convert to percentage
# 5. convert to letter grade
def compute_grade(data_dict):
    pass

def test_functions():
# test drop_lowest_scores
    list1 = [10, 9, 8, 7,  6]
    expected_return1 = [10, 9, 8]
    expected_return2 = [10]
    list2 = [1,1,1,1,1]

    passed = 0
    failed = 0

    if drop_lowest_scores(list1, 2) == expected_return1:
#   a test passed
        passed += 1
    else:
#   a test failed
        failed += 1
    print("Failed Test 1")

    if drop_lowest_scores(list1, 4) == expected_return2:
#   a test passed
        passed += 1
    else:
#   a test failed
        failed += 1
    print("Failed Test 2")

    if drop_lowest_scores(list3, 4) == expected_return3:
#   a test failed
        passed += 1
    else:
#   a test failed
        failed += 1
    print('Failed test 1')


data_dict = get_data()
homework_scores = drop_lowest_scores(data_dict["homeworks"], 2)
lecture_scores = drop_lowest_scores(data_dict["lectures"], 4)
discussion_scores = drop_lowest_scores(data_dict["discussion"], 2)
midterm_scores = data_dict["mideterm"]
project_scores = data_dict["projects"]
final_score = data_dict["final_project"]
