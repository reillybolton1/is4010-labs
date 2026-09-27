"""Week 05 Lab: user data helper functions.

This module provides two small utility functions for working with a list
of user dictionaries:

* ``calculate_average_age`` computes the average of the valid, numeric
  ages found in the user records.
* ``get_active_user_emails`` collects the email addresses of users who
  are marked active and who have an email on record.
"""


def calculate_average_age(users):
    """Return the average numeric age, or 0.0 when none are valid.

    Each user is expected to be a dictionary that may contain an "age"
    key. Users missing the "age" key, or whose "age" value is not a
    number (int or float), are ignored. Boolean values are also treated
    as non-numeric ages, since ``bool`` is technically a subclass of
    ``int`` in Python but does not represent an age.

    Args:
        users: An iterable of user dictionaries.

    Returns:
        The average of all valid numeric ages as a float. If there are
        no valid ages, returns 0.0.
    """
    valid_ages = []

    for user in users:
        age = user.get("age")

        if isinstance(age, bool):
            continue

        if isinstance(age, (int, float)):
            valid_ages.append(age)

    if not valid_ages:
        return 0.0

    return sum(valid_ages) / len(valid_ages)


def get_active_user_emails(users):
    """Return email addresses belonging to active users.

    Each user is expected to be a dictionary that may contain an
    "is_active" key and an "email" key. A user's email is included in
    the result only when "is_active" is truthy and the "email" key is
    present in the dictionary.

    Args:
        users: An iterable of user dictionaries.

    Returns:
        A list of email addresses for active users. Returns an empty
        list when no active user has an email on record.
    """
    active_emails = []

    for user in users:
        if user.get("is_active") and "email" in user:
            active_emails.append(user["email"])

    return active_emails
    