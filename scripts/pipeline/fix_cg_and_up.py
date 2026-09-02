import csv

def fix_remaining():
    csv_path = "scripts/pipeline/constituency_master.csv"
    with open(csv_path, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    fieldnames = rows[0].keys()
    fixed = 0

    for r in rows:
        st = r['state'].strip()
        cname = r['constituency_name'].strip()

        # 1. Chhattisgarh: Arang (SC)
        if st == "Chhattisgarh" and "Arang" in cname:
            r['elected_person'] = "Guru Khushwant Saheb"
            r['party'] = "Bharatiya Janata Party"
            r['bio'] = f"Guru Khushwant Saheb is the elected MLA representing {cname}, {r['district']}, Chhattisgarh."
            fixed += 1
            print("Fixed Arang -> Guru Khushwant Saheb (BJP)")

        # 2. Chhattisgarh: Mohla-Manpur (ST)
        elif st == "Chhattisgarh" and "Mohla" in cname:
            r['elected_person'] = "Indrashah Mandavi"
            r['party'] = "Indian National Congress"
            r['bio'] = f"Indrashah Mandavi is the elected MLA representing {cname}, {r['district']}, Chhattisgarh."
            fixed += 1
            print("Fixed Mohla-Manpur -> Indrashah Mandavi (INC)")

        # 3. Uttar Pradesh: Colonelganj
        elif st == "Uttar Pradesh" and cname == "Colonelganj":
            r['elected_person'] = "Ajay Kumar Singh"
            r['party'] = "Bharatiya Janata Party"
            r['bio'] = f"Ajay Kumar Singh is the elected MLA representing Colonelganj, Gonda, Uttar Pradesh."
            fixed += 1
            print("Fixed Colonelganj -> Ajay Kumar Singh (BJP)")

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nSuccessfully applied {fixed} final candidate name fixes!")

if __name__ == "__main__":
    fix_remaining()
