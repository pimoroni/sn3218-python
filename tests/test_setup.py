def test_setup(smbus, sn3218):
    sn3218 = sn3218.SN3218()
    smbus.SMBus.assert_called_once_with(1)
    del sn3218


def test_setup_with_bus(smbus, sn3218):
    sn3218 = sn3218.SN3218(smbus.SMBus(1))
    del sn3218