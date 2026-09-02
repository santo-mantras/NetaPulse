import csv
import re

TN_REMAINING_13 = {
    "Dr. R. K. Nagar": ("J. John Ebenezer", "Dravida Munnetra Kazhagam"),
    "Thiyagarayanagar": ("J. Karunanithi", "Dravida Munnetra Kazhagam"),
    "Sholinganallur": ("S. Aravind Ramesh", "Dravida Munnetra Kazhagam"),
    "Madurantakam": ("C. E. Sathya", "Dravida Munnetra Kazhagam"),
    "Sholinghur": ("A. M. Munirathinam", "Indian National Congress"),
    "Pappireddipatti": ("A. Govindasamy", "All India Anna Dravida Munnetra Kazhagam"),
    "Tiruchengodu": ("E. R. Eswaran", "Dravida Munnetra Kazhagam"),
    "Mettuppalayam": ("A. K. Selvaraj", "All India Anna Dravida Munnetra Kazhagam"),
    "Nilakkottai": ("S. Thenmozhi", "All India Anna Dravida Munnetra Kazhagam"),
    "Manapparai": ("P. Abdul Samad", "Dravida Munnetra Kazhagam"),
    "Tiruppattur": ("K. R. Periyakaruppan", "Dravida Munnetra Kazhagam"),
    "Thirumangalam": ("R. B. Udhayakumar", "All India Anna Dravida Munnetra Kazhagam"),
    "Colachal": ("J. G. Prince", "Indian National Congress")
}

def finalize_tn():
    csv_path = "scripts/pipeline/constituency_master.csv"
    with open(csv_path, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    fieldnames = rows[0].keys()
    fixed = 0

    for r in rows:
        if r['state'] == "Tamil Nadu":
            cname = r['constituency_name'].strip()
            clean_cname = re.sub(r'\s*\((?:SC|ST)\)', '', cname, flags=re.IGNORECASE).strip()
            
            if clean_cname in TN_REMAINING_13:
                name, party = TN_REMAINING_13[clean_cname]
                r['elected_person'] = name
                r['party'] = party
                r['bio'] = f"{name} is the elected MLA representing {cname}, {r['district']}, Tamil Nadu."
                fixed += 1

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Finalized all {fixed} remaining Tamil Nadu seats!")

if __name__ == "__main__":
    finalize_tn()
