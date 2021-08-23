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
    def __init__(self,num_bits):
        gr.sync_block.__init__(self,
            name="gr_pdb",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])

        self.num_bits=num_bits
        #self.a=0
        #self.b=0

    def calculate(self):
        
        self.result = [(lambda A,N : float( int ( round( A* (pow(2,(N-1))-1))) / (pow(2,(N-1)) -1) )) ( self.sample[x] if abs(self.sample[x]) < 1 else numpy.sign(self.sample[x]) , self.num_bits) for x in range(len(self.sample))]
        return self.result

        
    def set_bits(self,num_bits):

        self.num_bits = num_bits


    def work(self, input_items, output_items):
        self.sample = input_items[0]
        output_items[0][:] = self.calculate()
 
        return len(output_items[0])

        #if(self.a!= self.num_bits or self.b!= self.sample):
        #self.a=self.num_bits
        #self.b=self.sample

        return 0
