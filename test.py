from pygitbundle import MY_CUSTOM_VAR, MY_CUSTOM_VAR2, create_bundle, verify_bundle, unpack_bundle

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

# Run on main python
def main():
    test_create_bundle()
    test_verify_bundle()
    test_unpack_bundle()

if __name__ == "__main__":
    main()


