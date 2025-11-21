import price_info as price

def test_cost_of_fruit():
    result=0
    result=price.cost_of_fruits("pear",10)
    assert(result==9.00)

def test_total_cost_shopping():
    result=0
    result=price.total_cost_shopping()
    assert(result==46.75)
