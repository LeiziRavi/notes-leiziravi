# Show number in currency format, specify width
def currency(n, w=15):
    """Show in currency format, width = 15 or width of your choosing"""
    s = f"${n:,.2f}"
    # Pad left of output with spaces to width of w.
    return s.rjust(w)


# Show number in percent format, specify width.
def percent(n, w=15):
    """Show in percent format, width = 15 or width of your choosing """
    # Show in percent format
    s = f"{n:.1%}"
    # Pad left of output with spaces to width of w
    return s.ljust(w)

print(currency(9999))
print(currency(9999,20))
print(percent(0.065))
print(percent(0.065,20))