from smbus import SMBus

__version__ = '2.0.0'


I2C_ADDRESS = 0x54
CMD_ENABLE_OUTPUT = 0x00
CMD_SET_PWM_VALUES = 0x01
CMD_ENABLE_LEDS = 0x13
CMD_UPDATE = 0x16
CMD_RESET = 0x17

_sn3218 = None  # For module compatibiity shim


class SN3218:
    def __init__(self, i2c_bus=None, i2c_dev=None, enable_mask=0b111111111111111111):
        if i2c_dev is None:
            if i2c_bus is None:
                import RPi.GPIO as GPIO
                if GPIO.RPI_REVISION < 2:
                    i2c_bus = 0
                else:
                    i2c_bus = 1

            self.i2c = SMBus(i2c_bus)
        else:
            self.i2c = i2c_dev

        # generate a good default gamma table
        self.default_gamma_table = [int(pow(255, float(i - 1) / 255)) for i in range(256)]
        self.channel_gamma_table = [self.default_gamma_table for _ in range(18)]

        self.enable_leds(enable_mask)

    def enable(self):
        """Enable output."""
        self.i2c.write_i2c_block_data(I2C_ADDRESS, CMD_ENABLE_OUTPUT, [0x01])

    def disable(self):
        """Disable output."""
        self.i2c.write_i2c_block_data(I2C_ADDRESS, CMD_ENABLE_OUTPUT, [0x00])

    def reset(self):
        """Reset all internal registers."""
        self.i2c.write_i2c_block_data(I2C_ADDRESS, CMD_RESET, [0xFF])

    def enable_leds(self, enable_mask):
        """Enable or disable each LED channel.

        The first 18 bit values are
        used to determine the state of each channel (1=on, 0=off) if fewer
        than 18 bits are provided the remaining channels are turned off.

        Args:
            enable_mask (int): up to 18 bits of data
        Raises:
            TypeError: if enable_mask is not an integer.
        """
        if not isinstance(enable_mask, int):
            raise TypeError("enable_mask must be an integer")

        self.i2c.write_i2c_block_data(I2C_ADDRESS, CMD_ENABLE_LEDS, [
            enable_mask & 0x3F,
            (enable_mask >> 6) & 0x3F,
            (enable_mask >> 12) & 0X3F])
        self.i2c.write_i2c_block_data(I2C_ADDRESS, CMD_UPDATE, [0xFF])

    def channel_gamma(self, channel, gamma_table):
        """Override the gamma table for a single channel.

        Args:
            channel (int): channel number
            gamma_table (list): list of 256 gamma correction values
        Raises:
            TypeError: if channel is not an integer.
            ValueError: if channel is not in the range 0..17.
            TypeError: if gamma_table is not a list.
        """
        if not isinstance(channel, int):
            raise TypeError("channel must be an integer")

        if channel not in range(18):
            raise ValueError("channel be an integer in the range 0..17")

        if not isinstance(gamma_table, list) or len(gamma_table) != 256:
            raise TypeError("gamma_table must be a list of 256 integers")

        self.channel_gamma_table[channel] = gamma_table

    def output(self, values):
        """Output a new set of values to the driver.

        Args:
            values (list): channel number
        Raises:
            TypeError: if values is not a list of 18 integers.
        """
        if not isinstance(values, list) or len(values) != 18:
            raise TypeError("values must be a list of 18 integers")

        self.i2c.write_i2c_block_data(I2C_ADDRESS, CMD_SET_PWM_VALUES, [self.channel_gamma_table[i][values[i]] for i in range(18)])
        self.i2c.write_i2c_block_data(I2C_ADDRESS, CMD_UPDATE, [0xFF])

    def output_raw(self, values):
        """Output a new set of values to the driver.

        Similar to output(), but does not use channel_gamma_table.

        Args:
            values (list): channel number
        Raises:
            TypeError: if values is not a list of 18 integers.
        """
        # SMBus.write_i2c_block_data does the type check, so we don't have to
        if len(values) != 18:
            raise TypeError("values must be a list of 18 integers")

        self.i2c.write_i2c_block_data(I2C_ADDRESS, CMD_SET_PWM_VALUES, values)
        self.i2c.write_i2c_block_data(I2C_ADDRESS, CMD_UPDATE, [0xFF])


# Module-method compatibility shim

def _get_sn3218():
    global _sn3218
    if _sn3218 is None:
        _sn3218 = SN3218()
    return _sn3218


def enable():
    _get_sn3218().enable()


def output(values):
    _get_sn3218().output(values)


def output_raw(values):
    _get_sn3218().output_raw(values)


def channel_gamma(channel, gamma_table):
    _get_sn3218().enable()


def enable_leds(enable_mask):
    _get_sn3218().enable_leds(enable_mask)


def reset():
    _get_sn3218().reset()
