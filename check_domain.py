import dns.resolver

def check_domain(domain: str) -> str:
    """Проверка доменов и mx-записей"""
    try:
        """Проверяем существует ли домен (ns или a)"""
        try:
            dns.resolver.resolve(domain, 'A')
        except Exception:
            try:
                dns.resolver.resolve(domain, 'NS')
            except Exception:
                return "домен отсутствует"

        try:
            """Проверяем MX-записи"""
            mx_records = dns.resolver.resolve(domain, 'MX')
            if not mx_records:
                return "MX-записи отсутствуют или некорректны"
            return "домен валиден"
        except Exception:
            return "MX-записи отсутствуют или некорректны"

    except Exception:
        return "домен отсутствует"


def check_emails(emails: list[str]) -> None:
    for email in emails:
        if "@" not in email:
            print(f"{email}: некорректный email-формат")
            continue

        domain = email.split("@")[1]
        status = check_domain(domain)
        print(f"{email}: {status}")


if __name__ == "__main__":
    # Пример списка email-адресов
    test_emails = [
        "user@gmail.com",
        "info@nonexistent-domain-1234567.xyz",
        "sales@example.com",
        "support@yandex.ru",
        "bad-format-email"
    ]

    check_emails(test_emails)
