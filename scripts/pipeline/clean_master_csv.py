import csv

def normalize_districts():
    filename = "scripts/pipeline/constituency_master.csv"
    with open(filename, "r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))

    fieldnames = reader[0].keys()

    # Normalization map
    up_map = {
        'Ayodhya (Faizabad)': 'Ayodhya',
        'Prayagraj (Allahabad)': 'Prayagraj',
        'Gautam Buddha Nagar (Noida)': 'Gautam Buddha Nagar'
    }

    ka_map = {
        'Bangalore Urban': 'Bengaluru Urban',
        'Bangalore Rural': 'Bengaluru Rural',
        'Mysore': 'Mysuru',
        'Shimoga': 'Shivamogga',
        'Dharwad': 'Dharwad',
        'Dharwad & Hubballi': 'Dharwad',
        'Dakshina Kannada (Mangaluru)': 'Dakshina Kannada',
        'Chikmagalur': 'Chikkamagaluru'
    }

    pb_map = {
        'Rupnagar & SAS Nagar (Mohali)': 'SAS Nagar (Mohali)'
    }

    cleaned_rows = []
    # Deduplicate strictly on (state.lower(), constituency_name.lower())
    seen = {}
    for r in reader:
        st = r['state'].strip()
        dist = r['district'].strip()
        cname = r['constituency_name'].strip()

        if st == "Uttar Pradesh" and dist in up_map:
            dist = up_map[dist]
        elif st == "Karnataka" and dist in ka_map:
            dist = ka_map[dist]
        elif st == "Punjab" and dist in pb_map:
            dist = pb_map[dist]

        r['district'] = dist
        key = (st.lower(), cname.lower())

        # If duplicate, prefer row that already had detailed biography or custom data
        if key in seen:
            prev = seen[key]
            # If current row has specific assets/photos and previous had defaults, keep the better one
            if r.get('photo_source_url', '') != '/assets/placeholder-avatar.svg' and prev.get('photo_source_url', '') == '/assets/placeholder-avatar.svg':
                seen[key] = r
        else:
            seen[key] = r

    final_rows = list(seen.values())

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(final_rows)

    print(f"Normalized and deduplicated down to {len(final_rows)} clean constituency rows.")

if __name__ == "__main__":
    normalize_districts()
