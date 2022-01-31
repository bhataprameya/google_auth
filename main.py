import pyotp
import qrcode

# This Should be a Secure Key and different for each user
otp = pyotp.TOTP("KRUGS4ZAKNUG65LMMQQGEZJAMEQFGZLDOVZGKICLMV4Q====")
print(otp.now())


def register():
    auth_string = otp.provisioning_uri(name="Test User", issuer_name="My test System", )
    # print(auth_string)
    img = qrcode.make(auth_string)
    img.show()
    while True:
        val = input("Enter current code to complete registration: ")
        if otp.now() == val:
            print("Registration Complete")
            break
        else:
            print("Wrong OTP please try again...")


def login():
    val = input("Enter your Google Authenticator to Login: ")
    if otp.now() == val:
        print("Login Successful")
    else:
        print("Login Failed please try again...")


register()
while True:
    login()
