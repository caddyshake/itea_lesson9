a = 1.233
b = 12.343

a_dollars = "${:.3f}".format(a)  # make strings with leading dollar sign
b_dollars = "${:.3f}".format(b)

a_padded = "foo:{:>8}".format(a_dollars)  # insert them into strings with padding
b_padded = "foo:{:>8}".format(b_dollars)
print(a_dollars)