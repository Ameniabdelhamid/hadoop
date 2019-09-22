import csv
import random
import string



def randomString(stringLength):
    """Generate a random string with the combination of lowercase and uppercase letters """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))


with open('productdb.csv', 'w') as csvfile:
    i = 0
    while i < 10000000:
        i += 1
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        d = random.randint(0, 100000)
        nb = str(d)
        name = nb + "Product"
        price = random.uniform(2.5, 5000.5)
        idprod = randomString(8) + str(i)
        image = "https://www.google.com/search?biw=1366&bih=672&tbm=isch&sa=1&ei=rTndXLSMJ4vFUpXOhsAJ&q=grocery+products+jpeg&oq=grocery+products+jpeg&gs_l=img.3...19341.21093..21388...0.0..0.898.1760.6-2......1....1..gws-wiz-img.Wmqatzgw304#imgdii=poMuxU0ccc61lM:&imgrc=INhWlgHo-gyMqM:"
        if i in range(1, 10001):
            c = random.randint(5, 10)
            categ = "Category" + str(c)
            b= random.randint(25, 50)
            brand = "Brand" + str(b)
        if i in range(10002, 50001):
            c = random.randint(15, 20)
            categ = "Category" + str(c)
            b = random.randint(35, 40)
            brand = "Brand" + str(b)
        if i in range(50002, 100001):
            c = random.randint(5, 10)
            categ = "Category" + str(c)
            b = random.randint(55, 60)
            brand = "Brand" + str(b)




        filewriter.writerow([idprod, name, price, categ, brand, image])
