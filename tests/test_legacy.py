def test_setup_legacy_bus0(gpio, smbus, sn3218):
    gpio.RPI_REVISION = 1
    sn3218.channel_gamma(0, [int(pow(255, float(i - 1) / 255)) for i in range(256)])
    smbus.SMBus.assert_called_once_with(0)
    sn3218.enable()


def test_setup_legacy_bus1(gpio, smbus, sn3218):
    gpio.RPI_REVISION = 3
    sn3218.channel_gamma(0, [int(pow(255, float(i - 1) / 255)) for i in range(256)])
    smbus.SMBus.assert_called_once_with(1)
    sn3218.enable()
