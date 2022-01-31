def test_setup(smbus, sn3218):
    sn3218 = sn3218.SN3218()
    assert smbus.SMBus.called_once_with(0)
    del sn3218
