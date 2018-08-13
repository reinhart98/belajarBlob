from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket('deep-freehold-213203.appspot.com')
blob = bucket.get_blob('new.yml')
with open('new.yml', 'wb') as file_obj:
	blob.download_to_file(file_obj)	