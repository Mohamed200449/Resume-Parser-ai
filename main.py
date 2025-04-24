import pandas as pd

def calculate_score(job_requirements, candidate_skills):
    match_count = sum(1 for word in job_requirements if word in candidate_skills)
    return match_count

def find_best_candidate(job_requirements, candidate_profiles):
    best_candidate = None
    best_score = 0

    for _, candidate in candidate_profiles.iterrows():
        candidate_skills = [skill.strip().lower() for skill in candidate['skills'].split(',')]
        experience = candidate['experience']
        communication = candidate['communication_skills'].lower()

        score = calculate_score(job_requirements, candidate_skills)
        score += experience

        if communication == 'excellent':
            score += 2
        elif communication == 'good':
            score += 1

        if score > best_score:
            best_candidate = candidate
            best_score = score

    return best_candidate

def print_candidate(candidate):
    if candidate is not None:
        print("✅ أفضل مرشح للوظيفة:")
        print(f"الاسم: {candidate['name']}")
        print(f"المهارات: {candidate['skills']}")
        print(f"الخبرة: {candidate['experience']} سنة")
        print(f"مهارات التواصل: {candidate['communication_skills']}")
        print(f"الدرجة النهائية: {best_score}")
    else:
        print("لا يوجد مرشح مناسب حالياً.")

def get_job_requirements():
    print("اكتب المهارات المطلوبة (مفصولة بفاصلة):")
    return [skill.strip().lower() for skill in input().split(',')]

def main():
    job_requirements = get_job_requirements()
    candidate_profiles = pd.read_csv("candidates_dataset_with_real_names.csv")
    best_candidate = find_best_candidate(job_requirements, candidate_profiles)
    print_candidate(best_candidate)

if __name__ == "__main__":
    main()
# Main code will go here
