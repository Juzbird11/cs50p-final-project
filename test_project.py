import project

def test_binary_search():
    assert(len(project.binary_search([2, 3, 1, 4, 1], 1)) == 3)
    assert(not len(project.binary_search([2, 3, 1, 4, 1], 1)) == 2)
    assert(not len(project.binary_search([2, 3, 1, 4, 1], 1)) == 1)

def test_string_to_num_list():
    assert(project.string_to_num_list('12, 34, 23, 33, 23') == [12, 23, 23, 33, 34])
    assert(project.string_to_num_list('1, 14, 223, 51, 3') == [1, 3, 14, 51, 223])
    assert(project.string_to_num_list('14, 3, 1, 33 , 23 ') == [1, 3, 14, 23, 33])

def test_vis():
    assert(project.vis(project.binary_search([2, 3, 1, 4, 2, 1], 1)) == True)
    assert(project.vis(project.binary_search([2, 3, 1, 4, 2, 1], 5)) == False)
    assert(project.vis(project.binary_search([2, 3, 1, 4, 2, 1], 12)) == False)