#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 gr-pdb author.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#


import numpy
from gnuradio import gr

class gr_pdb(gr.sync_block):
    """
    docstring for block gr-pdb
    """
    def __init__(self,num_bits,sample):
        gr.sync_block.__init__(self,
            name="gr_pdb",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])

        self.num_bits=num_bits
        self.sample = sample
        self.a=0
        self.b=0

    def calculate(self,sample):
        self.result = (lambda A,N : float( int ( round( A* (pow(2,(N-1))-1))) / (pow(2,(N-1)) -1) )) (sample,self.num_bits)
        print(self.result)
        
    def set_bits(self,num_bits):
        print("[INFO] | Self: {}".format(self.num_bits))

        self.num_bits = num_bits
        print("[INFO] | Slider: {}".format(num_bits))

    def set_sample(self,sample):

        self.sample = sample

    def work(self, input_items, output_items):
        self.sample = input_items[0]
        
        if(self.a!= self.num_bits or self.b!= self.sample):
          self.calculate(self.sample)
          self.a=self.num_bits
          self.b=self.sample

        output_items[0] = input_items[0]
#        consume(0, len(input_items[0]))        #self.consume_each(len(input_items[0]))
        return 0
