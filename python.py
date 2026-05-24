# INTEGERS
integers = {
    # 1. Binary & Bitwise Operations
    'bit_length': 'bit_length(): Returns the number of bits required to represent the integer in binary, excluding the sign and leading zeros. (37).bit_length() -> 6',
    'bit_count': 'bit_count(): Returns the number of ones (1s) in the binary representation of the absolute value of the integer (added in Python 3.10). (37).bit_count() -> 3',

    # 2. Ratios
    'as_integer_ratio': 'as_integer_ratio(): Returns a tuple of two integers whose ratio exactly equals the integer. For whole numbers, the second number is always 1. (10).as_integer_ratio() -> (10, 1)',

    # 3. Byte Conversions
    'to_bytes': 'to_bytes(): Converts the integer into an array of bytes for low-level memory storage or network transmission. (1024).to_bytes(2, byteorder="big") -> b"\\x04\\x00"',
    'from_bytes': 'from_bytes(): A class method that converts an array of bytes back into a standard integer. int.from_bytes(b"\\x04\\x00", byteorder="big") -> 1024'
}
# FLOATS
floats = {
    # 1. Type Checking & Fractions
    'is_integer': 'is_integer(): Returns True if the float has no fractional part (ends exactly in .0). (2.5).is_integer() -> False',
    'as_integer_ratio': 'as_integer_ratio(): Returns a tuple of two integers whose exact mathematical ratio equals the float. (0.5).as_integer_ratio() -> (1, 2)',

    # 2. Hexadecimal Conversions
    'hex': 'hex(): Returns a hexadecimal string representation of the floating-point number. (1.5).hex() -> "0x1.8000000000000p+0"',
    'fromhex': 'fromhex(): A class method that converts a hexadecimal string back into a standard float. float.fromhex("0x1.8p+0") -> 1.5'
}
# STRINGS
strings = {
    # 1. Changing Case
    'capitalize': 'capitalize(): Capitalizes only the very first character; lowers the rest. "hello WORLD".capitalize() -> "Hello world"',
    'lower': 'lower(): Converts all characters to lowercase. "HeLlO".lower() -> "hello"',
    'upper': 'upper(): Converts all characters to uppercase. "hello".upper() -> "HELLO"',
    'title': 'title(): Capitalizes the first letter of every word (Title Case). "hello world".title() -> "Hello World"',
    'swapcase': 'swapcase(): Flips uppercase to lowercase and vice versa. "Hello".swapcase() -> "hELLO"',
    'casefold': 'casefold(): Removes all case distinctions for aggressive matching. "groß".casefold() -> "gross"',

    # 2. Searching & Counting
    'count': 'count(): Counts how many times a substring appears. "banana".count("an") -> 2',
    'find': 'find(): Returns first index of substring, or -1 if not found. "hello".find("l") -> 2',
    'rfind': 'rfind(): Returns last index of substring, or -1 if not found. "hello".rfind("l") -> 3',
    'index': 'index(): Returns first index of substring, raises ValueError if not found. "hello".index("l") -> 2',
    'rindex': 'rindex(): Returns last index of substring, raises ValueError if not found. "hello".rindex("l") -> 3',

    # 3. Formatting & Padding
    'center': 'center(): Centers string inside space padding of a given width. "hi".center(6) -> "  hi  "',
    'ljust': 'ljust(): Left-justifies string inside space padding of a given width. "hi".ljust(5) -> "hi   "',
    'rjust': 'rjust(): Right-justifies string inside space padding of a given width. "hi".rjust(5) -> "   hi"',
    'zfill': 'zfill(): Pads left side of string with zeros to a given width. "42".zfill(5) -> "00042"',
    'expandtabs': 'expandtabs(): Replaces tab characters (\\t) with spaces. "a\\tb".expandtabs(2) -> "a b"',
    'format': 'format(): Injects variables into bracket {} placeholders. "{}, {}!".format("Hello", "World") -> "Hello, World!"',
    'format_map': 'format_map(): Maps dictionary keys directly into named placeholders. "{n}".format_map({"n": "Alice"}) -> "Alice"',

    # 4. Stripping & Trimming
    'strip': 'strip(): Removes leading and trailing whitespace. "  hi  ".strip() -> "hi"',
    'lstrip': 'lstrip(): Removes leading whitespace from the left side. "  hi  ".lstrip() -> "hi  "',
    'rstrip': 'rstrip(): Removes trailing whitespace from the right side. "  hi  ".rstrip() -> "  hi"',
    'removeprefix': 'removeprefix(): Cuts off a specific starting substring if present. "test_file.py".removeprefix("test_") -> "file.py"',
    'removesuffix': 'removesuffix(): Cuts off a specific ending substring if present. "test_file.py".removesuffix(".py") -> "test_file"',

    # 5. Splitting, Joining & Partitioning
    'split': 'split(): Breaks a string into a list based on a delimiter. "a b c".split() -> ["a", "b", "c"]',
    'rsplit': 'rsplit(): Breaks a string into a list starting from the right side. "a b c".rsplit(maxsplit=1) -> ["a b", "c"]',
    'splitlines': 'splitlines(): Splits a string at line breaks (\\n) into a list. "a\\nb".splitlines() -> ["a", "b"]',
    'join': 'join(): Glues a list of strings together using the main string. "-".join(["a", "b"]) -> "a-b"',
    'partition': 'partition(): Splits at first delimiter into a 3-tuple (before, match, after). "a-b-c".partition("-") -> ("a", "-", "b-c")',
    'rpartition': 'rpartition(): Splits at last delimiter into a 3-tuple (before, match, after). "a-b-c".rpartition("-") -> ("a-b", "-", "c")',

    # 6. Replacing & Translating
    'replace': 'replace(): Swaps an old substring for a new one. "abc".replace("b", "z") -> "azc"',
    'maketrans': 'maketrans(): Creates a translation dictionary map for character swapping. str.maketrans("ae", "12") -> {97: 49, 101: 50}',
    'translate': 'translate(): Applies a maketrans map to swap characters in text. "apple".translate(table) -> "1ppl2"',
    'encode': 'encode(): Converts string into bytes (defaults to UTF-8). "hi".encode("utf-8") -> b"hi"',

    # 7. Boolean Verification (is...)
    'startswith': 'startswith(): True if the string starts with the given value. "apple".startswith("ap") -> True',
    'endswith': 'endswith(): True if the string ends with the given value. "apple".endswith("le") -> True',
    'isalnum': 'isalnum(): True if all characters are letters or numbers. "a1".isalnum() -> True',
    'isalpha': 'isalpha(): True if all characters are letters only. "abc".isalpha() -> True',
    'isascii': 'isascii(): True if all characters fit in the standard ASCII table. "hi".isascii() -> True',
    'islower': 'islower(): True if all cased characters are lowercase. "hi".islower() -> True',
    'isupper': 'isupper(): True if all cased characters are uppercase. "HI".isupper() -> True',
    'istitle': 'istitle(): True if string follows Title Case rules. "Hello World".istitle() -> True',
    'isspace': 'isspace(): True if string contains only whitespace characters. " \\n\\t ".isspace() -> True',
    'isprintable': 'isprintable(): True if all characters are visible/printable. "hi".isprintable() -> True',
    'isidentifier': 'isidentifier(): True if string is a valid variable name pattern. "my_var1".isidentifier() -> True',
    'isdecimal': 'isdecimal(): True if string only contains strict digits 0-9. "123".isdecimal() -> True',
    'isdigit': 'isdigit(): True if string contains digits 0-9 or superscripts. "123²".isdigit() -> True',
    'isnumeric': 'isnumeric(): True if string contains digits, superscripts, or fractions. "½".isnumeric() -> True'
}
# LIST
lists = {
    # 1. Adding Elements
    'append': 'append(): Adds a single element to the very end of the list in place. [1, 2].append(3) -> [1, 2, 3]',
    'extend': 'extend(): Appends all elements from an iterable (like another list) to the end in place. [1].extend([2, 3]) -> [1, 2, 3]',
    'insert': 'insert(): Inserts an element at a specific index, shifting everything else right. [1, 3].insert(1, 2) -> [1, 2, 3]',

    # 2. Removing Elements
    'pop': 'pop(): Removes and RETURNS the element at a given index (defaults to the last item). [10, 20].pop() -> returns 20, list becomes [10]',
    'remove': 'remove(): Removes the first occurrence of a specific value; raises ValueError if not found. [1, 2, 1].remove(1) -> [2, 1]',
    'clear': 'clear(): Removes all elements from the list, leaving it completely empty. [1, 2].clear() -> []',

    # 3. Searching & Counting
    'count': 'count(): Returns the number of times a specific value appears in the list. [1, 2, 2].count(2) -> 2',
    'index': 'index(): Returns the first index of a value; raises ValueError if the value is missing. ["a", "b"].index("b") -> 1',

    # 4. Ordering & Reversing
    'sort': 'sort(): Sorts the list items in place (ascending order by default). [3, 1, 2].sort() -> [1, 2, 3]',
    'reverse': 'reverse(): Reverses the order of the elements in the list completely in place. [1, 2, 3].reverse() -> [3, 2, 1]',

    # 5. Copying
    'copy': 'copy(): Returns a shallow, independent copy of the original list. old = [1, 2]; new = old.copy() -> new becomes [1, 2]'
}
# DICTIONARY
dictionaries = {
    # 1. Retrieving Values Safely
    'get': 'get(): Returns the value for a key if it exists; otherwise returns a default value (None if not specified) without crashing. {"a": 1}.get("b", 0) -> 0',
    'setdefault': 'setdefault(): Returns the value of a key if it exists. If not, inserts the key with a specified default value. d = {"a": 1}; d.setdefault("b", 2) -> returns 2, d becomes {"a": 1, "b": 2}',

    # 2. Accessing Keys, Values & Pairs (View Objects)
    'keys': 'keys(): Returns a dynamic view object of all keys in the dictionary. {"a": 1, "b": 2}.keys() -> dict_keys(["a", "b"])',
    'values': 'values(): Returns a dynamic view object of all values in the dictionary. {"a": 1, "b": 2}.values() -> dict_values([1, 2])',
    'items': 'items(): Returns a dynamic view object of all key-value pairs as a list of tuples. {"a": 1}.items() -> dict_items([("a", 1)])',

    # 3. Adding & Modifying Data
    'update': 'update(): Merges another dictionary or iterable of key-value pairs into the current one, overwriting existing keys in place. {"a": 1}.update({"b": 2}) -> {"a": 1, "b": 2}',
    'fromkeys': 'fromkeys(): A class method that creates a new dictionary with a given sequence of keys and a single shared value. dict.fromkeys(["a", "b"], 0) -> {"a": 0, "b": 0}',

    # 4. Removing Data
    'pop': 'pop(): Removes a specific key and returns its value; raises KeyError if missing unless a default fallback is provided. {"a": 1}.pop("a") -> returns 1, dict becomes {}',
    'popitem': 'popitem(): Removes and returns the LAST inserted key-value pair as a tuple (LIFO order). {"a": 1, "b": 2}.popitem() -> returns ("b", 2), dict becomes {"a": 1}',
    'clear': 'clear(): Removes all keys and values, leaving the dictionary completely empty. {"a": 1}.clear() -> {}',

    # 5. Copying
    'copy': 'copy(): Returns a shallow, independent copy of the original dictionary. old = {"a": 1}; new = old.copy() -> new becomes {"a": 1}'
}
# TUPLES
tuples = {
    # Searching & Counting
    'count': 'count(): Returns the number of times a specified value appears in the tuple. (1, 2, 2, 3).count(2) -> 2',
    'index': 'index(): Returns the first index of a specified value; raises ValueError if the value is missing. ("a", "b", "c").index("b") -> 1'
}
# SETS
sets = {
    # 1. Adding & Removing
    'add': 'add(): Adds an element to the set. If the element is already present, the set remains unchanged. {1, 2}.add(3) -> {1, 2, 3}',
    'remove': 'remove(): Removes a specified element; raises KeyError if the element is not found. {1, 2}.remove(1) -> {2}',
    'discard': 'discard(): Removes a specified element; does nothing (no error) if the element is not found. {1, 2}.discard(3) -> {1, 2}',
    'pop': 'pop(): Removes and returns an arbitrary element from the set; raises KeyError if the set is empty. {1, 2}.pop() -> 1',
    'clear': 'clear(): Removes all elements from the set. {1, 2}.clear() -> set()',

    # 2. Set Operations (Mathematical)
    'union': 'union(): Returns a new set containing all unique elements from both sets. {1, 2}.union({2, 3}) -> {1, 2, 3}',
    'intersection': 'intersection(): Returns a new set with elements common to both sets. {1, 2}.intersection({2, 3}) -> {2}',
    'difference': 'difference(): Returns a new set with elements in the first set but not in the second. {1, 2}.difference({2, 3}) -> {1}',
    'symmetric_difference': 'symmetric_difference(): Returns a new set with elements in either set, but not both. {1, 2}.symmetric_difference({2, 3}) -> {1, 3}',

    # 3. Membership & Subsets
    'issubset': 'issubset(): Returns True if all elements of the set are present in another set. {1, 2}.issubset({1, 2, 3}) -> True',
    'issuperset': 'issuperset(): Returns True if the set contains all elements of another set. {1, 2, 3}.issuperset({1, 2}) -> True',
    'isdisjoint': 'isdisjoint(): Returns True if the two sets have no elements in common. {1, 2}.isdisjoint({3, 4}) -> True',

    # 4. Copying
    'copy': 'copy(): Returns a shallow copy of the set. s = {1, 2}; s2 = s.copy() -> s2 becomes {1, 2}'
}


