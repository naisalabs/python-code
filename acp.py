student_data = {
    "id1": {"name": "naisa", "class": "IV", "subject_integation": "english"},
    "id2": {"name": "sara", "class": "V", "subject_integation": "math"},
    "id3": {"name": "david", "class": "III", "subject_integation": "science"},
    "id4": {"name": "surya", "class": "I", "subject_integation": "islamic_studies"},
}
result = {}
seen_keys = []
for student_id,details in student_data.items():
    unique_key = (details["name"], details["class"],
        details["subject_integation"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details
        #print output line by line
        for k, v in result.items():
            print(k,":", v)
