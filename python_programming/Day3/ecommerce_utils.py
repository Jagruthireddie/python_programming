def apply_discount(p, d): 
    d_price = p- (p*d/100)
    return d_price
def add_gst(p, gst_per=18):
    price_with_gst = p+ (p * gst_per/100)
    return price_with_gst
def generate_invoice(c, d=0, gst_per=18):
    print("------ INVOICE ------")
    subtotal = 0
    for product, p in c.items():
        print(f"{product:<15}: ₹{p}")
        subtotal += p
    print("---------------------")
    print(f"Subtotal: ₹{subtotal}")
    if d> 0:
        subtotal_after_discount = apply_discount(subtotal, d)
        print(f"After {d}% discount: ₹{subtotal_after_discount}")
    else:
        subtotal_after_discount = subtotal
    total_with_gst = add_gst(subtotal_after_discount, gst_per)
    print(f"After {gst_per}% GST: ₹{total_with_gst:.2f}")
    print("---------------------")
    print("Thank you for shopping with us!")
