message = "The quick, brown, fox jumped over the lazy river"
print(message.split(','))
the_array = ["I", "am", "here"]
print(','.join(the_array))
m1 = "JIMMER"
m2 = "jimmer"
m3 = "1234"
m4 = "jimmer1234"

print(m3.isalpha())
if m4.find(m1) != -1:
    print(m4[0:m4.find(m3)])