import qrcode
# taking upi id as input
upi_id=input("Enter your upi id=")

# payment url=
# upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# defining payment url based on upi id and payment app,,,you can modify these urls based on payments apps you want to support

phonepe_url= f'upi://pay?pa={upi_id}&pn=YourName&cu=INR&am=100&tn=Thank you for your support!'
paytm_url= f'upi://pay?pa={upi_id}&pn=YourName&cu=INR&am=100&tn=Thank you for your support!'
google_pay_url= f'upi://pay?pa={upi_id}&pn=YourName&cu=INR&am=100&tn=Thank you for your support!'

# create qr codes for each app
phonepe_qr= qrcode.make(phonepe_url)
paytm_qr= qrcode.make(paytm_url)
google_pay_qr= qrcode.make(google_pay_url)

# save thes qr code image files
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# display qr using pil viewer library
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
