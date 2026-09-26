ext = input("").strip().lower()

if ext[-4:] == ".gif":
    print("image/gif")
elif ext[-4:] == ".jpg" or ext[-5:] == ".jpeg":
    print("image/jpeg")
elif ext[-4:] == ".png":
    print("image/png")
elif ext[-4:] ==".pdf":
    print("application/pdf")
elif ext[-4:] == ".txt":
    print("text/plain")
elif ext[-4:] == ".zip":
    print("application/zip")
else:
    print("application/octet-stream")
