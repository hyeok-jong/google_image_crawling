import google_images_download.google_images_download as gid

response = gid.googleimagesdownload()

arguments = {"keywords" : "한복 여자", "limit" : 5000, "print_urls" : True}

paths = response.download(arguments)

print(paths)
