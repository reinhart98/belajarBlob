from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket('deep-freehold-213203.appspot.com')
blob = bucket.get_blob('trainerv2.yml')
with open('trainerv2.yml', 'wb') as file_obj:
	blob.download_to_file(file_obj)	
