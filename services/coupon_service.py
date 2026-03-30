def apply_coupon(total, code):
    if code == "SAVE10":
        return total * 0.9
    elif code == "FLAT200":
        return max(0, total - 200)
    return total