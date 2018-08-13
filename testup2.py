from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket('deep-freehold-213203.appspot.com')
blob = bucket.blob('new.yml')
blob.upload_from_filename('/home/odroid/belajar/testupload.py')
