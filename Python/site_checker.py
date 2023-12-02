import urllib.request as urlib

def main(url):
    print("Checking Connectivity .........")
    print("------------------")
    response = urlib.urlopen(url)
    print("connected to " + "[ " +  url  + " ]" + " successfully")
    print("The Response code was : " , response.getcode())

print ("Welcome To The Website Connectivity Checker App")

print("------------------")

input_address = input("Please Enter the website Url (with [https://]): ")

print("------------------")


main(input_address)


print("------------------")

print ("Developer : Onai Hector")