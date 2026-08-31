import os
import json
import csv

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
CSV_PATH = os.path.join(BASE_DIR, "scripts/pipeline/constituency_master.csv")
JSON_PATH = os.path.join(BASE_DIR, "src/data/realGovernanceData.json")
PUBLIC_DIR = os.path.join(BASE_DIR, "public")
REPORT_PATH = os.path.join(BASE_DIR, "photo_coverage_report.md")

def check_photo_exists(photo_url):
    """
    Returns True if the photoUrl points to a real, valid image file on disk (> 1KB)
    and is not the placeholder avatar.
    """
    if not photo_url or "placeholder-avatar" in photo_url:
        return False, "Placeholder Avatar"
    
    # Strip base path e.g. /my-leader/assets/... -> public/assets/...
    clean_path = photo_url
    if clean_path.startswith("/my-leader/"):
        clean_path = clean_path.replace("/my-leader/", "")
    elif clean_path.startswith("/"):
        clean_path = clean_path.lstrip("/")
        
    local_file_path = os.path.join(PUBLIC_DIR, clean_path)
    
    if os.path.exists(local_file_path):
        size = os.path.getsize(local_file_path)
        if size > 1000:
            return True, f"Present ({size//1024} KB)"
        else:
            return False, "File too small / Corrupt"
    else:
        return False, f"Missing file: {clean_path}"

def run_photo_audit():
    print(f"Loading Master CSV from: {CSV_PATH}")
    
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        records = list(reader)
        
    total_constituencies = len(records)
    
    state_stats = {}
    missing_by_state = {}
    present_by_state = {}
    
    for r in records:
        state = r['state']
        district = r['district']
        code = r['constituency_code']
        c_name = r['constituency_name']
        person = r['elected_person']
        role = r['role']
        party = r['party']
        photo = r['photo_source_url']
        
        is_present, status_msg = check_photo_exists(photo)
        
        if state not in state_stats:
            state_stats[state] = {"total": 0, "present": 0, "missing": 0}
            missing_by_state[state] = []
            present_by_state[state] = []
            
        state_stats[state]["total"] += 1
        
        item = {
            "state": state,
            "district": district,
            "code": code,
            "constituency": c_name,
            "person": person,
            "role": role,
            "party": party,
            "photo_url": photo,
            "status": status_msg
        }
        
        if is_present:
            state_stats[state]["present"] += 1
            present_by_state[state].append(item)
        else:
            state_stats[state]["missing"] += 1
            missing_by_state[state].append(item)
            
    # Generate Markdown Report
    total_present = sum(s['present'] for s in state_stats.values())
    total_missing = sum(s['missing'] for s in state_stats.values())
    overall_coverage = (total_present / total_constituencies) * 100 if total_constituencies > 0 else 0
    
    md_lines = []
    md_lines.append("# NetaPulse Candidate Photo Coverage Audit Report\n")
    md_lines.append(f"**Total Constituencies / Representatives Audited**: `{total_constituencies}`\n")
    md_lines.append(f"**Total Photos Present**: `{total_present}` ({overall_coverage:.1f}%)\n")
    md_lines.append(f"**Total Photos Missing (Using Placeholder)**: `{total_missing}` ({(100 - overall_coverage):.1f}%)\n")
    md_lines.append("\n---\n")
    
    md_lines.append("## State-wise Summary Table\n")
    md_lines.append("| State | Total Seats | Photos Present | Photos Missing | Coverage % |")
    md_lines.append("| :--- | :---: | :---: | :---: | :---: |")
    for st, stats in state_stats.items():
        cov = (stats['present'] / stats['total']) * 100 if stats['total'] > 0 else 0
        md_lines.append(f"| **{st}** | {stats['total']} | {stats['present']} | {stats['missing']} | {cov:.1f}% |")
        
    md_lines.append("\n---\n")
    
    # Detailed missing listings per state
    md_lines.append("## Missing Candidate Photos by State\n")
    for st, m_list in missing_by_state.items():
        md_lines.append(f"### {st} ({len(m_list)} missing)\n")
        if not m_list:
            md_lines.append("_All candidate photos are present for this state!_\n")
            continue
            
        md_lines.append("| Code | Constituency | District | Elected Representative | Party | Status |")
        md_lines.append("| :--- | :--- | :--- | :--- | :--- | :--- |")
        for m in m_list:
            md_lines.append(f"| {m['code']} | {m['constituency']} | {m['district']} | **{m['person']}** | {m['party']} | `{m['status']}` |")
        md_lines.append("\n")
        
    # Write to file
    with open(REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write("\n".join(md_lines))
        
    print(f"\n=======================================================")
    print(f"Photo Coverage Audit Completed!")
    print(f"Total Constituencies: {total_constituencies}")
    print(f"Total Present: {total_present} ({overall_coverage:.1f}%)")
    print(f"Total Missing: {total_missing} ({(100 - overall_coverage):.1f}%)")
    print(f"Detailed report saved to: {REPORT_PATH}")
    print(f"=======================================================\n")
    
    for st, stats in state_stats.items():
        cov = (stats['present'] / stats['total']) * 100 if stats['total'] > 0 else 0
        print(f" - {st}: {stats['present']}/{stats['total']} present ({cov:.1f}%), {stats['missing']} missing")

if __name__ == "__main__":
    run_photo_audit()
