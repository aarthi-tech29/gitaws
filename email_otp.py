import smtplib
import random

try:
    otp = random.randint(100000, 999999)

    sender = "aarthi.2205@gmail.com"
    password = "rppn rrrv raqn czdi"
    receiver = "aarthi.152529@gmail.com"

    # Check email format
    if "@gmail.com" not in sender:
        raise ValueError("Invalid Email")

    message = f"Subject: Your OTP\n\nYour OTP is {otp}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)

    server.sendmail(sender, receiver, message)
    server.quit()

    print("OTP sent to email!")

    # User enters OTP
    user_otp = int(input("Enter OTP: "))

    if user_otp == otp:
        print("✅ OTP Verified (TRY SUCCESS)")
    else:
        raise ValueError("Wrong OTP")

except ValueError as e:
    print("❌", e)

except smtplib.SMTPAuthenticationError:
    print("❌ Invalid email or password")

except Exception as e:
    print("❌ Error:", e)