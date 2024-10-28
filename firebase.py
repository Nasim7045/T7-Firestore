import firebase_admin
from firebase_admin import credentials, firestore

# Hard-coded service account key
service_account_info = {
    "type": "service_account",
    "project_id": "t7-securities",
    "private_key_id": "0e5c5e94778981baa6c863c9290aab6e0a7a71c4",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDoWcF4cIlcCM00\nJJfBJfSb6DELoOXdSGbXWE4yuRY1uW1/iSb490giKldDUcj8zmT36CoAc8gEWb3G\ns3xuMXK7hCkTXVfWhAI8XZxfl24HVFvk65oAKE0r9v5KbhH2XJljDIKzHCDmIrI7\nFY4kB5FbH7CIwdFZZf+S4RWcjTIWIly4sdiolW1flhsgaVPtQoOf02Z4prnCh+Po\nEnBRd84X7snLRiQiME833znOWzg+9wtPVi5kiz6OMB6Fzean/M3uTvL94gGU4XkQ\n+s48annXJdfjuH2tDrMYj4WQxOvZylSNLBWk6qnozfIat+ctFkfbvDT0pnuPxAZ6\nn5/p+AmnAgMBAAECggEAWUOyWm0RuHQBMhkk3CWS1hrcTNVhuiPIrs7ULBSDfdxh\nPvAYMun9onKV190h1E4O6FcfW9EfdNxtVls6YLNKmtPpW/Euf9FzcnGcU/U/Zj14\nmHgTUCArlcpsY3fqGrX0j+MMi3cxBHkr9BsR4rGtnE6Oadvca/YNvAYRYXW1Wl7Z\nybgjUndpFXbEZYd5vhLvHl2aiYRpJg+d/i/4Ye9MlsF7EScvZn72dHicuDyU0dH4\nBwe7ibE4cIG1gbtsXx5QLvHMHchyTqdQoZYhyUWB95lnqUd0yliLhcqTTZmct7rg\nLBkGr7hVTLlSIhJnRj+7T/Devv4GCodu8zHwGGNj4QKBgQD3cvhtToY2rMFKJRRR\n7DnCEMRcbqzUYo8SDRF7YLwEWnOiOGWc3uxP1HLl0lKvaNnoie5j4zb/CJaGVHY7\nwh/Yi4pT4ayREUIUGhtWUv5K+QkZJm7ey0uwoMBTzp7GQ2tga3D45okHwDf87mlZ\nl7qJA0bLmvqaTiqRdjiAQojNaQKBgQDwYTffmiDUGsQfXvnVBvHjHnnFAoYZu7d2\nOhylxr6b/EFSssKW3PSZabyPB4Ju8hEUHp5TBXWoVRQiZYNd7HHcLX1v/22/Lg5P\nVr7l1Gc1bLWNJ7smw4excvf0kWVtQV+1AFlAUp1eMAB2/87VkD53nVeiP+YcBPcV\n8ZVvJB1sjwKBgGU4KlbMICqNUCO8NyurrZSstyX4P8pA5rVDkzscvswpE9PvreEV\nbyTYiodoGVqXUUvF4DYL45s/MBOSySp4pf42VkcpsSVGIfmHFFeja1HPvOEEz6Vj\nE3sUxpeBlYEUYv/18yhdZQA+qKhV/dIgNrWFGZh/tLMZ9l+6NDKDBOLBAoGARWGK\nIvv1pcLkALoFGjua7ZcKRpbn5d2Moo87XY3zzkoNALWf/LNh1jXyusXMHAG6dDgy\nMnxM7X1BBnyOYjmw04A9yGnNX3UHpFbBWsznzT/HVyq0lgexzsIEV47v240W9sNW\n/33Y9iqct7w2EuZDYXsEpEwVOtkkCC1mmGGwLHkCgYEAkF9Uv9ZVBbOM9rjgWwST\nnRjk02RhPFEWvYxVNL7l735T7XX3uWRvMq2z4D+3SjUgY/htzhU7y5JT8uv10yKp\nb3TK+oc139K1rRPPEoj5VYRZ/AOFeouijsN3YRLHsaCKce2BG8S+Bsq76xxqDQqm\nF26OAHKrXy9w7prz1Z91V7M=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-7f5c5@t7-securities.iam.gserviceaccount.com",
    "client_id": "109777960870820502186",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-7f5c5%40t7-securities.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

# Initialize Firebase Admin using the hard-coded key
cred = credentials.Certificate(service_account_info)
firebase_admin.initialize_app(cred)

# Get Firestore instance
db = firestore.client()
