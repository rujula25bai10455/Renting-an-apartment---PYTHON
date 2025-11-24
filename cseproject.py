import math

BASERENT = 1000.0
CSQFT = 1.5
CBEDS = 300.0

CBATHS = 250.0
PADJ ={
'90210': 1.50,
'10001': 1.40,
'94103': 1.25,
'78704': 1.10,
'46201': 0.80,
}
def prentlocal(sq_ft, bedrooms, bathrooms, pin_code):
    predict = BASERENT
    predict += sq_ft * CSQFT
    predict += bedrooms * CBEDS
    predict += bathrooms * CBATHS
    adjfactor = PADJ.get(pin_code, 1.0)
    frent = predict * adjfactor
    return round(frent)
def main():
    print("\n---RENT-PREDIcT Minimal Local Estimator ---")
    print("This version uses a simple internal formula, no external URLs or APIs")
    print("Please enter the property details:")
    try:
        sqft = int(input("Square Footage (e.g., 950): "))
        bedrooms = float(input("Bedrooms (e.g., 2.5): "))
        bathrooms = int(input("Bathrooms (e.g., 2): "))
        pincode = input("5-digit Pin Code (e.g., 90210):")
    except ValueError:
        print("\n[Error] Invalid number format. Please run the script again with correct numbers.")
        return
    if len(pincode) != 5 or not pincode.isdigit():
        print("\n[Error] Invalid Pin Code format. Must be 5 digits.")
        return 
    print("\n.Calculating price now .")
    try:
        pprice = prentlocal(sqft, bedrooms, bathrooms, pincode)
        print("\n--- ESTIMATE ---")
        print(f"The estimated monthly rent for a {sqft} sq. ft, {bedrooms} bed, {bathrooms} bath")
        print(f"apartment in Pin Code {pincode} is:")
        print(f"**${pprice:,.0f}**")
        print("\n--- FORMULA COMPONENTS ---")
        print(f"Base Cost: ${BASERENT:,.0f}")
        print(f"Sq. Ft. Contribution ${sqft * CSQFT:,.0f}")
        print(f"Bedroom Contribution: ${bedrooms * CBEDS:,.0f}")
        print(f"Bathroom Contribution: ${bathrooms * CBATHS:,.0f}")
        adjustment = PADJ.get(pincode, 1.0)
        print(f"Local Multiplier (from ZIP map): x{adjustment:.2f}")
        if adjustment == 1.0:
            print("Note: Zip code was not mapped, using default multiplier (1.0). ")
    except Exception as e :
        print(f"\n[Fatal Error] An internal calculation error occurred: {e}")

main()