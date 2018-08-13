from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket('deep-freehold-213203.appspot.com')
blob = bucket.blob('test1.yml') # membuat file .yml
blob.upload_from_string('12122121') # mengupload file .yml dengan contentx
print(blob.path)