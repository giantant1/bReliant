from google.cloud import firestore
import re
from thefuzz import process, fuzz

# 1. Connect to your Google Cloud Project (nifty-jet-484012-e5)
db = firestore.Client(project="nifty-jet-484012-e5")

# 2. The Universal Gold Standard 
# Combining Logistics Hubs and Medical Neuroanatomy Terms
VALID_TERMS = [
    "MEMPHIS", "NASHVILLE", "KNOXVILLE", "CHATTANOOGA", "FEDEX", 
    "CEREBELLUM", "OCCIPITAL", "GLIOBLASTOMA", "MENINGIOMA"
]

def breliant_universal_cleaner(messy_input, audit_id):
    # Step A: Rigid Cleaning (Formatting)
    # Strip dashes/zeros and convert to uppercase
    step1 = re.sub(r'[^a-zA-Z0-9]', '', messy_input).upper().strip()
    
    # Step B: Smart Sensing (Fuzzy Matching)
    # Using partial_ratio to find 'CEREBELLUM' inside 'Cere-bell-um-Lab'
    best_match, score = process.extractOne(step1, VALID_TERMS, scorer=fuzz.partial_ratio)
    
    # Step C: Decision Logic
    # 80% is the 'New Collar' threshold for trust
    if score > 80:
        final_data = best_match
        status = "AUTO_FIXED"
    else:
        final_data = step1
        status = "CLEANED"
    
    # Step D: Log to Cloud (Multi-Industry Audit)
    doc_ref = db.collection('logistics_audits').document(audit_id)
    doc_ref.set({
        'raw_input': messy_input,
        'refined_output': final_data,
        'confidence_score': score,
        'status': status,
        'industry_sensing': "Medical" if any(x in final_data for x in ["CERE", "GLIO", "MENIN"]) else "Logistics"
    })
    return final_data, score

# --- THE UNIVERSAL BATCH TEST ---

mixed_industry_data = [
    "  000-Mempis-901  ",     # Logistics Typo
    "Glio-Blast-oma-Scan",     # Medical Typo
    "  Cere-bell-um-Lab-  ",   # Medical Format issue
    "Mening-ioma-901",         # Medical + Logistics hybrid
    "Fedx-Express-TN"          # Logistics Typo
]

print("--- bReliant Universal Processing: START ---")

for i, item in enumerate(mixed_industry_data):
    current_id = f"universal_audit_{i}"
    result, confidence = breliant_universal_cleaner(item, current_id)
    print(f"ID {i}: Input [{item}] -> Result [{result}] ({confidence}%)")

print("--- Processing COMPLETE. Check Firestore! ---")






