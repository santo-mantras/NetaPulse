import csv
import json

def update_master_with_real_names():
    csv_path = "scripts/pipeline/constituency_master.csv"
    with open(csv_path, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    fieldnames = rows[0].keys()

    # Load corrected Karnataka and UP data
    with open("scripts/pipeline/ka_scraped_224.json", "r", encoding="utf-8") as f:
        ka_data = json.load(f)
    ka_lookup = {x['constituency_name'].strip().lower(): x for x in ka_data}

    with open("scripts/pipeline/up_scraped_403.json", "r", encoding="utf-8") as f:
        up_data = json.load(f)
    up_lookup = {x['constituency_name'].strip().lower(): x for x in up_data}

    ka_fixed = 0
    up_fixed = 0

    for r in rows:
        st = r['state'].strip()
        cname = r['constituency_name'].strip().lower()
        person = r['elected_person'].strip()

        # Check if placeholder
        is_placeholder = person.lower() in ['elected mla', 'elected representative', ''] or person.startswith('MLA ')

        if st == "Karnataka":
            if cname in ka_lookup:
                actual_name = ka_lookup[cname]['winner'].strip()
                actual_party = ka_lookup[cname]['party'].strip()
                if actual_name and is_placeholder:
                    r['elected_person'] = actual_name
                    if actual_party:
                        r['party'] = actual_party
                    r['bio'] = f"{actual_name} is the elected MLA representing {r['constituency_name']}, {r['district']}, Karnataka."
                    ka_fixed += 1
        elif st == "Uttar Pradesh":
            if cname in up_lookup:
                actual_name = up_lookup[cname]['winner'].strip()
                actual_party = up_lookup[cname]['party'].strip()
                if actual_name and is_placeholder:
                    r['elected_person'] = actual_name
                    if actual_party:
                        r['party'] = actual_party
                    r['bio'] = f"{actual_name} is the elected MLA representing {r['constituency_name']}, {r['district']}, Uttar Pradesh."
                    up_fixed += 1

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Fixed {ka_fixed} Karnataka placeholders with real MLA names.")
    print(f"Fixed {up_fixed} Uttar Pradesh placeholders with real MLA names.")

if __name__ == "__main__":
    update_master_with_real_names()
