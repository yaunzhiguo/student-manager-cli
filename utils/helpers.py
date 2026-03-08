def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
def is_valid_score(score):
    return 0 <= score <= 100

def print_line():
    print("-" * 30)
