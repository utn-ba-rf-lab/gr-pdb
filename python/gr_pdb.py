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
from numpy import log, zeros, abs, sign,exp


class gr_pdb(gr.sync_block):
    """
    docstring for block gr-pdb
    """
    def __init__(self,num_bits,companding,constant_u,constant_a):
        gr.sync_block.__init__(self,
            name="gr_pdb",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32,numpy.float32,numpy.float32])

        self.num_bits=num_bits
        self.companding=companding
        self.constant_u=constant_u
        self.constant_a=constant_a



    def calculate(self):
        
        #self.result = [(lambda A,N : float( int ( round( A* (pow(2,(N-1))-1))) / (pow(2,(N-1)) -1) )) (self.sample[x],self.num_bits) for x in range(len(self.sample))]
        self.result = [(lambda A,N : float( int ( round( A* (pow(2,(N-1))-1))) / (pow(2,(N-1)) -1) )) ( self.sample[x] if abs(self.sample[x]) < 1 else numpy.sign(self.sample[x]) , self.num_bits) for x in range(len(self.sample))]
        return self.result

    def calculate2(self):
        
        self.result2 = [(lambda A,N : float( int ( round( A* (pow(2,(N-1))-1))) / (pow(2,(N-1)) -1) )) ( self.sample2[x] if abs(self.sample2[x]) < 1 else numpy.sign(self.sample2[x]) , self.num_bits) for x in range(len(self.sample2))]
        return self.result2

    def set_bits(self,num_bits):

        self.num_bits=num_bits
            
    def set_constant_u(self,constant_u):

        self.constant_u=constant_u



    def set_constant_a(self,constant_a):

        self.constant_a = constant_a

    def lin2alaw(self, x):
        '''
        Método para aplicarle ley-a a la señal de entrada x
        Recibe un vector de floats.
        Devuelve un vector de floats
        '''
        
        abs_x = abs(x)                              # Obtengo el módulo de la entrada
        INV_DIV_A = 1/(1+log(self.constant_a))
        INV_A = numpy.float32(1/self.constant_a)

        opt1 = self.constant_a * abs_x * INV_DIV_A                # Obtengo un vector con los valores para los casos en que mod_x < 1/A
        opt2 = 1 + log(abs_x) * INV_DIV_A           # Obtengo un vector con los valores para los casos en que mod_x > 1/A

        y = zeros(len(x), dtype = numpy.float32)       # Creo un vector de ceros para guardar la salida

        i=0                                         # Seteo un contador para indexar
        for n in abs_x:                             # Inicio el algoritmo de ley-a
            if(n < INV_A):
                y[i] = opt1[i]
            else:
                y[i] = opt2[i]
            i+=1
        
        return y*sign(x)


    def alaw2lin(self,x):
        '''
        Método para linealizar una la señal de entrada x comprimida en ley-a
        Recibe un vector de floats.
        Devuelve un vector de floats
        '''
        abs_x = abs(x)                              # Obtengo el módulo de la entrada

        INV_A = numpy.float32(1/self.constant_a)
        INV_DIV_A = 1/(1+log(self.constant_a))

        opt1 = abs_x * (1 + log(self.constant_a)) * INV_A         # Obtengo un vector con los valores para los casos en que mod_x < 1/1+ ln(A)
        opt2 = exp(abs_x * (1+log(self.constant_a)) -1)* INV_A   # Obtengo un vector con los valores para los casos en que mod_x < 1/1+ ln(A)

        y = zeros(len(x), dtype = numpy.float32)       # Creo un vector de ceros para guardar la salida

        i=0                                         # Seteo un contador para indexar
        for n in abs_x:                             # Inicio el algoritmo de ley-a

            if(n < INV_DIV_A):
                y[i] = opt1[i]
                
            elif(n > INV_DIV_A):
                y[i] = opt2[i]
            i+=1

        return sign(x) * y


    def lin2ulaw(self,x):
        '''
        Método para aplicarle ley-u a la señal de entrada x
        Recibe un vector de floats.
        Devuelve un vector de floats
        '''
        
        INV_ULAW_DEN = 1/log(1+self.constant_u)

        ulaw_num = log(1 + self.constant_u * abs(x)) 
        return sign(x) * ulaw_num * INV_ULAW_DEN



    def ulaw2lin(self,x):
        '''
        Método para linealizar una la señal de entrada x comprimida en ley-u
        Recibe un vector de floats.
        Devuelve un vector de floats
        '''
        INV_ULAW = numpy.float32(1/self.constant_u)
        ulaw_num = pow((1+ self.constant_u),abs(x)) -1
        return sign(x) * INV_ULAW * ulaw_num




    def signal_compression(self, in0):


        if(self.companding == "ulaw"):        # u-Law
            x1 = self.lin2ulaw(in0)

        elif(self.companding == "alaw"):      # A-Law
            x1 = self.lin2alaw(in0)

        else:                               # Linear
            x1 = in0

        return x1    


    def signal_expansion(self, in0):

        in0_compress = self.signal_compression(in0)

        if(self.companding == "ulaw"):        # u-Law
            x1 = self.ulaw2lin(in0_compress)

        elif(self.companding == "alaw"):      # A-Law
            x1 = self.alaw2lin(in0_compress)

        else:                               # Linear
            x1 = in0

        return x1         


    def signal_process(self, in0):


        if(self.companding == "ulaw"):        # u-Law
            self.sample2 = self.lin2ulaw(in0)
            x1 = self.calculate2()
            x1 = self.ulaw2lin(x1)

        elif(self.companding == "alaw"):      # A-Law
            self.sample2 = self.lin2alaw(in0)
            x1 = self.calculate2()
            x1 = self.alaw2lin(x1)
        else:                               # Linear
            x1 = in0

        return x1    


    def work(self, input_items, output_items):
        self.sample = input_items[0]
        self.sample2 = input_items[0]

        output_items[0][:] = self.calculate()
        output_items[1][:] = self.signal_process(input_items[0])
        output_items[2][:] = self.signal_compression(input_items[0])

        return len(output_items[0])
