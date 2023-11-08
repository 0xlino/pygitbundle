from pygitbundle import create_bundle, verify_bundle, unpack_bundle, encrypt_bundle_with_password

# Test create_bundle
def test_create_bundle():
    create_bundle('test.bundle', '.')
    assert True

def test_verify_bundle():
    verify_bundle('test.bundle', '.')
    assert True

def test_unpack_bundle():
    unpack_bundle('test.bundle', '.')
    assert True

def test_encrypt_bundle_with_password():
    encrypt_bundle_with_password('test.bundle', '.', 'password')
    assert True

# Run on main python
def main():
    test_create_bundle()
    test_verify_bundle()
    test_unpack_bundle()
    test_encrypt_bundle_with_password()


if __name__ == "__main__":
    main()


