#!/usr/bin/env python
""" Class representing a AI Model.

Represents a AI Model. AI Models are used by AI Agents to process
incoming data.

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

from modules.AbstractModel import AbstractModel


class model(AbstractModel):
	""" Class representing a AI Model.

	This object represents a AI Model.AI Models are used by AI Agents
	to process incoming data.
	"""

	def prepare_data(self):
		""" Creates/sorts dataset. """
		pass

	def prepare_network(self):
		""" Builds the network. """
		pass

	def train(self):
		""" Trains the model

		Trains the neural network.
		"""
		pass

	def freeze_model(self):
		""" Freezes the model """
		pass

	def save_model_as_json(self):
		""" Saves the model as JSON """
		pass

	def save_weights(self):
		""" Saves the model weights """
		pass

	def visualize_metrics(self):
		""" Visualize the metrics. """
		pass

	def confusion_matrix(self):
		""" Prints/displays the confusion matrix. """
		pass

	def figures_of_merit(self):
		""" Calculates/prints the figures of merit.

		https://homes.di.unimi.it/scotti/all/
		"""
		pass

	def load(self):
		""" Loads the model """
		pass

	def evaluate(self):
		""" Evaluates the model """
		pass

	def predictions(self):
		""" Gets a prediction for an image. """
		pass

	def predict(self, img):
		""" Gets a prediction for an image. """
		pass

	def reshape(self, img):
		""" Reshapes an image. """
		pass

	def test(self):
		""" Test mode

		Loops through the test directory and classifies the images.
		"""
		pass
