import validator

def test_validate_name_good():
    assert validator.validate_name("Cæsar Test Østergård",80) == True


def test_validate_name_too_long():
    assert validator.validate_name("Cæsar Test Østergård",10) == False


def test_validate_name_too_short():
    assert validator.validate_name("E Å",10) == False


def test_validate_name_bad_format():
    assert validator.validate_name("ljsadk34 ###",20) == False


def test_validate_street_name_good():
    assert validator.validate_street_name("Testgrusgraven") == True


def test_validate_street_name_bad():
    assert validator.validate_street_name("18ende Kartoffelrække") == False


def test_validate_street_number_good():
    assert validator.validate_street_number("132") == True


def test_validate_street_number_bad():
    assert validator.validate_street_number("-20") == False


def test_validate_street_number_bad_2():
    assert validator.validate_street_number("XIV") == False


def test_validate_zip_code_good():
    assert validator.validate_zip_code("2820") == True


def test_validate_zip_code_good():
    assert validator.validate_zip_code("2820") == True


def test_validate_zip_code_bad():
    assert validator.validate_zip_code("12820") == False

def test_validate_zip_code_badformat():
    assert validator.validate_zip_code("#1820") == False


def test_validate_city_name():
    assert validator.validate_city_name("Gentofte") == True


def test_validate_city_name():
    assert validator.validate_city_name("Æble_grød_213-.¤2") == False



# The next two tests will only work with a valid cpr number!
# e.g. try it on your own laptop with your own cpr-number

#def test_validate_cpr_number_good():
#    assert validator.validate_cpr_number("xxxxxx-yyyy") == True
#
#
#def test_validate_cpr_number_good2():
#    assert validator.validate_cpr_number("xxxxxxyyyy") == True
#

def test_validate_cpr_number_bad():
    assert validator.validate_cpr_number("-010490+9995!") == False
