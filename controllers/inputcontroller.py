import re
from datetime import datetime

class InputController:
    @staticmethod
    def is_last_name(input_string):
        # Pattern for valid last names (starts with uppercase, only letters with accents allowed)
        pattern = r"^[A-ZÉÈÊËÀÂÄÎÏÔÖÛÜÇ][a-zéèêëàâäîïôöûüç]+$"
        if re.match(pattern, input_string):
            return True
        return False
    
    @staticmethod
    def is_first_name(input_string):
        
        # Pattern for valid first names (allows hyphens and apostrophes)
        pattern = r"^[A-ZÉÈÊËÀÂÄÎÏÔÖÛÜÇ][a-zéèêëàâäîïôöûüç'-]*$"
        if re.match(pattern, input_string):
            return True
        return False
    
    def is_date_past(input_string):
        # Pattern for French date format DD/MM/YYYY
        pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}$"
        if re.match(pattern, input_string):
            try:
                # Check if the date is valid and not in the future
                birthday = datetime.strptime(input_string, "%d/%m/%Y")
                if birthday <= datetime.now():
                    return True
            except ValueError:
                return False
        return False
    
    def is_date(date_string):
        # Regular expression for DD/MM/YYYY format
        pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}$"
        if re.match(pattern, date_string):
            try:
                # Check if the date is valid
                datetime.strptime(date_string, "%d/%m/%Y")
                return True
            except ValueError:
                return False
        return False

    @staticmethod
    def is_valid_id_chess(id_chess_string):
        # Pattern for two letters followed by five digits
        pattern = r"^[A-Za-z]{2}[0-9]{5}$"
        return bool(re.match(pattern, id_chess_string))

    def is_tournament_name(name):
        # Pattern for tournament names:
        # - Start with an uppercase letter.
        # - Allow letters, spaces, hyphens, apostrophes, accented characters, and digits.
        # - Must be at least 3 characters long.
        pattern = r"^[A-ZÉÈÊËÀÂÄÎÏÔÖÛÜÇ][a-zA-Zéèêëàâäîïôöûüç0-9' -]{2,}$"
        return bool(re.match(pattern, name))
    
    def is_location_name(name):
        # Pattern for valid location names:
        # - Starts with an uppercase letter.
        # - Allows letters, digits, spaces, hyphens, apostrophes, and accented characters.
        # - Must be at least 2 characters long.
        pattern = r"^[A-ZÉÈÊËÀÂÄÎÏÔÖÛÜÇ][a-zA-Z0-9éèêëàâäîïôöûüç' -]{1,}$"
        return bool(re.match(pattern, name))