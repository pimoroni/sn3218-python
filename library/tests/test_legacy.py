def test_setup(smbus, sn3218):
    sn3218.channel_gamma(0, [int(pow(255, float(i - 1) / 255)) for i in range(256)])
    assert smbus.SMBus.called_once_with(0)
    sn3218.enable()