# The explain function
def explain(object: str, method: str) -> str:
    '''
    Retrieves and prints the explanation for a specific method of a given Python data structure.

    This function acts as a lookup utility. It maps a string identifier for a data structure
    to its corresponding dictionary of method explanations, then prints the definition 
    and usage example for the requested method.

    Args:
        object (str): The name of the data structure (e.g., 'list', 'dict', 'int').
        method (str): The specific method name to explain (e.g., 'append', 'get').

    Returns:
        None: The function directly prints the explanation to the standard output.
        If the method or object type is not found, it prints an error message.
    '''
    #integer
    if str(object) in ['int', 'integer', 'integers']:
        print(f"{object}.{integers.get(method, f"Error: Method '{method}' not found in {object}")}")
    #float
    if str(object) in ['float', 'floats']:
        print(f"{object}.{floats.get(method, f"Error: Method '{method}' not found in {object}")}") 
    #string
    if str(object) in ['string', 'str', 'strings']:
        print(f"{object}.{strings.get(method, f"Error: Method '{method}' not found in {object}")}")
    #list
    if str(object) in ['list', 'lists']:
        print(f"{object}.{lists.get(method, f"Error: Method '{method}' not found in {object}")}")
    #dictionary
    if str(object) in ['dict', 'dictionary', 'dictionaries']:
        print(f"{object}.{dictionaries.get(method, f"Error: Method '{method}' not found in {object}")}") 
    #tuple
    if str(object) in ['tuple', 'tuples']:
        print(f"{object}.{tuples.get(method, f"Error: Method '{method}' not found in {object}")}") 
    #set
    if str(object) in ['set', 'sets']:
        print(f"{object}.{sets.get(method, f"Error: Method '{method}' not found in {object}")}")



