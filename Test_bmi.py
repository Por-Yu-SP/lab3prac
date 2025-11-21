import lab2.bmi as bmi

def test_bmi_normal_weight():
    result=0
    weight=60
    height=1.7
    result=bmi.calculate_bmi(height,weight)
    assert(result==0)

    
def test_bmi_under_weight():
    result=0
    weight=40
    height=1.7
    result=bmi.calculate_bmi(height,weight)
    assert(result==-1)

    
def test_bmi_over_weight():
    result=0
    weight=120
    height=1.7
    result=bmi.calculate_bmi(height,weight)
    assert(result==1)