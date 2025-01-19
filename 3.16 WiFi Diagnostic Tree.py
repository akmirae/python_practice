# 3.16 WiFi Diagnostic Tree

def wifi_diagnostic():
    # Step 1
    diagnostic = input("Reboot the computer and try to connect.\nDid that fix the problem? (yes or no): ").strip().lower()
    if diagnostic == "yes":
        print("\nThank you for contacting us!")
        return
    
    # Step 2
    diagnostic_01 = input("Reboot the router and try to connect.\nDid that fix the problem? (yes or no): ").strip().lower()
    if diagnostic_01 == "yes":
        print("\nThank you for contacting us!")
        return
    
    # Step 3
    diagnostic_02 = input("Make sure the cables between the router and modem are plugged in firmly.\nDid that fix the problem? (yes or no): ").strip().lower()
    if diagnostic_02 == "yes":
        print("\nThank you for contacting us!")
        return
    
    # Step 4
    diagnostic_03 = input("Move the router to a new location and try to connect.\nDid that fix the problem? (yes or no): ").strip().lower()
    if diagnostic_03 == "yes":
        print("\nThank you for contacting us!")
        return
    
    # Step 5
    print("Get a new router.")

# Run the diagnostic function
wifi_diagnostic()
   

    