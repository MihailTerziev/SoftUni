class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


email = input()

while not email == "End":
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = email.split('@')

    if len(name) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    valid_domains = [".com", ".bg", ".org", ".net"]

    for valid_domain in valid_domains:
        if not domain.endswith(valid_domain):
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
        else:
            break

    print("Email is valid")
    email = input()
