#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Replay
# Generated: Wed Jan 30 13:09:37 2019
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import wxgui as grc_wxgui
import wx


class replay(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Replay")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.gain_send = gain_send = 120
        self.freq_send = freq_send = 868.4e6
        self.device_addr = device_addr = "serial=XXXXXXX"

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink_0_0 = uhd.usrp_sink(
        	",".join(("serial=XXXXXXX", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0_0.set_subdev_spec('A:A', 0)
        self.uhd_usrp_sink_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0_0.set_center_freq(freq_send, 0)
        self.uhd_usrp_sink_0_0.set_gain(gain_send, 0)
        self.uhd_usrp_sink_0_0.set_antenna('TX/RX', 0)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/user/signal/opening2', True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.uhd_usrp_sink_0_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0_0.set_samp_rate(self.samp_rate)

    def get_gain_send(self):
        return self.gain_send

    def set_gain_send(self, gain_send):
        self.gain_send = gain_send
        self.uhd_usrp_sink_0_0.set_gain(self.gain_send, 0)


    def get_freq_send(self):
        return self.freq_send

    def set_freq_send(self, freq_send):
        self.freq_send = freq_send
        self.uhd_usrp_sink_0_0.set_center_freq(self.freq_send, 0)

    def get_device_addr(self):
        return self.device_addr

    def set_device_addr(self, device_addr):
        self.device_addr = device_addr


def main(top_block_cls=replay, options=None):
    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()
#    i=0
#    while i<1000:
#        i+=1
#        tb.Start(True)


if __name__ == '__main__':
    main()
