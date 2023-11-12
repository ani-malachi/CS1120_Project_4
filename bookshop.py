class Bookshop:
    def __int__(self, orders):
        self.orders = orders

    
    def get_order_number(self):
        return self.orderNumber
    def get_quanity(self):
        return self.quanity
    def get_price_per_item(self):
        return self.pricePerItem
        
    def set_order_number(self, orderNumber):
        self.orderNumber = orderNumber
    def set_quanity(self, quanity):
        self.quanity = quanity
    def set_price_per_item(self, pricePerItem):
        self.pricePerItem = pricePerItem
        
    def method1(self):
        m = [(order[0], *(map(lambda x: (x[0], x[1] * x[2] + 10 if (x[1] * x[2]) < 100 else x[1] * x[2]), order[1:])))
             for order in self.orders]
        return m
        # for each order in orders, lists book order num and price, plus 10 if the result is over 100
        # the * before map shows to unpack the items within the tuples
        # returns same list but the tuple w/ 2 items only
        # items r ( order num, quantity * price )
    
    def method2(self):
        print("method2")
        # filter out minimum price of product, 4 tuples
        # has order num, then which order has the least amnt total
        # so get the quantity * price and return the lowest one
        
    def method3(self):
        print("method3")
        # filters out the maximum price ? so same thing as before
        # so order num, then order w the highest total amnt

    def method4(self):
        order = self.orders
        book_order = []  # new list
        for i in order:
            num = 0
            for k in i[1:]:
                num += ((k[1]) * (k[2]))  # adds price * quantity

            book_order.append((i[0], round(num, 2)))  # adds all prices together to list for each order num

        return book_order
        # returns tuples w bookshop order number and then price * quantity?
        # so ( bookshop order number, total price of order )
        # so add all total amnt together and return it

    def method5(self):
        # use method 1 to get totals
        order5 = self.method1()
        answ = {}
        for i in order5:
            for j in i[1:]:
                if j[0] in answ:
                    answ[j[0]] += j[1]
                else:
                    answ.update({j[0]: j[1]})
        # dictionary filled with the numbers and their totals
        max_val = max(answ.values())  # finds max value
        max_key = max(answ, key=answ.get)  # finds max key
        x = [max_key, max_val]
        return x
        # returns list w two items, book order num and total amount of product in all order
        # returns order num that has max total amount of product in all order (??)
        # returns order num, which pops up multiple times, w the most amnt and the total

    def method6(self):
        print("method6")
        # same as before but total quantity? so amount of books in order
        # so which order gets ordered the most w highest quantity added together

    def method7(self):
        order = self.orders
        # get the whole order
        bookshop_order = map(lambda x: (x[0], list(map(lambda y: y[1], x[1:]))), order)
        # sums the second element of each tuple
        new_order = map(lambda x: (x[0], reduce(lambda a, b: a + b, x[1])), bookshop_order)
        new_order = list(new_order)  # makes it into list
        new_order.sort(key=lambda x: x[1], reverse=True)  # sorts final list
        return new_order
        # returns an ordered list based on bookshop order num, per maximum total quantity
        # [(max bookshop order number, total quantity)....(min bookshop order num, total quantity)]

    def method8(self):
        print("method8")
        # returns a total quantity of all books ordered
        # just a value no list or anything

    def method9(self):
        order5 = self.orders
        # similar to method 5, we go through with a dictionary
        answ = {}
        for i in order5:
            for j in i[1:]:
                if j[0] in answ:
                    answ[j[0]] += 1  # adds one when an order number is the same
                else:
                    answ.update({j[0]: 1})
        # dictionary filled with the numbers and the times they appear
        max_key = max(answ, key=answ.get)  # finds max key
        min_key = min(answ, key=answ.get)
        x = [max_key, min_key]
        return x
        # returns a list w two items
        # most ordered book, book order num, and the least ordered ( book order num)
        # count the occurrence of book order number in all orders

    def method10(self):
        print("method10")
        # returns a list w/ 4 items
        # each item represents length of sublist from index - to index 3
