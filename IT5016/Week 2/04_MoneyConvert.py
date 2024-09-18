"""
Program which converts New Zealand dollars to Australian Dollars and vice versa
Author: Sukhjyot Singh
"""

nzd = float(input("Enter Amount in NZD: "))
aud = float(input("Enter Amount in AUD: "))

nzd_to_aud = nzd * 0.95
aud_to_nzd = aud / 0.95

print("NZD to AUD Amount: $", nzd_to_aud, sep="")
print("AUD to NZD Amount: $", aud_to_nzd, sep="")

