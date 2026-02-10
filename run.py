from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

# {
#   "firstName": "Amit",
#   "middleName": "Kumar",
#   "lastName": "Sharma",
#   "companyName": "Sharma Transport Services",
#   "companyEmail": "info@sharmatransport.com",
#   "companyPhone": "9123456780",
#   "companyAddress": "Sector 18, Transport Nagar",
#   "city": "Delhi",
#   "state": "Delhi",
#   "pincode": "110085",
#   "country": "India"
# }
