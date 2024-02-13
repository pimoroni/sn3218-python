def test_setup_bus1(smbus, sn3218, gpio):
    gpio.RPI_REVISION = 3
    sn3218 = sn3218.SN3218()
    assert smbus.SMBus.called_once_with(1)
    del sn3218


def test_setup_bus0(smbus, sn3218, gpio):
    gpio.RPI_REVISION = 1
    sn3218 = sn3218.SN3218()
    assert smbus.SMBus.called_once_with(0)
    del sn3218