#Methods list function
def methods_list(object: str) -> None:
    """
    Displays all available method names for a specified Python data structure.

    This function utilizes a routing dictionary to map user input aliases 
    (e.g., 'lst', 'list', 'lists') to their corresponding method databases. 
    It prints the list of method names available for the specified type.

    Args:
        object (str): The common name or abbreviation of the data structure 
            to look up (e.g., 'list', 'dict', 'int', 'tuple', 'str', 'set').

    Returns:
        None: The function directly prints the list of available method 
            names (or an error message if the type is not found) to 
            standard output.

    Example:
        >>> methods_list('list')
        List methods: ['append', 'extend', 'insert', 'pop', 'remove', ...]
    """
    # Map all valid inputs to their respective data dictionaries
    router = {
        'int': integers, 'integer': integers, 'integers': integers,
        'float': floats, 'floats': floats,
        'str': strings, 'string': strings, 'strings': strings,
        'list': lists, 'lists': lists, 'lst': lists,
        'dict': dictionaries, 'dictionary': dictionaries, 'dictionaries': dictionaries,
        'tuple': tuples, 'tuples': tuples,
        'set': sets, 'sets': sets
    }
    
    # Simple lookup
    data = router.get(object.lower())
    if data:
        print(f"{object.capitalize()} methods: {list(data.keys())}")
    else:
        print(f"'{object}' not in library")




explain('dictionary', 'pop')
methods_list('tuple')
