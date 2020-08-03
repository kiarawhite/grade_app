def calculate(academics):
    points = int(academics["my_goal"]) - int(academics["my_grade"])

    plan=""
    if academics["my_current_assignment"]=="test":
        plan="2 pages per day"
    elif academics["my_current_assignment"]=="regular":
        plan="one-hundred thirty percent of current work done"
    elif academics["my_current_assignment"]=="makeup":
        plan="email teacher for plan"
    else:
        plan= "1/4 of project per day, last day proofread"
    study_plan= {
        "points": points,
        "plan": plan
    }
    return study_plan