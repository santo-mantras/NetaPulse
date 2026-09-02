import csv

GOA_OFFICIAL_MLAS_2022 = {
    "Mandrem": ("Jit Arolkar", "Maharashtrawadi Gomantak Party"),
    "Pernem (SC)": ("Pravin Arlekar", "Bharatiya Janata Party"),
    "Pernem": ("Pravin Arlekar", "Bharatiya Janata Party"),
    "Bicholim": ("Dr. Chandrakant Shetye", "Independent"),
    "Tivim": ("Nilkanth Halarnkar", "Bharatiya Janata Party"),
    "Mapusa": ("Joshua D'Souza", "Bharatiya Janata Party"),
    "Siolim": ("Delilah Lobo", "Indian National Congress"),
    "Saligao": ("Kedar Naik", "Indian National Congress"),
    "Calangute": ("Michael Lobo", "Indian National Congress"),
    "Porvorim": ("Rohan Khaunte", "Bharatiya Janata Party"),
    "Aldona": ("Carlos Alvares Ferreira", "Indian National Congress"),
    "Panaji": ("Atanasio Monserrate", "Bharatiya Janata Party"),
    "Taleigao": ("Jennifer Monserrate", "Bharatiya Janata Party"),
    "St. Cruz": ("Rodolfo Fernandes", "Indian National Congress"),
    "St. Andre": ("Viresh Borkar", "Revolutionary Goans Party"),
    "Cumbarjua": ("Rajesh Faldessai", "Indian National Congress"),
    "Maem": ("Premendra Shet", "Bharatiya Janata Party"),
    "Sanquelim": ("Pramod Sawant", "Bharatiya Janata Party"),
    "Poriem": ("Deviya Vishwajit Rane", "Bharatiya Janata Party"),
    "Valpoi": ("Vishwajit Pratapsingh Rane", "Bharatiya Janata Party"),
    "Priol": ("Govind Gaude", "Bharatiya Janata Party"),
    "Ponda": ("Ravi Naik", "Bharatiya Janata Party"),
    "Siroda": ("Subhash Shirodkar", "Bharatiya Janata Party"),
    "Marcaim": ("Sudin Dhavalikar", "Maharashtrawadi Gomantak Party"),
    "Mormugao": ("Sankalp Amonkar", "Indian National Congress"),
    "Vasco da Gama": ("Krishna Salkar", "Bharatiya Janata Party"),
    "Dabolim": ("Mauvin Godinho", "Bharatiya Janata Party"),
    "Cortalim": ("Antonio Vas", "Independent"),
    "Nuvem": ("Aleixo Sequeira", "Indian National Congress"),
    "Curtorim": ("Aleixo Reginaldo Lourenco", "Independent"),
    "Fatorda": ("Vijai Sardesai", "Goa Forward Party"),
    "Margao": ("Digambar Kamat", "Indian National Congress"),
    "Benaulim": ("Venzy Viegas", "Aam Aadmi Party"),
    "Navelim": ("Ulhas Tuenkar", "Bharatiya Janata Party"),
    "Cuncolim": ("Yuri Alemao", "Indian National Congress"),
    "Velim": ("Cruz Silva", "Aam Aadmi Party"),
    "Quepem": ("Altone D'Costa", "Indian National Congress"),
    "Curchorem": ("Nilesh Cabral", "Bharatiya Janata Party"),
    "Sanvordem": ("Ganesh Gaonkar", "Bharatiya Janata Party"),
    "Sanguem": ("Subhash Phal Desai", "Bharatiya Janata Party"),
    "Canacona": ("Ramesh Tawadkar", "Bharatiya Janata Party")
}

def audit_and_fix_goa():
    csv_path = "scripts/pipeline/constituency_master.csv"
    with open(csv_path, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    fieldnames = rows[0].keys()
    fixed = 0

    for r in rows:
        if r['state'] == "Goa":
            cname = r['constituency_name'].strip()
            if cname in GOA_OFFICIAL_MLAS_2022:
                official_name, official_party = GOA_OFFICIAL_MLAS_2022[cname]
                if r['elected_person'] != official_name:
                    print(f"Fixing Goa {cname}: '{r['elected_person']}' -> '{official_name}' ({official_party})")
                    r['elected_person'] = official_name
                    r['party'] = official_party
                    r['bio'] = f"{official_name} is the elected MLA representing {cname}, {r['district']}, Goa."
                    fixed += 1

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nAudit complete: Fixed {fixed} seats in Goa.")

if __name__ == "__main__":
    audit_and_fix_goa()
