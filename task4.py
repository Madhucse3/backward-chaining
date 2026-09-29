facts = [
    "GoodPerformance",
    "ProgrammingSkills",
    "CommunicationSkills",
    "PlacementTraining"
]

rules = {
    "EligibleForPlacement": [
        "GoodPerformance",
        "ProgrammingSkills",
        "CommunicationSkills",
        "PlacementTraining"
    ]
}


def backward_chaining(goal):
    print("Trying to prove:", goal)

    if goal in facts:
        print("Fact found:", goal)
        return True

    if goal in rules:
        for condition in rules[goal]:
            if not backward_chaining(condition):
                return False

        return True

    return False


goal = "EligibleForPlacement"

if backward_chaining(goal):
    print("Final Conclusion: Student is Eligible for Placement")
else:
    print("Final Conclusion: Student is NOT Eligible for Placement")