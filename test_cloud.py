from google.cloud import firestore

# Connect to the project you just set up
db = firestore.Client(project="nifty-jet-484012-e5")

def launch_breliant():
    doc_ref = db.collection('logistics_audits').document('cloud_shell_test')
    doc_ref.set({
        'status': 'ALIVE',
        'location': 'Memphis, TN',
        'message': 'No more glitches! bReliant is in the Cloud.'
    })
    print("✅ SUCCESS! Check your Firestore browser tab!")

if __name__ == "__main__":
    launch_breliant()

