class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None

    def insert_term(self, coefficient, exponent):
        new_term = Node(coefficient, exponent)

        if not self.head:
            self.head = new_term
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_term

    def display(self):
        current = self.head
        while current:
            print(f"{current.coefficient}x^{current.exponent}", end=" + " if current.next else "")
            current = current.next
        print()

def add_polynomials(poly1, poly2):
    result = Polynomial()

    current1, current2 = poly1.head, poly2.head

    while current1 and current2:
        if current1.exponent > current2.exponent:
            result.insert_term(current1.coefficient, current1.exponent)
            current1 = current1.next
        elif current1.exponent < current2.exponent:
            result.insert_term(current2.coefficient, current2.exponent)
            current2 = current2.next
        else:
            result.insert_term(current1.coefficient + current2.coefficient, current1.exponent)
            current1 = current1.next
            current2 = current2.next

    # Append remaining terms from both polynomials
    while current1:
        result.insert_term(current1.coefficient, current1.exponent)
        current1 = current1.next

    while current2:
        result.insert_term(current2.coefficient, current2.exponent)
        current2 = current2.next

    return result

def subtract_polynomials(poly1, poly2):
    result = Polynomial()

    current1, current2 = poly1.head, poly2.head

    while current1 and current2:
        if current1.exponent > current2.exponent:
            result.insert_term(current1.coefficient, current1.exponent)
            current1 = current1.next
        elif current1.exponent < current2.exponent:
            result.insert_term(-current2.coefficient, current2.exponent)  # Subtracting term
            current2 = current2.next
        else:
            result.insert_term(current1.coefficient - current2.coefficient, current1.exponent)
            current1 = current1.next
            current2 = current2.next

    # Append remaining terms from the first polynomial
    while current1:
        result.insert_term(current1.coefficient, current1.exponent)
        current1 = current1.next

    # Append remaining terms from the second polynomial with negated coefficients
    while current2:
        result.insert_term(-current2.coefficient, current2.exponent)
        current2 = current2.next

    return result

def multiply_polynomials(poly1, poly2):
    result = Polynomial()

    current1 = poly1.head
    while current1:
        current2 = poly2.head
        while current2:
            result.insert_term(current1.coefficient * current2.coefficient, current1.exponent + current2.exponent)
            current2 = current2.next
        current1 = current1.next

    return result

def divide_polynomials(poly1, poly2):
    if poly2.head is None:
        raise ValueError("Cannot divide by zero polynomial.")

    quotient = Polynomial()
    remainder = Polynomial()

    current1 = poly1.head
    while current1 and current1.coefficient == 0:
        current1 = current1.next

    current2 = poly2.head
    while current2 and current2.coefficient == 0:
        current2 = current2.next

    while current1 and current1.exponent >= current2.exponent:
        term_coefficient = current1.coefficient / current2.coefficient
        term_exponent = current1.exponent - current2.exponent

        quotient.insert_term(term_coefficient, term_exponent)

        # Update poly1 by subtracting term
        temp = Polynomial()
        temp.insert_term(term_coefficient, term_exponent)
        temp_result = multiply_polynomials(poly2, temp)
        current1 = subtract_polynomials(poly1, temp_result).head

    remainder = poly1

    return quotient, remainder

# Example usage:
poly1 = Polynomial()
poly1.insert_term(3, 2)
poly1.insert_term(5, 1)
poly1.insert_term(2, 0)

poly2 = Polynomial()
poly2.insert_term(4, 3)
poly2.insert_term(2, 1)
poly2.insert_term(1, 0)

print("Polynomial 1:")
poly1.display()

print("\nPolynomial 2:")
poly2.display()

sum_result = add_polynomials(poly1, poly2)
print("\nSum of Polynomials:")
sum_result.display()

difference_result = subtract_polynomials(poly1, poly2)
print("\nDifference of Polynomials:")
difference_result.display()

product_result = multiply_polynomials(poly1, poly2)
print("\nProduct of Polynomials:")
product_result.display()

quotient_result, remainder_result = divide_polynomials(poly1, poly2)
print("\nQuotient of Polynomials:")
quotient_result.display()
print("\nRemainder of Polynomials:")
remainder_result.display()
