"""
Project Gridiron
Model Evaluator

Version 0.1
"""


def evaluate_prediction(predicted_margin, actual_margin):

    error = abs(predicted_margin - actual_margin)

    if error <= 3:
        grade = "Excellent"

    elif error <= 7:
        grade = "Good"

    elif error <= 10:
        grade = "Fair"

    else:
        grade = "Poor"

    return {
        "prediction_error": round(error, 2),
        "grade": grade
    }


example = evaluate_prediction(
    predicted_margin=6.5,
    actual_margin=4
)

print(example)
