# Student Performance Analyzer
# Author: Jayasree Tamilvanan
# Description: Analyzes student marks and provides feedback

def get_marks():
    subjects = ["Math", "Science", "English", "Computer"]
    marks = {}

    print("Enter marks out of 100:\n")
    for subject in subjects:
        while True:
            try:
                score = int(input(f"{subject}: "))
                if 0 <= score <= 100:
                    marks[subject] = score
                    break
                else:
                    print("Please enter a number between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    return marks


def calculate_average(marks):
    total = sum(marks.values())
    return total / len(marks)


def find_weak_subjects(marks):
    weak = []
    for subject, score in marks.items():
        if score < 50:
            weak.append(subject)
    return weak


def give_suggestions(weak_subjects):
    if not weak_subjects:
        print("\nGreat job! No weak subjects detected.")
    else:
        print("\nSubjects that need improvement:")
        for subject in weak_subjects:
            print(f"- {subject}")
        print("\nSuggestion: Spend extra practice time on these subjects.")


def main():
    print("=== Student Performance Analyzer ===\n")

    marks = get_marks()
    average = calculate_average(marks)
    weak_subjects = find_weak_subjects(marks)

    print("\n--- Results ---")
    for subject, score in marks.items():
        print(f"{subject}: {score}")

    print(f"\nAverage Score: {average:.2f}")
    give_suggestions(weak_subjects)


if __name__ == "__main__":
    main()
