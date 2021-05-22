#!/usr/bin/env python
""" AI Model Data Class.

Provides the AI Model with the required required data
processing functionality.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files(the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Contributors:

"""

from modules.AbstractData import AbstractData

class data(AbstractData):
	""" AI Model Data Class.

	Provides the AI Model with the required required data
	processing functionality.
	"""

	def pre_process(self):
		""" Processes the images. """
		pass

	def convert_data(self):
		""" Converts the training data to a numpy array. """
		pass

	def encode_labels(self):
		""" One Hot Encodes the labels. """
		pass

	def shuffle(self):
		""" Shuffles the data and labels. """
		pass

	def get_split(self):
		""" Splits the data and labels creating training and validation datasets. """
		pass

	def resize(self, path, dim):
		""" Resizes an image to the provided dimensions (dim). """
		pass
